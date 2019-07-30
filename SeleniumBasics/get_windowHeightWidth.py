from selenium import webdriver
from selenium.webdriver.common.by import By


class GetWindowHeightWidth():

    def __init__(self, driver):
        self.driver = driver

    def tes(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        elem = driver.find_element(By.ID, "hondaradio")
        print("Got name attributr-->" + elem.get_attribute("name"))

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Got the window height and width from javascript-> height->{}, width->{}".format(height, width))


driver = None
if __name__ == '__main__':
    obj = GetWindowHeightWidth(driver)
    obj.tes()
