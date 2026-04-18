#!/usr/bin/env python3
"""
DB_メモ一覧から直近N日のメモを取得するスクリプト。
各ページの本文を Markdown としても保存する。

使い方:
    python fetch_memos.py <開始日> <終了日> [保存日]
    例: python fetch_memos.py 2026-04-02 2026-04-12 2026-04-12

出力:
    JSON 形式でメモ一覧を標準出力に表示
    保存日を指定すると以下も生成される：
      schedule/data/{保存日}/memos.csv
      schedule/data/{保存日}/memos_all.md        ← 全メモ本文を1ファイルに統合（AI読み取り用）
      schedule/data/{保存日}/memos/{タイトル}.md  ← 各ページの全文（人間が読む用）
"""

import json
import sys

from pathlib import Path

from utils import (
    blocks_to_markdown,
    fetch_page_blocks,
    get_token,
    notion_post,
    save_csv,
    save_json,
    save_page_as_markdown,
)

# DB_メモ一覧 の database_id
MEMO_DB_ID = "43a5556c-0273-49d1-8a35-aafac5b54847"


def fetch_memos(start_date: str, end_date: str, save_date: str = None) -> list[dict]:
    """
    DB_メモ一覧から指定期間に作成されたメモを取得する。
    save_date を指定すると各ページの本文も Markdown として保存する。

    Args:
        start_date: 開始日（YYYY-MM-DD 形式）
        end_date:   終了日（YYYY-MM-DD 形式）
        save_date:  保存日（YYYY-MM-DD 形式）。指定時のみ Markdown 保存

    Returns:
        メモの辞書リスト
    """
    token = get_token()

    url = f"https://api.notion.com/v1/databases/{MEMO_DB_ID}/query"
    memos = []
    cursor = None

    while True:
        # created_time で絞り込み（JST 0:00 〜 23:59:59）
        body: dict = {
            "filter": {
                "and": [
                    {"timestamp": "created_time", "created_time": {"on_or_after": f"{start_date}T00:00:00+09:00"}},
                    {"timestamp": "created_time", "created_time": {"on_or_before": f"{end_date}T23:59:59+09:00"}},
                ]
            },
            "sorts": [{"timestamp": "created_time", "direction": "ascending"}],
            "page_size": 100,
        }
        if cursor:
            body["start_cursor"] = cursor

        response = notion_post(url, token, body)

        for page in response.get("results", []):
            memo = extract_memo(page)

            # 本文ブロックを取得して Markdown に変換
            blocks = fetch_page_blocks(page["id"], token)
            content_md = blocks_to_markdown(blocks, token)
            memo["content_md"] = content_md

            # 保存日が指定されていれば Markdown ファイルとして保存
            if save_date:
                md_header = f"# {memo['name']}\n\n> 作成日時: {memo['created_time']}\n\n---\n\n"
                md_path = save_page_as_markdown(
                    memo["name"], md_header + content_md, save_date, "memos",
                    created_time=memo["created_time"]
                )
                memo["md_file"] = md_path

            memos.append(memo)

        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return memos


def extract_memo(page: dict) -> dict:
    props = page.get("properties", {})

    # 名前（タイトル）
    name = ""
    title_list = props.get("名前", {}).get("title", [])
    if title_list:
        name = title_list[0].get("plain_text", "")

    # ショートプロンプト
    short_prompt = ""
    rt_list = props.get("ショートプロンプト", {}).get("rich_text", [])
    if rt_list:
        short_prompt = rt_list[0].get("plain_text", "")

    # URL
    url = props.get("URL", {}).get("url")

    # 作成日時
    created_time = page.get("created_time", "")

    return {
        "id": page.get("id"),
        "name": name,
        "short_prompt": short_prompt,
        "url": url,
        "created_time": created_time,
    }


def main():
    if len(sys.argv) not in (3, 4):
        print("使い方: python fetch_memos.py <開始日> <終了日> [保存日]", file=sys.stderr)
        print("例:     python fetch_memos.py 2026-04-02 2026-04-12 2026-04-12", file=sys.stderr)
        sys.exit(1)

    save_date = sys.argv[3] if len(sys.argv) == 4 else None
    memos = fetch_memos(sys.argv[1], sys.argv[2], save_date)

    if save_date:
        # content_md は CSV には含めない（長すぎるため）
        csv_records = [{k: v for k, v in m.items() if k not in ("content_md", "md_file")} for m in memos]
        path = save_csv(csv_records, save_date, "memos")
        json_path = save_json(csv_records, save_date, "memos")
        print(f"[memos] {len(memos)}件 → {path}", file=sys.stderr)
        print(f"[memos] JSON  → {json_path}", file=sys.stderr)
        print(f"[memos] 個別MD → schedule/data/{save_date}/memos/", file=sys.stderr)

        # 全メモを1ファイルに統合（AI読み取り用）
        all_md_lines = [f"# メモ一覧 {sys.argv[1]} 〜 {sys.argv[2]}\n"]
        for m in memos:
            all_md_lines.append(f"---\n\n## {m['name']}\n\n> 作成日時: {m['created_time']}\n")
            if m.get("content_md"):
                all_md_lines.append(m["content_md"])
            all_md_lines.append("")

        # ai_context/ フォルダにも保存（他AIへの受け渡し用）
        ai_context_dir = Path(__file__).parent / "data" / save_date / "ai_context"
        ai_context_dir.mkdir(parents=True, exist_ok=True)
        all_md_path = ai_context_dir / "memos_all.md"
        all_md_path.write_text("\n".join(all_md_lines), encoding="utf-8")
        print(f"[memos] 統合MD → {all_md_path}", file=sys.stderr)

    print(json.dumps(memos, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
