"""
@package pages.projects

ProjectEditPage class to encapsulate all functionality related to the FDMS project page. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage
import os

class ProjectEditDataPage(BasePage):
    create_project_button_xpath = "//button[text()='Save and Continue']"
    data_entry_title_xpath = "//span[text()='Data Entry']"
    choose_file_id = "inputFile"

    def __init__(self):
        super().__init__()

    def is_at(self):
        return self.isat(self.data_entry_title_xpath, "xpath")

    def upload_shapefile(self, shapefile):
        self.driver.get_element(self.choose_file_id).send_keys(os.path.join(os.getcwd(), shapefile))
        self.driver.get_element(self.create_project_button_xpath, "xpath").click()





