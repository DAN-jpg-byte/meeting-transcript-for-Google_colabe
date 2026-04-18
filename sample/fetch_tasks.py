#!/usr/bin/env python3
"""
Notion タスクDB から「いつやるか？」で絞り込んでタスクを取得するスクリプト。

使い方:
    python fetch_tasks.py <開始日> <終了日>
    例: python fetch_tasks.py 2026-04-02 2026-05-12

出力:
    JSON 形式でタスク一覧を標準出力に表示
"""

import json
import sys

from utils import get_token, notion_post, save_csv, save_json

# タスクDB の database_id（固定）
TASK_DB_ID = "25a6f8be-0227-8194-9356-d06cb96c0812"


def fetch_tasks(start_date: str, end_date: str) -> list[dict]:
    """
    タスクDB から「いつやるか？」が指定範囲内のタスクを取得する。

    Args:
        start_date: 開始日（YYYY-MM-DD 形式）
        end_date:   終了日（YYYY-MM-DD 形式）

    Returns:
        タスクの辞書リスト
    """
    token = get_token()

    url = f"https://api.notion.com/v1/databases/{TASK_DB_ID}/query"
    tasks = []
    cursor = None

    while True:
        # フィルター: いつやるか？ が start_date 〜 end_date の範囲
        body: dict = {
            "filter": {
                "and": [
                    {
                        "property": "いつやるか？",
                        "date": {"on_or_after": start_date},
                    },
                    {
                        "property": "いつやるか？",
                        "date": {"on_or_before": end_date},
                    },
                ]
            },
            "page_size": 100,
        }
        if cursor:
            body["start_cursor"] = cursor

        response = notion_post(url, token, body)

        for page in response.get("results", []):
            task = extract_task(page)
            tasks.append(task)

        # 次のページがなければ終了
        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return tasks


def extract_task(page: dict) -> dict:
    """
    Notion のページオブジェクトから必要な情報だけ抽出する。

    Args:
        page: Notion API のページオブジェクト

    Returns:
        整形済みタスク辞書
    """
    props = page.get("properties", {})

    # タスク名（タイトル）
    name = ""
    name_prop = props.get("名前", {})
    title_list = name_prop.get("title", [])
    if title_list:
        name = title_list[0].get("plain_text", "")

    # 完了フラグ
    done = False
    done_prop = props.get("完了", {})
    if done_prop.get("type") == "checkbox":
        done = done_prop.get("checkbox", False)

    # いつやるか？（日付）
    scheduled_date = None
    date_prop = props.get("いつやるか？", {})
    if date_prop.get("type") == "date" and date_prop.get("date"):
        scheduled_date = date_prop["date"].get("start")

    # 重要度マトリクス（select）
    importance = None
    importance_prop = props.get("重要度マトリクス", {})
    if importance_prop.get("type") == "select" and importance_prop.get("select"):
        importance = importance_prop["select"].get("name")

    # 進行中フラグ
    in_progress = False
    in_progress_prop = props.get("進行中", {})
    if in_progress_prop.get("type") == "checkbox":
        in_progress = in_progress_prop.get("checkbox", False)

    return {
        "id": page.get("id"),
        "name": name,
        "done": done,
        "scheduled_date": scheduled_date,
        "importance": importance,
        "in_progress": in_progress,
        "last_edited_time": page.get("last_edited_time"),
        "url": page.get("url"),
    }


def main():
    # 引数: <開始日> <終了日> [保存日]
    # 保存日を指定すると schedule/data/{保存日}/tasks.csv にも保存される
    if len(sys.argv) not in (3, 4):
        print("使い方: python fetch_tasks.py <開始日> <終了日> [保存日]", file=sys.stderr)
        print("例:     python fetch_tasks.py 2026-04-02 2026-05-12 2026-04-12", file=sys.stderr)
        sys.exit(1)

    start_date = sys.argv[1]
    end_date = sys.argv[2]
    save_date = sys.argv[3] if len(sys.argv) == 4 else None

    tasks = fetch_tasks(start_date, end_date)

    if save_date:
        path = save_csv(tasks, save_date, "tasks")
        json_path = save_json(tasks, save_date, "tasks")
        print(f"[tasks] {len(tasks)}件 → {path}", file=sys.stderr)
        print(f"[tasks] JSON  → {json_path}", file=sys.stderr)

    print(json.dumps(tasks, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
