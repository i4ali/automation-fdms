"""
@package  pages.projects

Project page object to encapsulate all functionality related to the FDMS projects page. This includes the
locators, functions to be performed on the page
"""

from pages.base.base_page import BasePage
from pages.projects.projectedit_page import ProjectEditPage
from pages.clients.client_page import ClientPage
from pages.navigation.navigation_page import NavigationPage


class ProjectPage(BasePage):

    urlcontains = 'projects'
    new_project_button_xpath = "//button[text()='New Project']"
    project_successfully_created_toast_xpath = "//*[contains(text(), 'Project successfully created')]"
    project_title_xpath = "//h1[contains(text(), 'Projects')]"
    page_header_xpath = "//h1[text()='Projects']"
    pagination_menu_css = "div[class='ui pagination menu']"
    project_table_xpath = "//table[@id='test-data-table']//tbody"
    searchbox_xpath = "//input[@placeholder='Search']"
    searchbox_text_attribute = "value"
    searbox_text_dropdown_xpath = "//*[@id='container']//div[@class='results transition visible']//div[@class='title']"

    def __init__(self):
        super().__init__()
        self.navigation = NavigationPage()
        self.project_edit_page = ProjectEditPage()
        self.client_page = ClientPage()

    def add_new_project(self, projectname, companyname):
        """
        clicks new project on project page to create new project and enter
        all field information
        :param projectname: project name to be entered into form
        :param companyname: company name to be entered into form
        """
        self.navigation.navigate_to_clients()
        self.client_page.add_new_client(companyname)
        self.navigation.navigate_to_projects()
        self.click_new_project()
        self.project_edit_page.enter_project_name(projectname)
        self.project_edit_page.select_company_name(companyname)
        self.project_edit_page.click_create_project()

    def is_at(self):
        """
        To be used by test functions. Redirects to project page if not
        already there
        :return:True if successful
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        return self._is_at()

    def _is_at(self):
        """
        Internal function to check if currently at project page
        :return: Boolean
        """
        return self.isat(self.page_header_xpath, "xpath")

    def project_exists(self, projectname):
        """
        Check the project table to see if project by projectname exists
        :param projectname: project name to search
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        return self.driver.is_element_present(projectname, "link")

    def project_success_message_pops(self):
        """
        Check to see if the success message pops after project created
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        return self.driver.is_element_present(self.project_successfully_created_toast_xpath, "xpath")

    def get_toast_message(self):
        """
        Find the toast element and return its message
        :return: text of the toast message
        """
        # TODO grab toast message element and return its text
        pass

    def click_new_project(self):
        """
        Click the new project button on the project page
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        self.driver.get_element(self.new_project_button_xpath, "xpath").click()
        return ProjectEditPage()

    def page_refresh(self):
        """
        Refresh the page
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        self.driver.refresh()

    def pagination_menu_exists(self):
        """
        Verify that the pagination menu exists
        :return: Boolean
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        return self.driver.is_element_present(self.pagination_menu_css, "css")

    def get_table_entries_count(self):
        """
        Return the count of rows in the table
        :return: count of rows in the table
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        table_entries = self.driver.get_child_elements(self.project_table_xpath, "tr", "xpath", "tag")
        return len(table_entries)

    def search_project_in_searchbox(self, projectname):
        """
        Enters parameter into searchbox
        :param projectname: projectname to search in searchbox
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        self.driver.get_element(self.searchbox_xpath, "xpath").send_keys(projectname)

    def get_text_from_searchbox_dropdown(self):
        """
        As the data is entered into search box, the dropdown shows with
        the relevant entry. This function should return that entry
        :return: text from searchbox dropdown
        """
        if not self._is_at():
            self.navigation.navigate_to_projects()
        return self.driver.get_text(self.searbox_text_dropdown_xpath, "xpath")


