from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class isEnabledDemo():
    def checkIsEnabled(self):
        location = "/Users/karthikp/Desktop/drivers/chromedriver"
        os.environ["webdriver.chrome.driver"] = location
        driver = webdriver.Chrome(location)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        ele1 = driver.find_element(By.XPATH, "//input[contains(@class,'gsfi')]")
        isEnabledOrNot = ele1.is_enabled()
        print("isEnabledOrNot->{}".format(isEnabledOrNot))


if __name__ == '__main__':
    print("__name__ -> " + __name__)
    isEnabledDemo().checkIsEnabled()
