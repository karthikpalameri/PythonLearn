from selenium import webdriver

from SeleniumBasics.HandyWrapper import HandyWrapper


class UsingWrapperClass:
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get(baseUrl)
        hw = HandyWrapper(driver)
        ele = hw.getElement("benzradio")
        ele.click()

        ele2 = hw.getElement("//input[@id='bmwcheck']", locatorType="xpath")
        ele2.click()

        inputbox = hw.isElementPresent("//*[@id=\"name\"]", hw.getByType("xpath"))
        if inputbox is True:
            print("inputbox element found")

        alertButton = hw.getElement("//*[@id=\"alertbtn\"]", locatorType="xpath")

        print(
            "ALert button is present".format(hw.isElementPreseneceCheck("//*[@id='alertbtn']", hw.getByType("xpath"))))


o = UsingWrapperClass()
o.test()
