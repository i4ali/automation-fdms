from selenium.webdriver.common.by import By
import time
import os
from base.driver import Driver
from selenium.common.exceptions import NoSuchElementException


class SeleniumWebDriver():
    def __init__(self):
        self.driver = Driver.instance()

    def _wait_for_doc_ready(self):
        state = ""
        while state != "complete":
            state = self.driver.execute_script("return document.readyState;")
        return

    def get_url(self,url):
        self.driver.get(url)
        self._wait_for_doc_ready()

    def get_by_type(self, locatorType):
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

    def get_element(self, locator, locatorType="id"):
        self._wait_for_doc_ready()
        element = None
        locatorType = locatorType.lower()
        byType = self.get_by_type(locatorType)
        element = self.driver.find_element(byType, locator)
        return element

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator="", locatorType="id", element=None, info=""):
        try:
            if locator: # This means if locator is not empty
                element = self.get_element(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
        except NoSuchElementException:
            return ""
        return text

    def screenshot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        if not os.path.exists(destinationDirectory):
            os.makedirs(destinationDirectory)
        self.driver.save_screenshot(destinationFile)




