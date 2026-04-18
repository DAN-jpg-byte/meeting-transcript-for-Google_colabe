"""
Notion fetch スクリプト共通のユーティリティ。
"""

import csv
import json
import os
import urllib.request
from pathlib import Path

NOTION_API_VERSION = "2022-06-28"


def get_token() -> str:
    """環境変数から Notion トークンを取得する。"""
    token = (os.environ.get("NOTION_API_TOKEN") or os.environ.get("NOTION_TOKEN") or "").strip()
    if not token:
        raise RuntimeError("環境変数 NOTION_TOKEN が設定されていません")
    return token


def notion_post(url: str, token: str, body: dict) -> dict:
    """Notion API に POST リクエストを送る。"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_API_VERSION,
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))


def notion_get(url: str, token: str) -> dict:
    """Notion API に GET リクエストを送る。"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_API_VERSION,
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))


def fetch_page_blocks(page_id: str, token: str) -> list[dict]:
    """
    ページの全ブロックを取得する（ページネーション対応）。

    Args:
        page_id: Notion ページID
        token:   Notion API トークン

    Returns:
        ブロックの辞書リスト
    """
    blocks = []
    cursor = None

    while True:
        url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"

        response = notion_get(url, token)
        blocks.extend(response.get("results", []))

        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return blocks


def rich_text_to_str(rich_text_list: list) -> str:
    """rich_text 配列をプレーンテキストに変換する。"""
    return "".join(r.get("plain_text", "") for r in rich_text_list)


def blocks_to_markdown(blocks: list[dict], token: str, depth: int = 0) -> str:
    """
    Notion ブロックリストを Markdown 文字列に変換する。

    Args:
        blocks: Notion API のブロックリスト
        token:  子ブロック取得に使う API トークン
        depth:  インデント深さ（再帰呼び出し用）

    Returns:
        Markdown 文字列
    """
    lines = []
    indent = "  " * depth

    for block in blocks:
        block_type = block.get("type", "")
        content = block.get(block_type, {})
        text = rich_text_to_str(content.get("rich_text", []))

        if block_type == "paragraph":
            lines.append(f"{indent}{text}" if text else "")

        elif block_type == "heading_1":
            lines.append(f"{indent}# {text}")

        elif block_type == "heading_2":
            lines.append(f"{indent}## {text}")

        elif block_type == "heading_3":
            lines.append(f"{indent}### {text}")

        elif block_type == "bulleted_list_item":
            lines.append(f"{indent}- {text}")

        elif block_type == "numbered_list_item":
            lines.append(f"{indent}1. {text}")

        elif block_type == "to_do":
            checked = content.get("checked", False)
            mark = "x" if checked else " "
            lines.append(f"{indent}- [{mark}] {text}")

        elif block_type == "quote":
            lines.append(f"{indent}> {text}")

        elif block_type == "callout":
            emoji = content.get("icon", {}).get("emoji", "")
            lines.append(f"{indent}> {emoji} {text}")

        elif block_type == "code":
            lang = content.get("language", "")
            lines.append(f"{indent}```{lang}")
            lines.append(f"{indent}{text}")
            lines.append(f"{indent}```")

        elif block_type == "divider":
            lines.append(f"{indent}---")

        elif block_type == "child_page":
            child_title = content.get("title", "（サブページ）")
            lines.append(f"{indent}📄 **{child_title}**")
            # サブページの中身を再帰取得
            if block.get("id"):
                child_blocks = fetch_page_blocks(block["id"], token)
                child_md = blocks_to_markdown(child_blocks, token, depth + 1)
                if child_md:
                    lines.append(child_md)

        elif block_type == "image":
            url = (
                content.get("file", {}).get("url")
                or content.get("external", {}).get("url", "")
            )
            caption = rich_text_to_str(content.get("caption", []))
            lines.append(f"{indent}![{caption}]({url})")

        # 子ブロックがある場合（child_page 以外）は再帰取得
        if block.get("has_children") and block_type != "child_page":
            child_blocks = fetch_page_blocks(block["id"], token)
            child_md = blocks_to_markdown(child_blocks, token, depth + 1)
            if child_md:
                lines.append(child_md)

    return "\n".join(lines)


def save_page_as_markdown(title: str, content_md: str, save_date: str, subdir: str, created_time: str = "") -> str:
    """
    ページ内容を Markdown ファイルとして保存する。

    ファイル名は「YYYYMMDD_HHMM_{タイトル}.md」形式。
    同タイトルでも作成日時が違えば別ファイルになる。

    保存先: schedule/data/{save_date}/{subdir}/{YYYYMMDD_HHMM_タイトル}.md

    Args:
        title:        ファイル名に使うタイトル
        content_md:   Markdown 文字列
        save_date:    保存日（YYYY-MM-DD 形式）
        subdir:       サブディレクトリ名（例: "memos"）
        created_time: 作成日時（ISO8601形式。例: 2026-04-05T13:17:00.000Z）

    Returns:
        保存したファイルのパス文字列
    """
    base_dir = Path(__file__).parent / "data" / save_date / subdir
    base_dir.mkdir(parents=True, exist_ok=True)

    # 作成日時をファイル名用に変換（例: 20260405_1317）
    datetime_prefix = ""
    if created_time:
        # ISO8601 → yyyymmdd_hhmm
        dt = created_time.replace("Z", "+00:00")
        try:
            from datetime import datetime, timezone, timedelta
            JST = timezone(timedelta(hours=9))
            parsed = datetime.fromisoformat(dt).astimezone(JST)
            datetime_prefix = parsed.strftime("%Y%m%d_%H%M_")
        except Exception:
            pass

    # ファイル名に使えない文字を除去
    safe_title = "".join(c for c in title if c not in r'\/:*?"<>|').strip()[:60]
    if not safe_title:
        safe_title = "untitled"

    filepath = base_dir / f"{datetime_prefix}{safe_title}.md"
    filepath.write_text(content_md, encoding="utf-8")
    return str(filepath)


def save_json(records: list[dict], save_date: str, filename: str) -> str:
    """
    レコードを JSON ファイルに保存する。

    保存先: schedule/data/{save_date}/ai_context/{filename}.json

    Args:
        records:   辞書のリスト
        save_date: 保存日（YYYY-MM-DD 形式）
        filename:  ファイル名（拡張子なし）。例: "tasks"

    Returns:
        保存したファイルのパス文字列
    """
    base_dir = Path(__file__).parent / "data" / save_date / "ai_context"
    base_dir.mkdir(parents=True, exist_ok=True)

    filepath = base_dir / f"{filename}.json"
    filepath.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(filepath)


def save_csv(records: list[dict], save_date: str, filename: str) -> str:
    """
    レコードを CSV ファイルに保存する。

    保存先: schedule/data/{save_date}/{filename}.csv

    Args:
        records:   辞書のリスト（fetch_xxx.py の出力）
        save_date: 保存日（YYYY-MM-DD 形式）。フォルダ名になる
        filename:  ファイル名（拡張子なし）。例: "tasks"

    Returns:
        保存したファイルのパス文字列
    """
    if not records:
        return ""

    # schedule/data/{save_date}/ ディレクトリを作成
    base_dir = Path(__file__).parent / "data" / save_date
    base_dir.mkdir(parents=True, exist_ok=True)

    filepath = base_dir / f"{filename}.csv"

    # 辞書のキーをヘッダーとして使う（weekdays など dict 型は JSON 文字列に変換）
    fieldnames = list(records[0].keys())

    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            # 値が dict/list の場合は JSON 文字列に変換（例: weekdays）
            row = {
                k: json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else v
                for k, v in record.items()
            }
            writer.writerow(row)

    return str(filepath)
