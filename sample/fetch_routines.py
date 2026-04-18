#!/usr/bin/env python3
"""
今週のルーティンDB から有効なルーティン一覧を取得するスクリプト。

ルーティンは日付で絞るのではなく「終了していないもの全件」を取得する。

使い方:
    python fetch_routines.py

出力:
    JSON 形式でルーティン一覧を標準出力に表示
"""

import json
import sys

from utils import get_token, notion_post, save_csv, save_json

# 今週のルーティンDB の database_id
ROUTINE_DB_ID = "2ef6f8be-0227-80b8-8ad4-d11b112043f5"

# 取得する曜日チェックのプロパティ名
WEEKDAY_PROPS = ["月", "火", "水", "木", "金", "土", "日"]


def fetch_routines() -> list[dict]:
    """
    終了していないルーティンを全件取得する。

    Returns:
        ルーティンの辞書リスト
    """
    token = get_token()

    url = f"https://api.notion.com/v1/databases/{ROUTINE_DB_ID}/query"
    routines = []
    cursor = None

    while True:
        # 終了=false のもの（有効なルーティン）だけ取得
        body: dict = {
            "filter": {
                "property": "終了",
                "checkbox": {"equals": False},
            },
            "page_size": 100,
        }
        if cursor:
            body["start_cursor"] = cursor

        response = notion_post(url, token, body)

        for page in response.get("results", []):
            routines.append(extract_routine(page))

        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return routines


def extract_routine(page: dict) -> dict:
    props = page.get("properties", {})

    # ルーティン名（タイトル）
    name = ""
    title_list = props.get("ハードル低めの1分ルーテイン", {}).get("title", [])
    if title_list:
        name = title_list[0].get("plain_text", "")

    # 頻度
    frequency = None
    select = props.get("頻度", {}).get("select")
    if select:
        frequency = select.get("name")

    # 各曜日のチェック状態
    weekdays = {}
    for day in WEEKDAY_PROPS:
        prop = props.get(day, {})
        if prop.get("type") == "checkbox":
            weekdays[day] = prop.get("checkbox", False)

    # 終了フラグ
    done = props.get("終了", {}).get("checkbox", False)

    return {
        "id": page.get("id"),
        "name": name,
        "frequency": frequency,
        "weekdays": weekdays,
        "done": done,
    }


def main():
    # 引数: [保存日]（省略可）
    save_date = sys.argv[1] if len(sys.argv) == 2 else None

    routines = fetch_routines()

    if save_date:
        path = save_csv(routines, save_date, "routines")
        json_path = save_json(routines, save_date, "routines")
        print(f"[routines] {len(routines)}件 → {path}", file=sys.stderr)
        print(f"[routines] JSON  → {json_path}", file=sys.stderr)

    print(json.dumps(routines, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
