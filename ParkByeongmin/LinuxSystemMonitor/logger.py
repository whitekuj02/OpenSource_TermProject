import csv
from pathlib import Path
from datetime import datetime


LOG_FILE = Path(__file__).resolve().parent / "system_log.csv"


def save_log(cpu, memory, disk, alerts):

    new_file = not LOG_FILE.exists() or LOG_FILE.stat().st_size == 0

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if new_file:
            writer.writerow([
                "Timestamp",
                "CPU",
                "RAM",
                "DISK",
                "Alerts"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            cpu,
            memory,
            disk,
            " | ".join(alerts) if alerts else "Normal"
        ])