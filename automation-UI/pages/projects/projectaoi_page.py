"""
@package pages.projects

ProjectEditDataPage class to encapsulate all functionality related to the FDMS project edit data page. This includes the
locators, functions to be performed on the page
"""
import os

from pages.base.base_page import BasePage


class ProjectAOIPage(BasePage):
    url_contains = "acreage-planner/aoi"
    client_acreage_eyeball_xpath = "//*[@title='Client Acreage']"
    wdvg_wells_eyeball_xpath = "//*[@title='WDVG Wells']"
    save_geomodel_button_xpath = "//button[text()='Save Geomodel']"
    upload_acreage_button_xpath = "//button[text()='Upload Acreage']"
    upload_acreage_input_xpath = "//input[@accept='.zip']"
    upload_acreage_success_message_toast_xpath = "//*[contains(text(), 'Project acreage successfully created')]"

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

    def upload_acreage(self, shapefile):
        self.driver.get_element(self.upload_acreage_input_xpath, "xpath").send_keys(os.getcwd()+"/"+shapefile)

    def upload_acreage_success_message_pops(self):
        return self.driver.is_element_present(self.upload_acreage_success_message_toast_xpath, "xpath")








