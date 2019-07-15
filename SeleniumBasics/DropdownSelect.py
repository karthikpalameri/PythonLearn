import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DropdownSelect():
    def selectOperation(self):
        location = "/Users/karthikp/Desktop/drivers/geckodriver"
        driver = webdriver.Firefox(executable_path=location)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://learn.letskodeit.com/p/practice")
        ele = driver.find_element_by_id("carselect")
        s = Select(ele)

        s.select_by_visible_text("Honda")
        time.sleep(2)
        s.select_by_value("benz")
        time.sleep(2)
        s.select_by_index(0)
        time.sleep(2)



if __name__ == '__main__':
    DropdownSelect().selectOperation()
