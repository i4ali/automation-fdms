"""
@package base

This is a module that implements the Singleton driver class
"""

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import globalconfig


class Driver:
    """
    Singleton Driver class to enforce one driver instance use

    Methods
    -------
    instance()
        return driver instance. Same instance if already exists

    """
    @staticmethod
    def instance():
        if '_instance' not in Driver.__dict__:
            if globalconfig.browser.lower() == "chrome":
                Driver._instance = WebDriver()
            elif globalconfig.browser.lower() == "firefox":
                Driver._instance = webdriver.Firefox()
            elif globalconfig.browser.lower() == "iexplorer":
                Driver._instance = webdriver.Ie()
            else:
                Driver._instance = WebDriver() # chrome if not specified
            Driver._instance.implicitly_wait(globalconfig.browser_implicit_wait_in_secs)
        return Driver._instance
