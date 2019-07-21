import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from SeleniumBasics.HandyWrapper import HandyWrapper as HW


class DynamicXpath():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(baseUrl)
        """
        WEBDRIVER WAIT DEMO
        """
        WebDriverWait(driver, 10, poll_frequency=500,
                      ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                          ElementNotSelectableException]).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='apple']")))

        """
        DYNAMIC XPATH DEMO 
        """

        list = ["bmwcheck", "benzcheck", "hondacheck"]
        for val in list:
            print("*" * 60)
            _dynamicLocator = "//*[@id='{0}']"
            ele = HW(driver).getElement(_dynamicLocator.format(val), locatorType="xpath")
            print("Found {} and it is {} ITs is_selected()  state is->{}".format(ele.get_attribute("value"),
                                                                                 ele.get_attribute("type"),
                                                                                 ele.is_selected()))
            if ele.is_selected() is False:
                ele.click()
                print("Now After changing {} and it is {} ITs is_selected()  state is->{}".format(
                    ele.get_attribute("value"),
                    ele.get_attribute("type"),
                    ele.is_selected()))


DynamicXpath().test()
time.sleep(20)
