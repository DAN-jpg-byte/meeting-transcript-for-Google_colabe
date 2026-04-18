#!/usr/bin/env python3
"""
インテグレーションに接続されている Notion DB の一覧と ID を表示するスクリプト。
"""

import json
import os
import sys
import urllib.request

NOTION_API_VERSION = "2022-06-28"


def notion_request(path: str, token: str, method: str = "GET", body: dict = None) -> dict:
    url = f"https://api.notion.com/v1/{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_API_VERSION,
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))


def main():
    token = (os.environ.get("NOTION_API_TOKEN") or os.environ.get("NOTION_TOKEN") or "").strip()
    if not token:
        print("エラー: NOTION_TOKEN が設定されていません", file=sys.stderr)
        sys.exit(1)

    # インテグレーションに接続されている全 DB を検索
    response = notion_request(
        path="search",
        token=token,
        method="POST",
        body={"filter": {"value": "database", "property": "object"}, "page_size": 100},
    )

    print("=== 接続済み Notion データベース一覧 ===\n")
    for db in response.get("results", []):
        # DB名（タイトル）
        title_list = db.get("title", [])
        name = title_list[0].get("plain_text", "（無題）") if title_list else "（無題）"
        db_id = db.get("id")
        print(f"DB名: {name}")
        print(f"  ID: {db_id}")
        print()


if __name__ == "__main__":
    main()
