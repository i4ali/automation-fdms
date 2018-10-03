"""
@package pages.landing.welledit

WellEditPage class to encapsulate all functionality related to the FDMS landing page. This includes the
locators, functions to be performed on the page
"""

from base.webdriver import SeleniumWebDriver


class WellEditPage:
    url = 'http://0.0.0.0:30000/wells/edit-well'
    create_well_button = "//button[text()='Create Well']"
    well_fields = {
        'Well name': 'wellName',
        'UWI/API Number': 'uwi'
    }
    title = 'FDMS'
    project_title = "//h1[contains(text(), 'NEW WELL')]"
    uwi_api_number_validation_message = "//div[contains(text(), 'UWI / API must be either 14 or 16 characters.')]"
    well_name_validation_message = "//div[contains(text(), 'Well name is required.')]"

    def __init__(self, driver):
        self.driver = SeleniumWebDriver(driver)

    def goto(self):
        self.driver.get_url(self.url)

    def isat(self):
        return True if self.driver.get_element(self.project_title, "xpath") else False





