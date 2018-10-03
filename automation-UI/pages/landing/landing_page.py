"""
@package  pages.landing

Landing page object to encapsulate all functionality related to the FDMS landing page. This includes the
locators, functions to be performed on the page
"""

from base.seleniumwebdriver import SeleniumWebDriver
from pages.landing.welledit.welledit_page import WellEditPage


class LandingPage:
    """
        Landing page class

        Attributes
        ----------
        url : locator for page url
        driver : web driver instance obtained from web driver factory instance
        urlcontains : string to look for in url
        new_well_button : locator in the form of xpath for the new well button
        well_fields : dictionary to store fieldnames as keys and the locators in the form of
                      name for the values
        title : title of the page
        well_success_message_toast : locator in the form of xpath for the toast message on success for well addition
        new_well_ok_button : locator in the form of xpath for create new well button

        Methods
        -------
        goto()
            method to go to the url for the page

        isat()
            method to check if current page is landing page

        add_new_well(wellname, apinumber)
            method to add new well accepting wellname and apinumber as arguments

        well_success_message_pops()
            method to check if the success message pops when well is added

        well_exists(wellname)
            method to check if the well by wellname exists in the table

        """
    _url = 'http://0.0.0.0:30000/'
    _urlcontains = 'wells'
    _new_well_button = "//button[text()='New Well']"
    _well_fields = {
        'Well Name': 'wellName',
        'UWI/API Number': 'uwi'
    }
    _title = 'FDMS'
    _well_success_message_toast = "//*[contains(text(), 'Well successfully created')]"
    _new_well_ok_button = "//button[text()='Create Well']"

    def __init__(self):
        self.driver = SeleniumWebDriver()

    def goto(self):
        self.driver.get_url(self._url)
        return self

    def isat(self):
        return self._urlcontains in self.driver.get_current_url()

    def add_new_well(self, wellname, apinumber):
        new_well_button = self.driver.get_element(self._new_well_button, "xpath")
        new_well_button.click()
        well_name_field = self.driver.get_element(WellEditPage.well_fields['Well name'], "name")
        well_name_field.send_keys(wellname)
        well_name_field = self.driver.get_element(WellEditPage.well_fields['UWI/API Number'], "name")
        well_name_field.send_keys(apinumber)
        self.driver.get_element(WellEditPage.create_well_button, "xpath").click()
        return self

    def well_success_message_pops(self):
        return True if self.driver.get_element(self._well_success_message_toast, "xpath") else False

    def get_toast_message(self):
        # TODO grab toast message element and return its text
        pass

    def well_exists(self, wellname):
        # TODO think about how to handle pagination here before looking for element
        return True if self.driver.get_element(wellname, "link") else False






