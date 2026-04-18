#!/usr/bin/env python3
"""
インタースティシャル・ジャーナリングDB から指定期間のエントリを取得するスクリプト。

使い方:
    python fetch_journals.py <開始日> <終了日>
    例: python fetch_journals.py 2026-04-02 2026-04-12

出力:
    JSON 形式でジャーナルエントリ一覧を標準出力に表示
"""

import json
import sys

from utils import get_token, notion_post, save_csv, save_json

# インタースティシャル・ジャーナリングDB の database_id
JOURNAL_DB_ID = "3046f8be-0227-80ee-8943-fe6b077c80be"


def fetch_journals(start_date: str, end_date: str) -> list[dict]:
    """
    ジャーナリングDB から「日時」が指定範囲内のエントリを取得する。

    Args:
        start_date: 開始日（YYYY-MM-DD 形式）
        end_date:   終了日（YYYY-MM-DD 形式）

    Returns:
        ジャーナルエントリの辞書リスト
    """
    token = get_token()

    url = f"https://api.notion.com/v1/databases/{JOURNAL_DB_ID}/query"
    journals = []
    cursor = None

    while True:
        # 「日時」プロパティで絞り込み
        body: dict = {
            "filter": {
                "and": [
                    {"property": "日時", "date": {"on_or_after": start_date}},
                    {"property": "日時", "date": {"on_or_before": end_date}},
                ]
            },
            "sorts": [{"property": "日時", "direction": "ascending"}],
            "page_size": 100,
        }
        if cursor:
            body["start_cursor"] = cursor

        response = notion_post(url, token, body)

        for page in response.get("results", []):
            journals.append(extract_journal(page))

        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return journals


def extract_journal(page: dict) -> dict:
    props = page.get("properties", {})

    # 終了したこと・完了したこと（タイトル）
    completed = ""
    title_list = props.get("終了したこと・完了したこと", {}).get("title", [])
    if title_list:
        completed = title_list[0].get("plain_text", "")

    # 開始したこと・次にやりたいこと
    next_actions = ""
    rt_list = props.get("開始したこと・次にやりたいこと", {}).get("rich_text", [])
    if rt_list:
        next_actions = "".join(r.get("plain_text", "") for r in rt_list)

    # 気持ち
    feeling = ""
    rt_list = props.get("気持ち", {}).get("rich_text", [])
    if rt_list:
        feeling = "".join(r.get("plain_text", "") for r in rt_list)

    # 日時
    datetime_val = None
    date_prop = props.get("日時", {}).get("date")
    if date_prop:
        datetime_val = date_prop.get("start")

    return {
        "id": page.get("id"),
        "completed": completed,
        "next_actions": next_actions,
        "feeling": feeling,
        "datetime": datetime_val,
    }


def main():
    if len(sys.argv) not in (3, 4):
        print("使い方: python fetch_journals.py <開始日> <終了日> [保存日]", file=sys.stderr)
        print("例:     python fetch_journals.py 2026-04-02 2026-04-12 2026-04-12", file=sys.stderr)
        sys.exit(1)

    save_date = sys.argv[3] if len(sys.argv) == 4 else None
    journals = fetch_journals(sys.argv[1], sys.argv[2])

    if save_date:
        path = save_csv(journals, save_date, "journals")
        json_path = save_json(journals, save_date, "journals")
        print(f"[journals] {len(journals)}件 → {path}", file=sys.stderr)
        print(f"[journals] JSON  → {json_path}", file=sys.stderr)

    print(json.dumps(journals, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
