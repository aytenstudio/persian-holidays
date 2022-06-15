from functions import get_events, get_holidays
import json
import os


def holidays_as_json(from_year: int, to_year: int) -> None:
    os.makedirs("./output", exist_ok=True)
    file_path = f"output/holidays<{from_year}-{to_year}>.json"

    if not os.path.exists(file_path):
        with open(file_path, "w") as output_file:
            json.dump(get_holidays(from_year=from_year, to_year=to_year), output_file, indent=4)

    print(f"result has been saved in {file_path}")

def events_as_json(from_year: int, to_year: int) -> None:
    os.makedirs("./output", exist_ok=True)
    file_path = f"output/events<{from_year}-{to_year}>.json"

    if not os.path.exists(file_path):
        with open(file_path, "w") as output_file:
            json.dump(get_events(from_year=from_year, to_year=to_year), output_file, indent=4, ensure_ascii=False)

    print(f"result has been saved in {file_path}")
