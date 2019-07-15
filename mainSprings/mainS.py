import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys, traceback

driver = None;
username = "555127"
pwd = "Jun@2019"
sprintNum = "SPR18"


class mainS():

    def initializeBrowser(self):
        location = "/Users/karthikp/Desktop/drivers/chromedriver"
        driver = webdriver.Chrome(executable_path=location)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def explicitWait(self, ele):
        wait = WebDriverWait(driver, 15)
        print("Waiting for element ")
        return wait.until(EC.visibility_of_element_located, ele)

    def mouseOver(self, ele):
        ActionChains(driver).move_to_element(ele).perform

    def mouseOverAndClick(self, ele):
        mainS.explicitWait(self, ele=ele)
        ActionChains(driver).move_to_element(ele).click().perform()

    def loginWithCredentials(self, username, pwd):
        driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
        driver.find_element_by_xpath("//input[@id='PasswordInternal']").send_keys(pwd)
        driver.find_element_by_xpath("//input[@id='Log_On1']").click()
        print("Clicked on login")
        mainSprigLogo = mainS().explicitWait(driver.find_element_by_xpath("//*[@id='navbar']/div[3]/a"))

    def clickOnLeftNavBarFor(self, choice):
        main_spring_logo = driver.find_element_by_xpath("//*[@id='navbar']/div[3]/a")
        print("LeftNav element present!!")

        print(main_spring_logo.location)

        print("Main Spring element location:{}".format(main_spring_logo.location))
        print("Main Spring element size:{}".format(main_spring_logo.size))
        x = main_spring_logo.location["x"]
        y = main_spring_logo.location["y"]
        print(x, y)
        ActionChains(driver).move_to_element_with_offset(main_spring_logo, x - 230, y).click().send_keys(
            Keys.ESCAPE).perform()
        # ActionChains(driver).move_to_element_with_offset(mainSprigLogo, -95, 10).click().perform()
        print("Mouse hover performed")
        print("Dismissing rightclick by esc..")
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        if choice is "comcast":
            print("Clicking on comcast as it is passed!!!")
            comcast_bsd = driver.find_element_by_xpath("(//*[@id='projectIcon']//a)[2]")

            try:
                mainS().mouseOverAndClick(ele=comcast_bsd)
            except:
                print("Mouse Over failing -> {} , taking care by java script!!!".format(choice))
                driver.execute_script("document.querySelector('#projectIcon > ul > li:nth-child(1) > a').click()")

            mainS().explicitWait(main_spring_logo)
            time.sleep(5)
        elif choice is "workspace":
            print("Clicking on workspace as it is passed!!!")
            workspaceParent = driver.find_element_by_xpath("//*[@id='workspaceIcon']/span").click()
            workspaceChild = driver.find_element_by_xpath("//*[@id='MX_LOCK_Home']/a").click()
            try:
                mainS().mouseOverAndClick(ele=workspaceParent)
            except:
                print("Mouse Over failing -> {} , taking care by java script!!!".format(choice))
                driver.execute_script("document.querySelector('#workspaceIcon > span').click()")
            try:
                mainS().mouseOverAndClick(ele=workspaceChild)
            except:
                print("Mouse Over failing -> {} , taking care by java script!!!".format(choice))
                driver.execute_script("document.querySelector('#MX_LOCK_Home > a').click()")
            mainS().explicitWait(main_spring_logo)
            time.sleep(5)
        else:
            print("Just clicking on navBar only as none paramerters are passed!!!")

    def selectFromDropDownFor(self, choice):
        if choice is "releases":
            driver.execute_script("document.querySelector('#LOCK_Releases').click()")
            time.sleep(5)
        elif choice is "sprints":
            driver.execute_script("document.querySelector('#LOCK_Sprints').click()")
            time.sleep(5)
        elif choice is "executionboard":
            driver.execute_script("document.querySelector('#LOCK_Execution_Board').click()")
            time.sleep(5)

    def clickOnComcast(self):
        driver.find_element_by_xpath("//*[@id='projectIcon']/ul/li[1]/a").click()

    def mouseOnToPlan(self):
        ele = driver.find_element_by_xpath("//*[@id='a_11099469']")
        ActionChains(driver).context_click(ele).perform()

    def selectSprintNumber(self, sprintNum):
        print(sprintNum)
        sprintList = []
        sprintList = driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td[style='width:120px;']")
        print("*" * 60)
        print("\nEnter The Sprint  to proceed:")
        #userSprintInput = input()
        for ele in sprintList:
            if ele.text == sprintNum:  # and userSprintInput == sprintNum:
                print("SELECTING SPRINT ->" + ele.text)
                ele.click()
                break
            else:
                print("Sprint  -> {} not matching with value configured in code as sprintNum-> {} !!!".format(
                    userSprintInput, sprintNum))
                exit()

    def fillAllUserStories(self):
        time.sleep(5)
        driver.execute_script("document.querySelector('#a_9928178').click()")
        # if el.text == "1":
        #     el.click()


if __name__ == '__main__':

    try:
        driver = mainS().initializeBrowser()
        driver.get("https://mainspring.cognizant.com")
        mainS().loginWithCredentials(username, pwd)
        time.sleep(5)
        mainS().clickOnLeftNavBarFor("comcast")  # workspace
        # mainS().mouseOnToPlan()
        mainS().selectFromDropDownFor("sprints")
        mainS().selectSprintNumber(sprintNum=sprintNum)
        mainS().fillAllUserStories()
    except Exception as e:
        traceback.print_exc()
        print(e)
    finally:
        z = input()
        if (z is "z"):
            time.sleep(30)
            driver.quit()
            print("Driver quit successfull")
