"""
@package  pages.wells

Landing page object to encapsulate all functionality related to the FDMS wells page. This includes the
locators, functions to be performed on the page
"""

from pages.wells.welledit_page import WellEditPage
from pages.base.base_page import BasePage


class WellPage(BasePage):
    """
        Landing page class

        Attributes
        ----------
        url : locator for page url
        driver : web driver instance obtained from web driver factory instance
        urlcontains : string to look for in url
        new_well_button : locator in the form of xpath for the new well button
        title : title of the page
        well_success_message_toast : locator in the form of xpath for the toast message on success for well addition
        new_well_ok_button : locator in the form of xpath for create new well button
        page_header : locator in the form of xpath for the page header

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

        click_new_well()
            method to click new well button on wells page

        navigate_to_projects()
            method to navigate to projects page

        """
    url = 'http://localhost:9000/'
    urlcontains = 'wells'
    new_well_button = "//button[text()='New Well']"
    title = 'FDMS'
    well_success_message_toast = "//*[contains(text(), 'Well successfully created')]"
    new_well_ok_button = "//button[text()='Create Well']"
    page_header = "//h1[text()='Wells']"
    pagination_menu = "div[class='ui pagination menu']"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.goto(self.url)
        return self

    def is_at(self):
        return self.isat(self.page_header, "xpath")

    def add_new_well(self, wellname, apinumber):
        """
        clicks new well on well page to create new well and enter
        all field information
        :param wellname: well name to be entered into form
        :param apinumber: apinumber to be entered into form
        """
        self.click_new_well()
        WellEditPage().enter_well_name(wellname)
        WellEditPage().enter_api_number(apinumber)
        WellEditPage().click_create_well()

    def well_success_message_pops(self):
        """
        Check to see if the success message pops after project created
        :return: Boolean
        """
        return self.driver.is_element_present(self.well_success_message_toast, "xpath")

    def get_toast_message(self):
        """
        Find the toast element and return its message
        :return: text of the toast message
        """
        # TODO grab toast message element and return its text
        pass

    def edit_well(self):
        #TODO
        pass

    def well_exists(self, wellname):
        # TODO think about how to handle pagination here before looking for element
        return self.driver.is_element_present(wellname, "link")

    def click_new_well(self):
        """
        Click the new  well button on the well page
        """
        self.driver.get_element(self.new_well_button, "xpath").click()
        return WellEditPage()

    def pagination_menu_exists(self):
        return self.driver.is_element_present(self.pagination_menu, "css")








