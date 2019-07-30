import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from SeleniumBasics.HandyWrapper import HandyWrapper


class scrollIntoView():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrapper(self.driver)

    def tes(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        # # Scroll down 1000px
        # driver.execute_script("window.scrollBy(0,1000)")
        #
        # time.sleep(3)
        # # Scroll up 1000px
        # driver.execute_script("window.scrollBy(0,-1000)")
        # time.sleep(3)

        # elem = self.hw.getElement("//*[@id='mousehover']", "xpath")
        elem = driver.find_element_by_xpath("//*[@id='mousehover']")
        # ScrollIntoView until the element is visible
        driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        time.sleep(3)

        # Scroll up 1000px
        driver.execute_script("window.scrollBy(0,-1000)")

        # using native scroll
        location = elem.location_once_scrolled_into_view

        print("Got name elem loaction-->{}".format(location))

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Got the window height and width from javascript-> height->{}, width->{}".format(height, width))


driver = None
if __name__ == '__main__':
    obj = scrollIntoView(driver)
    obj.tes()
