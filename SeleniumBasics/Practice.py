import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium


class someClassA():
    def practice(self):
        location = "/Users/karthikp/Desktop/drivers/chromedriver"
        driver = webdriver.Chrome(executable_path=location)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.airbnb.com/")
        driver.find_element_by_id("Koan-magic-carpet-koan-search-bar__input").send_keys("goa" + Keys.TAB + Keys.TAB)
        # driver.find_element_by_id("Koan-magic-carpet-koan-search-bar__input").send_keys(Keys.TAB)
        # print(driver.find_element_by_css_selector("._gucugi>strong").text)
        # driver.find_element_by_css_selector("div > input[id = 'checkin_input']").send_keys("01/01/2019")
        # driver.find_element_by_css_selector("div>input[id='checkout_input']").send_keys("01/01/2019")
        month = driver.find_element_by_xpath("//div[@class='_1foj6yps']//div[@data-visible='true']//strong")
        gotThisMonth=month.text
        print(gotThisMonth)

        forwardArrow = driver.find_element_by_xpath("//div[@aria-label='Move forward to switch to the next month.']")
        forwardArrow.click()

        selectMonth = "September 2022"

        while selectMonth != gotThisMonth:
            forwardArrow.click()
            time.sleep(5)
            month = driver.find_element_by_xpath("//div[@class='_1foj6yps']//div[@data-visible='true']//strong")
            gotThisMonth = month.text
            print(gotThisMonth)

        time.sleep(15)


if __name__ == '__main__':
    someClassA().practice()
