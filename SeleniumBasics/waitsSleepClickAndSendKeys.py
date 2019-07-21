import time

from SeleniumBasics.launchBrowserAndLocatorsShortcuts import Browserinitialize


class AutomationOnPage():
    def loginAutomation(self, loginUrl):
        driver = Browserinitialize().inititalizeBrowser("chrome")
        driver.maximize_window()
        driver.implicitly_wait(10)  # IMPLICITLY WAIT DEMO
        driver.get(loginUrl)
        userNameField = driver.find_element_by_css_selector(".form-control.input-hg#user_email")
        userNameField.send_keys("someUserName@something.com")
        passwordField = driver.find_element_by_css_selector(".form-control.input-hg#user_password")
        passwordField.send_keys("someRandomPass")
        userNameField.clear()
        userNameField.send_keys("somerandomangain")
        print("Executing pythons time.sleep(3) for 3 seconds")
        time.sleep(5)
        driver.refresh()


urlToTest = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1"

if __name__ == '__main__':
    print("__name__ -> " + __name__)
    AutomationOnPage().loginAutomation(urlToTest)
