"""
@package pages.wells.welledit

WellEditPage class to encapsulate all functionality related to the FDMS wells page. This includes the
locators, functions to be performed on the page
"""

from base.seleniumwebdriver import SeleniumWebDriver


class ProjectEditPage:
    url = 'http://0.0.0.0:30000/wells/edit-project'
    create_project_button = "//button[text()='Create Project']"
    project_fields = {
        'Project Name': 'projectName',
        'Company Name': 'companyName',
        'Well Name': 'wellName',
        'UWI/API Number': 'uwi'
    }
    title = 'FDMS'
    project_title = "//h1[contains(text(), 'NEW PROJECT')]"
    uwi_api_number_validation_message = "//div[contains(text(), 'UWI / API must be either 14 or 16 characters.')]"
    wellname_validation_message = "test-wellName"
    apiname_validation_message = 'test-uwi'

    def __init__(self):
        self.driver = SeleniumWebDriver()

    def goto(self):
        self.driver.get_url(self.url)
        return self

    def isat(self):
        return True if self.driver.get_element(self.project_title, "xpath") else False

    def enter_well_name(self, wellname):
        self.driver.get_element(self.project_fields['Well Name'], "name").send_keys(wellname)

    def enter_project_name(self, projectname):
        self.driver.get_element(self.project_fields['Project Name'], "name").send_keys(projectname)

    def enter_company_name(self, companyname):
        self.driver.get_element(self.project_fields['Company Name'], "name").send_keys(companyname)

    def enter_api_number(self, apinumber):
        self.driver.get_element(self.project_fields['UWI/API Number'], "name").send_keys(apinumber)

    def click_create_project(self):
        self.driver.get_element(self.create_project_button, "xpath").click()

    def get_validation_message_wellname(self):
        return self.driver.get_text(self.wellname_validation_message, "id")

    def get_validation_message_apiname(self):
        return self.driver.get_text(self.apiname_validation_message, "id")



