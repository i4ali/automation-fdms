"""
@package  pages.wells

Landing page object to encapsulate all functionality related to the FDMS wells page. This includes the
locators, functions to be performed on the page
"""

from base.seleniumwebdriver import SeleniumWebDriver
from pages.wells.welledit_page import WellEditPage


class WellPage:
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
            method to check if current page is wells page

        add_new_well(wellname, apinumber)
            method to add new well accepting wellname and apinumber as arguments

        well_success_message_pops()
            method to check if the success message pops when well is added

        well_exists(wellname)
            method to check if the well by wellname exists in the table

        """
    url = 'http://localhost:9000/'
    urlcontains = 'wells'
    new_well_button = "//button[text()='New Well']"
    title = 'FDMS'
    well_success_message_toast = "//*[contains(text(), 'Well successfully created')]"
    new_well_ok_button = "//button[text()='Create Well']"
    projects_link = "a[href='/projects']"
    page_header = "//h1[text()='Wells']"

    def __init__(self):
        self.driver = SeleniumWebDriver()

    def goto(self):
        self.driver.get_url(self.url)
        return self

    def isat(self):
        return self.driver.is_element_present(self.page_header, "xpath")

    def add_new_well(self, wellname, apinumber):
        self.click_new_well()
        WellEditPage().enter_well_name(wellname)
        WellEditPage().enter_api_number(apinumber)
        WellEditPage().click_create_well()

    def well_success_message_pops(self):
        return self.driver.is_element_present(self.well_success_message_toast, "xpath")

    def get_toast_message(self):
        # TODO grab toast message element and return its text
        pass

    def edit_well(self):
        #TODO
        pass

    def well_exists(self, wellname):
        # TODO think about how to handle pagination here before looking for element
        return self.driver.is_element_present(wellname, "link")

    def click_new_well(self):
        self.driver.get_element(self.new_well_button, "xpath").click()

    def navigate_to_projects(self):
        self.driver.get_element(self.projects_link, "css").click()







