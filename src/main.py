from extract import events_as_json, holidays_as_json
from functions import get_events, get_holidays
import json


if __name__ == "__main__":
    # extract holidays and events as a json file
    holidays_as_json(1400, 1401)
    events_as_json(1400, 1401)

    # get holidays and events as python dictionary
    holidays = get_holidays(1400, 1401)
    events = get_events(1400, 1401)
