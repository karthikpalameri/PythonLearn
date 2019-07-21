from selenium import webdriver
from selenium.webdriver.common.by import By


class GetAttribute():
    def tes(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        elem = driver.find_element(By.ID, "hondaradio")
        print("Got name attributr-->" + elem.get_attribute("name"))


obj = GetAttribute()
obj.tes()
