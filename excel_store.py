import pandas as pd
from datetime import datetime
import hashlib
import os

EXCEL_FILE = "events.xlsx"
SHEET_NAME = "Events"

def generate_event_id(name, date, venue):
    unique_string = f"{name}-{date}-{venue}"
    return hashlib.md5(unique_string.encode()).hexdigest()

def update_excel(events):
    # Load or create Excel file
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
    else:
        df = pd.DataFrame(columns=[
            "event_id", "event_name", "event_date", "venue",
            "city", "category", "link", "status",
            "last_updated", "source"
        ])

    existing_ids = set(df["event_id"].astype(str))

    rows = []

    for event in events:
        event_id = generate_event_id(
            event["name"], event["date"], event["venue"]
        )

        row = {
            "event_id": event_id,
            "event_name": event["name"],
            "event_date": event["date"],
            "venue": event["venue"],
            "city": event["city"],
            "category": event["category"],
            "link": event["link"],
            "status": "Upcoming",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source": event.get("source", "Unknown")
        }

        if event_id in existing_ids:
            # Update existing row
            df.loc[df["event_id"] == event_id, :] = row
        else:
            rows.append(row)

    if rows:
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)

    # Save back to Excel
    df.to_excel(EXCEL_FILE, sheet_name=SHEET_NAME, index=False)
