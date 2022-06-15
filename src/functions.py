from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

__month_dict = {
            'فروردین': '1', 'اردیبهشت': '2', 'خرداد': '3',
            'تیر': '4', 'اَمرداد': '5', 'شهریور': '6',
            'مهر': '7', 'آبان': '8', 'آذر': '9', 
            'دی': '10', 'بهمن': '11', 'اسفند': '12'
        }

def __setup_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_holidays(from_year: int, to_year: int):
    driver = __setup_driver()
    driver.get('https://www.time.ir/fa/eventyear-%D8%AA%D9%82%D9%88%DB%8C%D9%85-%D8%B3%D8%A7%D9%84%DB%8C%D8%A7%D9%86%D9%87')
    
    global __month_dict

    holidays_dict = {}
    for year in range(from_year, to_year+1):
        input_field = driver.find_element(by=By.ID, value="ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_txtYear")
        input_field.clear()
        input_field.send_keys(year)
        driver.find_element(by=By.ID, value="ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_btnGo").click()

        holiday_events = driver.find_elements(by=By.CLASS_NAME, value="eventHoliday ")

        holidays_dict[str(year)] = {}
        for holiday in holiday_events:
            day, month_title, _ = str(holiday.text).split(maxsplit=2)
            if __month_dict[month_title] not in holidays_dict[str(year)]:
                holidays_dict[str(year)][__month_dict[month_title]] = []
            
            holidays_dict[str(year)][__month_dict[month_title]].append(str(int(day)))

    driver.close()
    return holidays_dict

def get_events(from_year: int, to_year: int):
    driver = __setup_driver()
    driver.get('https://www.time.ir/fa/eventyear-%D8%AA%D9%82%D9%88%DB%8C%D9%85-%D8%B3%D8%A7%D9%84%DB%8C%D8%A7%D9%86%D9%87')

    global __month_dict

    events_dict = {}
    for year in range(from_year, to_year+1):
        input_field = driver.find_element(by=By.ID, value="ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_txtYear")
        input_field.clear()
        input_field.send_keys(year)
        driver.find_element(by=By.ID, value="ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_btnGo").click()
        calender = driver.find_elements(by=By.TAG_NAME, value="li")[:-6]

        events_dict[str(year)] = {}
        
        for event in calender:
            day, month_str, event_title = str(event.text).split(maxsplit=2)

            is_holiday = event.get_attribute("class") == "eventHoliday "
            
            if __month_dict[month_str] not in events_dict[str(year)]:
                events_dict[str(year)][__month_dict[month_str]] = {}

            if str(int(day)) in events_dict[str(year)][__month_dict[month_str]]:
                events_dict[str(year)][__month_dict[month_str]][str(int(day))]["events"].append(str(event_title))
                if is_holiday:
                    events_dict[str(year)][__month_dict[month_str]][str(int(day))]["holiday"] = True
            else:         
                event_dict = {
                    str(int(day)): {
                            "events": [str(event_title)],
                            "holiday": is_holiday
                        }
                    }

                events_dict[str(year)][__month_dict[month_str]].update(event_dict)
    driver.close()
    return events_dict
