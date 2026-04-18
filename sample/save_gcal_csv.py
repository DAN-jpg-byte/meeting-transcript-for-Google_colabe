#!/usr/bin/env python3
"""
gcal_events.json を読み込んで gcal_events.csv に変換するスクリプト。

使い方:
    python save_gcal_csv.py <保存日>
    例: python save_gcal_csv.py 2026-04-12
"""

import json
import sys
from pathlib import Path

from utils import save_csv


def main():
    if len(sys.argv) != 2:
        print("使い方: python save_gcal_csv.py <保存日>", file=sys.stderr)
        print("例:     python save_gcal_csv.py 2026-04-12", file=sys.stderr)
        sys.exit(1)

    save_date = sys.argv[1]

    # gcal_events.json を読み込む
    json_path = Path(__file__).parent / "data" / save_date / "ai_context" / "gcal_events.json"
    if not json_path.exists():
        print(f"ファイルが見つかりません: {json_path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(json_path.read_text(encoding="utf-8"))

    # カレンダーをまたいでフラットなレコードリストに変換
    records = []
    for cal in data.get("calendars", []):
        calendar_id = cal.get("calendar_id", "")
        calendar_name = cal.get("calendar_name", "")
        for event in cal.get("events", []):
            records.append({
                "calendar_id": calendar_id,
                "calendar_name": calendar_name,
                "id": event.get("id", ""),
                "title": event.get("title", ""),
                "start": event.get("start", ""),
                "end": event.get("end", ""),
                "all_day": event.get("all_day", ""),
                "location": event.get("location", ""),
                "description": event.get("description", ""),
            })

    path = save_csv(records, save_date, "gcal_events")
    print(f"[gcal] {len(records)}件 → {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
