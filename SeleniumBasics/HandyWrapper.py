import datetime
import os
import traceback
from time import gmtime, strftime, localtime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


# driver.findElementById('dfaf',locatorType)
class HandyWrapper():
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "cssselector":
            return By.CSS_SELECTOR
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Locator type is not supported")
            return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found. Returning element..")
            return element


        except:
            print("Element Not Found!!!")

    def isElementPresent(self, locator, byType):
        element = None
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element Not found")
                return False
        except:
            print("Element Not Found")
            return False

    def isElementPreseneceCheck(self, locator, byTypee):
        ele = None
        try:
            elements = self.driver.find_elements(byTypee, locator)

            if len(elements) > 0:
                print("Element Found")
                return True

            else:
                print("Element Not Found")
                return False

        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType=id, timeout=10, poll_frequency=0.5):
        element = None
        byType = self.getByType(locatorType)
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency)
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

        except:
            print("Element not appeared in the webpage and is not clickable")
            traceback.print_stack()

    def saveScreenShot(self):
        """
        takes screenshot and puts in a directory
        :return:
        """
        file_location = os.getcwd() + "/Screenshots/" + strftime("%d-%m-%y_%H:%M:%S", localtime()) + ".png"
        try:
            self.driver.save_screenshot(file_location)
            print("Screenshot taken in ->{}".format(file_location))
        except:
            print("Unable to take screenshot")
