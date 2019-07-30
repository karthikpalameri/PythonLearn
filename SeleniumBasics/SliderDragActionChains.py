import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import logging

class SliderDragActionClass():

    def test(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get("https://jqueryui.com/slider/")

        iframe = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        print("Switched to frame..")

        src_ele = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
        try:
            action = ActionChains(driver)
            # Method 1(easy method)
            action.drag_and_drop_by_offset(src_ele, 100, 0).perform()
            time.sleep(5)
        except:
            print("Something went wrong in actionsclasss")

        time.sleep(10)
        driver.quit()


if __name__ == '__main__':
    SliderDragActionClass().test()
