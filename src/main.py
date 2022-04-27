from crawl_holidays import get_holidays
import json


if __name__ == "__main__":
    with open('output/holidays.json', 'w') as output_file:
        json.dump(get_holidays(from_year=1391, to_year=1411), output_file)