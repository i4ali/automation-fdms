"""
@package pages.projects

ProjectEditDataPage class to encapsulate all functionality related to the FDMS project edit data page. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage
import os


class ProjectAOIPage(BasePage):
    url_contains = "acreage-planner/aoi"
    client_acreage_eyeball_xpath = "//*[@title='Client Acreage']"
    wdvg_wells_eyeball_xpath = "//*[@title='WDVG Wells']"
    save_geomodel_button_xpath = "//button[text()='Save Geomodel']"

    def __init__(self):
        super().__init__()

    def is_at(self):
        return self.url_contains in self.driver.get_current_url()

    def toggle_client_acreage_button_present(self):
        return self.driver.is_element_present(self.client_acreage_eyeball_xpath, "xpath")

    def toggle_wdvg_wells_button_present(self):
        return self.driver.is_element_present(self.wdvg_wells_eyeball_xpath, "xpath")

    def save_geomodel_button_present(self):
        return self.driver.is_element_present(self.save_geomodel_button_xpath, "xpath")






