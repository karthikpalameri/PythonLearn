import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class CheckSelcted():
    def performSomeSelectionAndCheck(self):
        location = "/Users/karthikp/Desktop/drivers/geckodriver"
        # os.environ["webdriver.gecko.driver"] = location
        driver = webdriver.Firefox(executable_path=location)
        driver.maximize_window()
        driver.implicitly_wait(7)
        driver.get("https://learn.letskodeit.com/p/practice")
        bmwRadioButton = driver.find_element_by_xpath("//input[@type='radio' and @value='bmw']")
        bmwRadioButton.click()
        benzRadioButton = driver.find_element_by_xpath("//input[@type='radio' and @value='benz']")
        benzRadioButton.click()

        bmwCheckBox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckBox.click()

        benzCheckBox = driver.find_element(By.ID, "benzcheck")
        benzCheckBox.click()

        print("bmwRadioButton->" + str(bmwRadioButton.is_selected()))
        print("benzRadioButton->" + str(benzRadioButton.is_selected()))

        print("bmwCheckBox->" + str(bmwCheckBox.is_selected()))
        print("benzCheckBox->" + str(benzCheckBox.is_selected()))

        radioButtonList = driver.find_elements(By.XPATH, "//input[@type='radio']")
        for ele in radioButtonList:
            if not ele.is_selected():
                time.sleep(3)
                ele.click();


if __name__ == '__main__':
    CheckSelcted().performSomeSelectionAndCheck()
