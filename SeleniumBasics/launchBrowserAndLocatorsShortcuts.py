import os

from selenium import webdriver
from selenium.webdriver.common.by import By


class GlobalVariables():
    driver = None


class Browserinitialize():
    def inititalizeBrowser(self, browser):
        if (browser is "firefox"):
            self.driver = webdriver.Firefox(executable_path="/Users/karthikp/Desktop/drivers/geckodriver")
            return self.driver

        elif (browser is "chrome"):
            self.driver = webdriver.Chrome(executable_path="/Users/karthikp/Desktop/drivers/chromedriver")
            GlobalVariables.driver = self.driver
            return GlobalVariables.driver

        elif (browser is "safari"):
            serverLocation = "/Users/karthikp/Desktop/drivers/selenium-server-standalone-3.141.59.jar"
            os.environ["SELENIUM_SERVER_JAR"] = serverLocation
            self.driver = webdriver.Safari()

            return self.driver
        else:
            raise Exception("Browser not initialized please check ")


class BrowserInteractions():
    def maximizeBrowser(self):
        GlobalVariables.driver.maximize_window()


def myMain():
    urlToLaunch = "https://learn.letskodeit.com/p/practice"
    driver = Browserinitialize().inititalizeBrowser(browser="chrome")
    BrowserInteractions().maximizeBrowser()
    driver.get(urlToLaunch)
    driver.maximize_window()
    print("Title of the webpage is :" + driver.title)
    print("Url of current page is :" + driver.current_url)
    print("Browser refresh 1 st time :")
    driver.refresh()
    print("Browsear refresg 2nd time :")
    driver.get(driver.current_url)
    print("navigate to new page :")
    driver.get("http://ask.com")
    driver.back()
    driver.forward()
    driver.back()

    myElementById = driver.find_element_by_id("radio-btn-example")
    myElementByCss = driver.find_element_by_css_selector("div[id*='block']")  # matches any text containingg block
    if myElementById is not None and myElementByCss is not None:
        print("We found element by id and by css Great!")

    ##USING CSS WITH ID SHORTCUTS

    myElementByCssShortcutsForId1 = driver.find_elements(By.CSS_SELECTOR, "#openwindow")
    leng1 = len(myElementByCssShortcutsForId1)
    if myElementByCssShortcutsForId1 is not None:
        print("We Found {} css selectors  for #openwindow id using css shortcut ".format(leng1))

    myElementByCssShortcutsForId2 = driver.find_elements_by_css_selector("#carselect")
    leng2 = len(myElementByCssShortcutsForId2)
    if myElementByCssShortcutsForId2 is not None:
        print("We Found {} css id selectors  for #carselect id using css shortcut #<carselect>".format(leng2))

    myElementByCssShortcutsForId3 = driver.find_elements_by_css_selector("select#carselect")
    leng3 = len(myElementByCssShortcutsForId3)
    if myElementByCssShortcutsForId3 is not None:
        print(
            "We found {} css id selectors for selct#carselect id using css shortcut <tagname>#<idname> ".format(
                leng3))

    myElementByCssShortcutsForId4 = driver.find_elements_by_css_selector("select[id='carselect']")
    leng4 = len(myElementByCssShortcutsForId4)
    if leng4 != 0:
        print("We found %s css id selectors for <tag-name>[<attribute>='<value>']" % leng4)

    ##USING CSS WITH CLASSNAME SHORTCUTS
    # APPENDING CLASS NAMES TO FIND THE UNIQUE ELEMENT
    # .class1.class2.class3 -> Until we find a unique element
    # a[class='btn-style'] -> will match exactly so most of the times it will fail
    myElementByCssShortcutsForClass1 = driver.find_elements(By.CSS_SELECTOR, ".btn-style.class2.class1")
    leng5 = len(myElementByCssShortcutsForClass1)
    if leng5 is not None:
        print("We found %s css class selectors for .<class-name1>.<class-name2>" % leng5)

    """
    USING WILD CARDS IN CSS SELECTORS 
    Syntax: 
    <tag>[<attribute><special-character>='<value>]

    input[class^='inputs'] -> Matches starting atrribute value
    input[class$='inputs'] -> Matches ending attribute value
    input[class*='inputs'] -> Matches attribute  containging value g
    """

    """
    FINDING CHILD NODES USING CSS
    Syntax:
     <tag-name>><tag-name>
    Exapme:
    div>input

    CAN ALSO ADD # AND . 
    div>fieldset>
    div>fieldset>label[for="bmw"]
    div>fieldset>label>input[id='bmwradio']

s
    """

    """
    XPATH CONTAINS CAN BE CLUBBED WITH AND TO FIND THE UNIQUE ELEMENT 

    CONTAINS
    //a[contains(@class,'someclass') and contains(text(),'someText')]

    STARTS-WITH
    //a[starts-with(@class,'someclassname') or contsins(text(),'something')]

    PARENT::<tag-name>  PRECEDING-SIBLING::<tag-name>  FOLLOWING-SIBLING::<tag-name>  
    //select[@id='multiple-select-example']//option[text()='Apple']/following-sibling::option[1]/preceding-sibling::option/parent::select

    """
    driver.quit()

if __name__ == '__main__':
    print("__name__ -> "+__name__)
    myMain()