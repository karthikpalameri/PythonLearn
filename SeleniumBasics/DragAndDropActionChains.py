import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DragAndDropActionClass():

    def test(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://jqueryui.com/droppable/")

        iframe = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)
        print("Switched to frame..")
        src_ele = driver.find_element(By.XPATH, "//div[@id='draggable']")
        dest_ele = driver.find_element(By.XPATH, "//div[@id='droppable']")
        try:
            action = ActionChains(driver)
            # Method 1(easy method)
            # action.drag_and_drop(src_ele, dest_ele).perform()

            # method -2 (chaining and performing)
            action.click_and_hold(src_ele).pause(3).move_to_element(dest_ele).release().perform()
            print("drag and drag executed..")
            time.sleep(5)
        except:
            print("Something went wrong in actionsclasss")

        time.sleep(10)
        driver.quit()


if __name__ == '__main__':
    DragAndDropActionClass().test()
