from ast import arg
from extract import events_as_json, holidays_as_json
from functions import get_events, get_holidays


if __name__ == "__main__":
    """
        in order to extract holidays and events as json file,
        run the script as the instruction below:
        
            python ./src/main.py --From <from_year> --To <to_year>

    """

    # configure arguments
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--From", type=int, default=1401)
    parser.add_argument("-t", "--To", type=int, default=1401)

    args = parser.parse_args()

    # extract holidays and events as a json file
    holidays_as_json(args.From, args.To)
    events_as_json(args.From, args.To)

    # you can also get holidays and events as python dictionary by running these functions:
    # holidays = get_holidays(1400, 1401)
    # events = get_events(1400, 1401)
