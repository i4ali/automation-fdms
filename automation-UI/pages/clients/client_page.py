"""
@package  pages.projects

Project page object to encapsulate all functionality related to the FDMS projects page. This includes the
locators, functions to be performed on the page
"""

from pages.base.base_page import BasePage
from pages.clients.clientedit_page import ClientEditPage
from pages.navigation.navigation_page import NavigationPage


class ClientPage(BasePage):
    """
        Project page class

        Attributes
        ----------
        url : locator for page url
        driver : web driver instance obtained from web driver factory instance
        urlcontains : string to look for in url
        new_project_button : locator in the form of xpath for the new project button
        project_successfully_created_toast : locator in the form of xpath for the toast message on success for
        well addition
        page_header : locator in the form of xpath for the page header

        Methods
        -------
        goto()
            method to go to the url for the page

        isat()
            method to check if current page is wells page

        add_new_project(projectname, companyname, wellname, apinumber)
            method to add new project

        project_success_message_pops()
            method to check if the success message pops when project is added

        project_exists(projectname)
            method to check if the projectname by projectname exists in the table

        get_toast_message()
            method to grab toast message element and return its text

        click_new_project()
            method to click new project button on project page

        """
    url = 'http://localhost:9000/clients'
    urlcontains = 'clients'
    new_client_button = "//button[text()='New Client']"
    pagination_menu = "div[class='ui pagination menu']"
    client_successfully_created_toast = "//*[contains(text(), 'Client successfully created')]"
    project_title = "//h1[contains(text(), 'Projects')]"
    page_header = "//h1[text()='Clients']"
    client_table = "//table//tbody"
    client_table_rows = "tr"

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
        if not self._is_at():
            self.navigation.navigate_to_clients()
        return self._is_at()

    def _is_at(self):
        """
        Check if currently at project page
        :return: Boolean
        """
        return self.isat(self.page_header, "xpath")

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
        return self.driver.is_element_present(self.client_successfully_created_toast, "xpath")

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
        self.driver.get_element(self.new_client_button, "xpath").click()
        return ClientEditPage()

    def page_refresh(self):
        if not self._is_at():
            self.navigation.navigate_to_clients()
        return self.driver.refresh()

    def pagination_menu_exists(self):
        if not self._is_at():
            self.navigation.navigate_to_wells()
        return self.driver.is_element_present(self.pagination_menu, "css")

    def get_table_entries_count(self):
        if not self._is_at():
            self.navigation.navigate_to_clients()
        table_entries = self.driver.get_child_elements(self.client_table, self.client_table_rows, "xpath", "tag")
        return len(table_entries)


