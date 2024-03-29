"""
@package  pages.wells

Landing page object to encapsulate all functionality related to the FDMS wells page. This includes the
locators, functions to be performed on the page
"""

from pages.wells.welledit_page import WellEditPage
from pages.base.base_page import BasePage
from pages.navigation.navigation_page import NavigationPage


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
    urlcontains = 'wells'
    new_well_button_xpath = "//button[text()='New Well']"
    title = 'FDMS'
    well_success_message_toast_xpath = "//*[contains(text(), 'Well successfully created')]"
    new_well_ok_button_xpath = "//button[text()='Create Well']"
    page_header_xpath = "//h1[text()='Wells']"
    pagination_menu_css = "div[class='ui pagination menu']"
    well_table_xpath = "//table[@id='test-data-table']//tbody"
    pagination_listbox_xpath = "//*[@id='test-pagination']"
    pagination_listbox_text_xpath = "//*[@id='test-pagination']/div[@class='text']"
    searchbox_xpath = "//input[@placeholder='Search']"
    searchbox_text_attribute = "value"
    searbox_text_dropdown_xpath = "//*[@id='container']//div[@class='results transition visible']//div[@class='title']"

    def __init__(self):
        super().__init__()
        self.navigation = NavigationPage()
        self.well_edit_page = WellEditPage()

    def is_at(self):
        """
        To be used by test functions. Redirects to project page if not
        already there
        :return:True if successful
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        return self._is_at()

    def _is_at(self):
        """
        Internal function to check if currently at project page
        :return: Boolean
        """
        return self.isat(self.page_header_xpath, "xpath")

    def add_new_well(self, wellname, apinumber): #TODO need another method to add new well with project name
        """
        clicks new well on well page to create new well and enter
        all field information
        :param wellname: well name to be entered into form
        :param apinumber: apinumber to be entered into form
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        self.click_new_well()
        self.well_edit_page.enter_well_name(wellname)
        self.well_edit_page.enter_api_number(apinumber)
        self.well_edit_page.click_create_well()

    def well_success_message_pops(self):
        """
        Check to see if the success message pops after project created
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        return self.driver.is_element_present(self.well_success_message_toast_xpath, "xpath")

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
        if not self._is_at():
            self.navigation.navigate_to_wells()
        self.driver.get_element(self.new_well_button_xpath, "xpath").click()
        return WellEditPage()

    def pagination_menu_exists(self):
        """
        Verify that the pagination menu exists
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        return self.driver.is_element_present(self.pagination_menu_css, "css")

    def page_refresh(self):
        """
        Refresh the page
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        self.driver.refresh()

    def get_table_entries_count(self):
        """
        :return: count of rows in the table
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        table_entries = self.driver.get_child_elements(self.well_table_xpath, "tr", "xpath", "tag")
        return len(table_entries)

    def click_pagination_listbox(self):
        """
        Clicks on the pagination list box menu
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        self.driver.get_element(self.pagination_listbox_xpath).click()

    def get_number_pagination_listbox(self):
        """
        :return: number shown on listbox for pagination
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        return self.driver.get_text(self.pagination_listbox_text_xpath, "xpath")

    def search_well_in_searchbox(self, wellname):
        """
        Enters parameter into searchbox
        :param wellname: wellname to search in searchbox
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        self.driver.get_element(self.searchbox_xpath, "xpath").send_keys(wellname)

    def get_text_from_searchbox_dropdown(self):
        """
        As the data is entered into search box, the dropdown shows with
        the relevant entry. This function should return that entry
        :return: text from searchbox dropdown
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        return self.driver.get_text(self.searbox_text_dropdown_xpath, "xpath")







