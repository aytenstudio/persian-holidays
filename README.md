# persian-holidays

This is basically a Crawler in order to extract Persian holidays and events from [time.ir](https://www.time.ir/fa/eventyear-%D8%AA%D9%82%D9%88%DB%8C%D9%85-%D8%B3%D8%A7%D9%84%DB%8C%D8%A7%D9%86%D9%87)

## Sample Output
Checkout [output](https://github.com/aytenstudio/persian-holidays/tree/main/output) folder to see sample results.


## Usage



by importing the "extract" file you can call "holidays_as_json" & "events_as_json" by giving starting and ending year as input to these functions. The output will be a JSON file, stored in the output directory in root. The desired output can be found within the path given in the console after calling these functions.



Moreover, there are more basic functions you can use by importing the "functions" file. These are the exact functions that are used inside of extract functions. For instance "get_holidays" return the desired holidays in Python-Dictionary format, as well as "get_events".



to make it easy, I provided an inline script by running the "main.py" file along with arguments. the output will be saved inside the output directory. By using this script there's no need to import "extract" and call "holidays_as_json".



in order to extract holidays and events as JSON files, run the script as the instruction below:

        

            python ./src/main.py --From <from-year> --To <to-year>





The output will be holidays and events in the given range.





## CI/CD

This project is provided with Github-actions. it automatically runs the script and generates output files.

you can change environment variables in the "actions.yml" file. By default, $FROM_YEAR is equal to 1400 and $TO_YEAR is 1401.
