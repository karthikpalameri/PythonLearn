import time

from selenium import webdriver
from SeleniumBasics.HandyWrapper import HandyWrapper as HW
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import Select


class windowSwitch():
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
    elem = hw.getElement("//*[@id='openwindow']", "xpath")
    elem.click()
    time.sleep(2)

    main_window = driverx.current_window_handle
    print("Main window handle ->{}".format(main_window))
    handles = driverx.window_handles

    print("Got all window handles ->{}".format(handles))
    for handle in handles:

        if handle not in main_window:
            child_window = handle
            break
    driverx.switch_to.window(child_window)
    print("Switched to child window->{}".format(child_window))
    driverx.maximize_window()
    el = hw.getElement("//input[@id='search-courses']", "xpath")
    el.send_keys("python")
    driverx.close()
    driverx.switch_to.window(main_window)
    select = Select(hw.getElement("//*[@id='carselect']", "xpath"))
    print("Switched to main window and performing select operation..")
    select.select_by_visible_text("Honda")
