"""
@package pages.wells.welledit

WellEditPage class to encapsulate all functionality related to the FDMS wells page. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage


class ClientEditPage(BasePage):
    url = 'http://0.0.0.0:30000/wells/edit-project'
    create_client_button = "//button[text()='Submit']"
    client_fields = {
        'Company Name': 'companyName',
    }
    title = 'FDMS'
    project_title = "//h1[contains(text(), 'NEW CLIENT')]"
    companyname_validation_message = 'test-companyName'

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.goto(self.url)
        return self

    def is_at(self):
        return self.isat(self.project_title, "xpath")

    def enter_company_name(self, companyname):
        self.driver.get_element(self.client_fields['Company Name'], "name").send_keys(companyname)

    def click_create_client(self):
        self.driver.get_element(self.create_client_button, "xpath").click()

    def get_validation_message_companyname(self):
        return self.driver.get_text(self.companyname_validation_message, "id")




