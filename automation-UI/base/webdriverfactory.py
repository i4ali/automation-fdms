"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import globalconfig

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser.lower() == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser.lower() == "firefox":
            driver = webdriver.Firefox()
        elif self.browser.lower() == "chrome":
            # Set chrome driver
            # chromedriver = "/Users/atomar/Documents/workspace_personal/selenium/chromedriver"
            # os.environ["webdriver.chrome.driver"] = chromedriver
            driver = WebDriver()
            driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(globalconfig.browser_implicit_wait_in_secs)
        # Maximize the window
        driver.maximize_window()
        return driver
