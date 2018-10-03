"""
@package  pages.projects

Project page object to encapsulate all functionality related to the FDMS projects page. This includes the
locators, functions to be performed on the page
"""

from base.seleniumwebdriver import SeleniumWebDriver
from pages.projects.projectedit.projectedit_page import ProjectEditPage

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
            method to check if current page is landing page

        add_new_project(projectname, companyname, wellname, apinumber)
            method to add new project

        project_success_message_pops()
            method to check if the success message pops when project is added

        project_exists(projectname)
            method to check if the projectname by projectname exists in the table

        """
    _url = 'http://0.0.0.0:30000/projects'
    _urlcontains = 'projects'
    _new_project_button = "//button[text()='New Project']"
    _project_successfully_created_toast = "//*[contains(text(), 'Project successfully created')]"
    _project_title = "//h1[contains(text(), 'Projects')]"

    def __init__(self, driver):
        self.driver = SeleniumWebDriver(driver)

    def add_new_project(self, projectname, companyname, wellname, apinumber=None):
        new_proj_button = self.driver.get_element(self._new_project_button, "xpath")
        new_proj_button.click()
        projectname_field = self.driver.get_element(ProjectEditPage.project_fields['Project Name'], "name")
        projectname_field.send_keys(projectname)
        companyname_field = self.driver.get_element(ProjectEditPage.project_fields['Company Name'], "name")
        companyname_field.send_keys(companyname)
        wellname_field = self.driver.get_element(ProjectEditPage.project_fields['Well Name'], "name")
        wellname_field.send_keys(wellname)
        if apinumber is not None:
            apinumber_field = self.driver.get_element(ProjectEditPage.project_fields['UWI / API Number'], "name")
            apinumber_field.send_keys(apinumber)
        self.driver.get_element(ProjectEditPage.create_project_button, "xpath").click()
        return self

    def goto(self):
        self.driver.get_url(self._url)
        return self

    def isat(self):
        return True if self.driver.get_element(self._project_title, "xpath") else False

    def project_exists(self, projectname):
        return True if self.driver.get_element(projectname, "link") else False

    def project_success_message_pops(self):
        return True if self.driver.get_element(self._project_successfully_created_toast, "xpath") else False

    def get_toast_message(self):
        # TODO grab toast message element and return its text
        pass
