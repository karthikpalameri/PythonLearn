from selenium.webdriver.common.by import By


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
            print("Element Found")

        except:
            print("Element Not Found")

        return element

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
