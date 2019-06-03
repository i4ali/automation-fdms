"""
@package pages.projects

ProjectDetailsPage class to encapsulate all functionality related to the FDMS project details page. This includes the
locators, functions to be performed on the page
"""
import re

from pages.base.base_page import BasePage


class ProjectDetailsPage(BasePage):
    regex_url_substring = r"projects/(.+)/details"

    def __init__(self):
        super().__init__()

    def is_at(self):
        match = re.search(self.regex_url_substring, self.driver.get_current_url())
        return True if match else False


