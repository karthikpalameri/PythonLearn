import time

from selenium import webdriver
from selenium.webdriver import ActionChains


class ActionsChainsDemo():
    driverx = None

    def __init__(self):
        self.driverx = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    def testActionsChains(self):
        self.driverx.maximize_window()
        self.driverx.implicitly_wait(10)
        self.driverx.get("https://learn.letskodeit.com/p/practice")
        self.driverx.execute_script("window.scrollBy(0,600);")
        drivery = self.driverx
        mouseHoverMenu = drivery.find_element_by_id("mousehover")
        action = ActionChains(drivery)
        action.move_to_element(mouseHoverMenu).perform()
        time.sleep(2)

        
        action.move_to_element(drivery.find_element_by_link_text("Top")).click().perform()
        time.sleep(2)

        drivery.quit()


if __name__ == '__main__':
    ActionsChainsDemo().testActionsChains()
