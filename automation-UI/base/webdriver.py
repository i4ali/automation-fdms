from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumWebDriver():
    def __init__(self, browsertype):
        if browsertype.lower() == "chrome":
            self.browser = WebDriver()
        elif browsertype.lower() == "firefox":
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def _wait_for_doc_ready(self):
        state = ""
        while state != "complete":
            state = self.browser.execute_script("return document.readyState;")
        return

    def get_url(self,url):
        self.browser.get(url)
        self._wait_for_doc_ready()

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        return False

    def getElement(self, locator, locatorType="id"):
        self._wait_for_doc_ready()
        element = None
        locatorType = locatorType.lower()
        byType = self.getByType(locatorType)
        element = self.browser.find_element(byType, locator)
        return element

    def getTitle(self):
        return self.browser.title

    def getcurrenturl(self):
        return self.browser.current_url

    def close(self):
        self.browser.close()



