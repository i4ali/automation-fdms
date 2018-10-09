"""
@package  pages.projects

Project page object to encapsulate all functionality related to the FDMS projects page. This includes the
locators, functions to be performed on the page
"""

from pages.base.base_page import BasePage
from pages.projects.projectedit_page import ProjectEditPage


class ProjectPage(BasePage):
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
    url = 'http://localhost:9000/projects'
    urlcontains = 'projects'
    new_project_button = "//button[text()='New Project']"
    project_successfully_created_toast = "//*[contains(text(), 'Project successfully created')]"
    project_title = "//h1[contains(text(), 'Projects')]"
    page_header = "//h1[text()='Projects']"

    def __init__(self):
        super().__init__()

    def add_new_project(self, projectname, companyname, wellname, apinumber):
        """
        clicks new project on project page to create new project and enter
        all field information
        :param projectname: project name to be entered into form
        :param companyname: company name to be entered into form
        :param wellname: well name to be entered into form
        :param apinumber: apinumber to be entered into form
        """
        self.click_new_project()
        ProjectEditPage().enter_project_name(projectname)
        ProjectEditPage().enter_company_name(companyname)
        ProjectEditPage().enter_well_name(wellname)
        ProjectEditPage().enter_api_number(apinumber)
        ProjectEditPage().click_create_project()

    def go_to(self):
        """
        Go to the project page
        """
        self.goto(self.url)
        return self

    def is_at(self):
        """
        Check if currently at project page
        :return: Boolean
        """
        return self.isat(self.page_header, "xpath")

    def project_exists(self, projectname):
        """
        Check the project table to see if project by projectname exists
        :param projectname: project name to search
        :return: Boolean
        """
        return self.driver.is_element_present(projectname, "link")

    def project_success_message_pops(self):
        """
        Check to see if the success message pops after project created
        :return: Boolean
        """
        return self.driver.is_element_present(self.project_successfully_created_toast, "xpath")

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
        self.driver.get_element(self.new_project_button, "xpath").click()
        return ProjectEditPage()


