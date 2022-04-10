import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def __setup_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_holidays(from_year: int, to_year: int):
    driver = __setup_driver()
    driver.get('https://www.time.ir/fa/eventyear-%D8%AA%D9%82%D9%88%DB%8C%D9%85-%D8%B3%D8%A7%D9%84%DB%8C%D8%A7%D9%86%D9%87')

    holidays_dict = {}
    for year in range(from_year, to_year+1):
        input_field = driver.find_element(by=By.ID, value="ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_txtYear")
        input_field.clear()
        input_field.send_keys(year)
        driver.find_element(by=By.ID, value="ctl00_cphTop_Sampa_Web_View_EventUI_EventYearCalendar10cphTop_3417_btnGo").click()

        calender = driver.find_elements_by_class_name("dayList")
        holidays_dict[year] = {}
        for month_number in range(len(calender)):
            holidays_dict[year][month_number+1] = []
            div_tags = calender[month_number].find_elements(by=By.TAG_NAME, value='div')
            for div in div_tags:
                div_class = div.get_attribute('class') 
                div_parent_class = div.find_element(by=By.XPATH, value='..').get_attribute('class')
                if div_class == ' holiday' and div_parent_class != 'spacer disabled':
                    day = int(div.text.split('\n')[0])
                    holidays_dict[year][month_number+1].append(day)

    return holidays_dict