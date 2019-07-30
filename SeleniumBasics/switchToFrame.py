import time

from selenium import webdriver
from SeleniumBasics.HandyWrapper import HandyWrapper as HW
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select


class iframeSwitch():
    def __init__(self, driver):
        self.driver = driver


class createDriver():
    driverz = None

    def __init__(self, driverr):
        self.driverz = driverr
        self.driverz = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        self.driverz.maximize_window()
        self.driverz.implicitly_wait(10)

    def getDriver(self):
        return self.driverz


if __name__ == '__main__':
    driverx = None
    drivery = None

    driverx = createDriver(driverx).getDriver()
    driverx.get("https://learn.letskodeit.com/p/practice")
    hw = HW(driverx)
    time.sleep(2)

    select = Select(hw.getElement("//*[@id='carselect']", "xpath"))
    print("Switched to main window and performing select operation..")
    select.select_by_visible_text("Honda")

    iframe = driverx.find_element_by_xpath("//iframe[@id='courses-iframe']")

    print(iframe.location_once_scrolled_into_view)

    # switch to iframe using ID
    # driverx.switch_to.frame("courses-iframe")


    # switch to iframe using name
    # driverx.switch_to.frame("iframe-name")


    # switch to iframe using Index
    driverx.switch_to.frame(0)

time.sleep(2)
driverx.find_element_by_xpath("//input[@id='search-courses']").send_keys("python")

driverx.switch_to.default_content()

selectEle = driverx.find_element_by_xpath("//*[@id='carselect']")

driverx.execute_script("arguments[0].scrollIntoView(true);", selectEle)

time.sleep(20)
driverx.quit()
