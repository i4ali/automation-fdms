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
from selenium.webdriver.support import expected_conditions
from utilities.customlogger import customlogger
import globalconfig


class SeleniumWebDriver():
    log = customlogger(globalconfig.logging_level)

    def __init__(self):
        self.driver = Driver.instance()

    def _wait_for_doc_ready(self):
        state = ""
        while state != "complete":
            state = self.driver.execute_script("return document.readyState;")
        return

    def get_url(self,url):
        self.log.info("go to url {0}".format(url))
        self.driver.get(url)
        self._wait_for_doc_ready()

    def get_by_type(self, locatorType):
        self.log.info("get by type for locator type {0}".format(locatorType))
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
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def get_element(self, locator, locatorType="id"):
        self.log.info("getting element with locator {0} and locator type {1}".format(locator, locatorType))
        self._wait_for_doc_ready()
        locatorType = locatorType.lower()
        byType = self.get_by_type(locatorType)
        try:
            element = self.driver.find_element(byType, locator)
        except NoSuchElementException:
            self.log.error("Element not found using Locator-{0}, Locator type-{1}".format(locator, locatorType))
            return None
        return element

    def get_child_elements_given_parent_element(self, parentelement, locatorChild, locatorTypeChild="id"):
        self.log.info("getting child element(s) with locator {0} and locatortype {1}"
                           "for parent {2}".format(locatorChild, locatorTypeChild, parentelement))
        self._wait_for_doc_ready()
        byType = self.get_by_type(locatorTypeChild.lower())
        elements = parentelement.find_elements(byType, locatorChild)
        if elements is not None:
            return elements
        else:
            self.log.error("Child element(s) with locator {0} and locatortype {1} "
                           "not found for parent-{0}".format(locatorChild, locatorTypeChild, parentelement))
            return None

    def get_child_elements(self, locatorParent, locatorChild, locatorTypeParent="id", locatorTypeChild="id"):
        self.log.info("getting child element(s) with locator {0} and locatortype {1}"
                           "for parent with locator {2} and locatortype {3}".format(locatorChild, locatorTypeChild, locatorParent, locatorTypeParent))
        self._wait_for_doc_ready()
        locatorChildType = locatorTypeChild.lower()
        ChildbyType = self.get_by_type(locatorChildType)
        parent_element = self.get_element(locatorParent, locatorTypeParent)
        elements = parent_element.find_elements(ChildbyType, locatorChild)
        if elements is not None:
            return elements
        else:
            self.log.error("Child element(s) with locator {0} and locatortype {1} not found "
                           "for parent with locator {2} and locatortype {3}".format(locatorChild, locatorTypeChild, locatorParent, locatorTypeParent))
            return None

    def is_element_present(self, locator="", locatorType="id", element=None):
        self.log.info("checking if element with locator {0}, locator type {1} "
                      "or element {2} is present".format(locator, locatorType, element))
        self._wait_for_doc_ready()
        if locator:  # This means if locator is not empty
            element = self.get_element(locator, locatorType)
        if element is not None:
            return True
        else:
            return False

    def click_element(self, locator="", locatorType="id"):
        element = self.get_element(locator, locatorType)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((self.get_by_type(locatorType), locator)))
        self.driver.execute_script("arguments[0].click();", element)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator="", locatorType="id", element=None, info=""):
        self.log.info("getting text for element with locator {0}, "
                      "locator type {1} or element {2}".format(locator, locatorType, element))
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
        return destinationFile

    def refresh(self):
        self.driver.refresh()

    def wait_for_element_visible(self, locator="", locatorType="id"):
        self.log.info("wait for element with locator {0}, with locator type {1}".format(locator, locatorType))
        element = self.get_element(locator, locatorType)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(element))

    def get_page_source(self):
        return self.driver.page_source






