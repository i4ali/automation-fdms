"""
@packages base

"""

from selenium.webdriver.common.by import By
import time
import os
from base.driver import Driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
        elif locatorType == "tag":
            return By.TAG_NAME
        return False

    def get_element(self, locator, locatorType="id"):
        self._wait_for_doc_ready()
        locatorType = locatorType.lower()
        byType = self.get_by_type(locatorType)
        try:
            element = self.driver.find_element(byType, locator)
        except NoSuchElementException:
            return None
        # element = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((byType, locator))
        # )
        return element

    def get_child_elements_given_parent_element(self, parentelement, locatorChild, locatorTypeChild="id"):
        byType = self.get_by_type(locatorTypeChild.lower())
        elements = parentelement.find_elements(byType, locatorChild)
        if elements is not None:
            return elements
        else:
            return None

    def get_child_elements(self, locatorParent, locatorChild, locatorTypeParent="id", locatorTypeChild="id"):
        locatorChildType = locatorTypeChild.lower()
        ChildbyType = self.get_by_type(locatorChildType)
        parent_element = self.get_element(locatorParent, locatorTypeParent)
        elements = parent_element.find_elements(ChildbyType, locatorChild)
        if elements is not None:
            return elements
        else:
            return None

    def is_element_present(self, locator="", locatorType="id", element=None):
        if locator:  # This means if locator is not empty
            element = self.get_element(locator, locatorType)
        if element is not None:
            return True
        else:
            return False

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator="", locatorType="id", element=None, info=""):
        if locator: # This means if locator is not empty
            element = self.get_element(locator, locatorType)
        if element is not None:
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
            if text.isdigit():
                return int(text)
            else:
                return text
        else:
            return ""

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

    def refresh(self):
        self.driver.refresh()





