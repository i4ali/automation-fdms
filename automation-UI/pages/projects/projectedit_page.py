"""
@package pages.projects

ProjectEditPage class to encapsulate all functionality related to the FDMS project edit page. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage


class ProjectEditPage(BasePage):
    create_project_button_xpath = "//button[text()='Submit']"
    # project_fields = {
    #     'Project Name': 'projectName',
    #     'Company Name': 'companyName',
    # }
    project_name_xpath = "//div[text()='Project Name']/following-sibling::div//input"
    title = 'FDMS'
    project_title_xpath = "//h1[contains(text(), 'NEW PROJECT')]"
    uwi_api_number_validation_message_xpath = "//div[contains(text(), 'UWI / API must be either 14 or 16 characters.')]"
    wellname_validation_message_id = "test-wellName"
    apiname_validation_message_id = 'test-uwi'
    companyname_validation_message_id = 'test-companyName'
    projectname_validation_message_xpath = "//div[text()='Project Name']/following-sibling::div//div[@class='required-message']"
    companyname_validation_message_content = "Select or Create a Client."
    companyname_dropdown_xpath = "//div[@name='companyName']//i[@class='dropdown icon']"
    projecttype_dropdown_xpath = "//div[@name='projectType']//i[@class='dropdown icon']"
    basin_dropdown_xpath = "//div[@name='basin']//i[@class='dropdown icon']"
    create_new_company_link_xpath = "//a[text() = 'Create New Client']"

    def __init__(self):
        super().__init__()

    def is_at(self):
        return self.isat(self.project_title_xpath, "xpath")

    def enter_project_name(self, projectname):
        self.driver.get_element(self.project_name_xpath, "xpath").send_keys(projectname)

    def select_company_name(self, companyname):
        companyname_element = "//span[text()='{0}']".format(companyname)
        self.driver.get_element(self.companyname_dropdown_xpath, "xpath").click()
        self.driver.get_element(companyname_element, "xpath").click()

    def select_project_type(self, projecttype):
        projecttype_element = "//span[text()='{0}']".format(projecttype)
        self.driver.get_element(self.projecttype_dropdown_xpath, "xpath").click()
        self.driver.get_element(projecttype_element, "xpath").click()

    def click_create_project(self):
        self.driver.get_element(self.create_project_button_xpath, "xpath").click()

    def get_validation_message_wellname(self):
        return self.driver.get_text(self.wellname_validation_message_id, "id")

    def get_validation_message_apiname(self):
        return self.driver.get_text(self.apiname_validation_message_id, "id")

    def get_validation_message_companyname(self):
        return self.driver.get_text(self.companyname_validation_message_id, "id")

    def companyname_validation_message_shows(self):
        return self.get_validation_message_companyname() == self.companyname_validation_message_content

    def get_validation_message_projectname(self):
        return self.driver.get_text(self.projectname_validation_message_xpath, "xpath")

    def click_create_new_company(self):
        self.driver.get_element(self.create_new_company_link_xpath, "xpath").click()

    def select_basin(self, basin):
        basin_element = "//span[text()='{0}']".format(basin)
        self.driver.get_element(self.basin_dropdown_xpath, "xpath").click()
        self.driver.get_element(basin_element, "xpath").click()




