"""
@package  pages.clients

Client page object to encapsulate all functionality related to the FDMS clients page. This includes the
locators, functions to be performed on the page
"""

from pages.base.base_page import BasePage
from pages.clients.clientedit_page import ClientEditPage
from pages.navigation.navigation_page import NavigationPage


class ClientPage(BasePage):

    urlcontains = 'clients'
    new_client_button_xpath = "//button[text()='New Client']"
    pagination_menu = "div[class='ui pagination menu']"
    client_successfully_created_toast_xpath = "//*[contains(text(), 'Client successfully created')]"
    project_title_xpath = "//h1[contains(text(), 'Projects')]"
    page_header_xpath = "//h1[text()='Clients']"
    client_table_xpath = "//table[@id='test-data-table']//tbody"

    def __init__(self):
        super().__init__()
        self.navigation = NavigationPage()
        self.client_edit_page = ClientEditPage()

    def add_new_client(self, companyname):
        """
        clicks new project on project page to create new project and enter
        all field information
        :param projectname: project name to be entered into form
        :param companyname: company name to be entered into form
        :param wellname: well name to be entered into form
        :param apinumber: apinumber to be entered into form
        """
        self.click_new_client()
        self.client_edit_page.enter_company_name(companyname)
        self.client_edit_page.click_create_client()

    def is_at(self):
        """
        To be used by test functions. Redirects to project page if not
        already there
        :return:True if successful
        """
        if not self._is_at():
            self.navigation.navigate_to_clients()
        return self._is_at()

    def _is_at(self):
        """
       Internal function to check if currently at project page
       :return: Boolean
       """
        return self.isat(self.page_header_xpath, "xpath")

    def client_exists(self, companyname):
        """
        Check the project table to see if project by projectname exists
        :param projectname: project name to search
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_clients()
        return self.driver.is_element_present(companyname, "link")

    def client_success_message_pops(self):
        """
        Check to see if the success message pops after project created
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_clients()
        return self.driver.is_element_present(self.client_successfully_created_toast_xpath, "xpath")

    def get_toast_message(self):
        """
        Find the toast element and return its message
        :return: text of the toast message
        """
        # TODO grab toast message element and return its text
        pass

    def click_new_client(self):
        """
        Click the new project button on the project page
        """
        if not self._is_at():
            self.navigation.navigate_to_clients()
        self.driver.get_element(self.new_client_button_xpath, "xpath").click()
        return ClientEditPage()

    def page_refresh(self):
        """
        Refresh the page
        """
        if not self._is_at():
            self.navigation.navigate_to_clients()
        self.driver.refresh()

    def pagination_menu_exists(self):
        """
        Verify that the pagination menu exists
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_wells()
        return self.driver.is_element_present(self.pagination_menu, "css")

    def get_table_entries_count(self):
        """
        Return the count of rows in the table
        :return: count of rows in the table
        """
        if not self._is_at():
            self.navigation.navigate_to_clients()
        table_entries = self.driver.get_child_elements(self.client_table_xpath, "tr", "xpath", "tag")
        return len(table_entries)


