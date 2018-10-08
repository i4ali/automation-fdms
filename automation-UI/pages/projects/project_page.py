"""
@package  pages.projects

Project page object to encapsulate all functionality related to the FDMS projects page. This includes the
locators, functions to be performed on the page
"""

from base.seleniumwebdriver import SeleniumWebDriver
from pages.projects.projectedit_page import ProjectEditPage

class ProjectPage:
    """
        Project page class

        Attributes
        ----------
        url : locator for page url
        driver : web driver instance obtained from web driver factory instance
        urlcontains : string to look for in url
        new_project_button : locator in the form of xpath for the new project button
        project_fields : dictionary to store fieldnames as keys and the locators in the form of
                      name for the values
        title : title of the page
        well_success_message_toast : locator in the form of xpath for the toast message on success for well addition
        create_project_button : locator in the form of xpath for create project button

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

        """
    url = 'http://localhost:9000/projects'
    urlcontains = 'projects'
    new_project_button = "//button[text()='New Project']"
    project_successfully_created_toast = "//*[contains(text(), 'Project successfully created')]"
    project_title = "//h1[contains(text(), 'Projects')]"
    page_header = "//h1[text()='Projects']"

    def __init__(self):
        self.driver = SeleniumWebDriver()

    def add_new_project(self, projectname, companyname, wellname, apinumber):
        self.click_new_project()
        ProjectEditPage().enter_project_name(projectname)
        ProjectEditPage().enter_company_name(companyname)
        ProjectEditPage().enter_well_name(wellname)
        ProjectEditPage().enter_api_number(apinumber)
        ProjectEditPage().click_create_project()

    def goto(self):
        self.driver.get_url(self.url)
        return self

    def isat(self):
        return self.driver.is_element_present(self.page_header, "xpath")

    def project_exists(self, projectname):
        return self.driver.is_element_present(projectname, "link")

    def project_success_message_pops(self):
        return self.driver.is_element_present(self.project_successfully_created_toast, "xpath")

    def get_toast_message(self):
        # TODO grab toast message element and return its text
        pass

    def click_new_project(self):
        self.driver.get_element(self.new_project_button, "xpath").click()


