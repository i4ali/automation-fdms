"""
@package pages.base

Base Page class that all pages should inherit from. This class implements the basic
functionality common to all pages

"""
from base.seleniumwebdriver import SeleniumWebDriver


class BasePage:

    def __init__(self):
        self.driver = SeleniumWebDriver()

    def goto(self, url):
        self.driver.get_url(url)

    def isat(self, page_header, locatortype):
        return self.driver.is_element_present(page_header, locatortype)

    def refresh(self):
        self.driver.refresh()