"""
@package pages.projects

ProjectEditPage class to encapsulate all functionality related to the FDMS project page. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage
import os
import time


class AcreagePlanner(BasePage):
    url_substring = "acreage-planner"
    client_acreage_xpath = "//span[@title='Client Acreage']"
    map_id = 'base-container'
    project_data_successfully_created_toast_xpath = "//*[contains(text(), 'Project data successfully created')]"

    def __init__(self):
        super().__init__()

    def is_at(self):
        return self.url_substring in self.driver.get_current_url()

    def success_message_pops(self):
        return self.driver.is_element_present(self.project_data_successfully_created_toast_xpath, "xpath")









