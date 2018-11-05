"""
@package pages.clients

ClientEditPage class to encapsulate all functionality related to the FDMS client edit page. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage
from pages.navigation.navigation_page import NavigationPage


class ClientEditPage(BasePage):

    create_client_button_xpath = "//button[text()='Submit']"
    client_fields = {
        'Company Name': 'companyName',
    }
    title = 'FDMS'
    client_title_xpath = "//h1[contains(text(), 'New Client')]"
    companyname_validation_message_id = 'test-companyName'

    def __init__(self):
        super().__init__()
        self.navigation = NavigationPage()

    def is_at(self):
        return self.isat(self.client_title_xpath, "xpath")

    def enter_company_name(self, companyname):
        self.driver.get_element(self.client_fields['Company Name'], "name").send_keys(companyname)

    def click_create_client(self):
        self.driver.get_element(self.create_client_button_xpath, "xpath").click()

    def get_validation_message_companyname(self):
        return self.driver.get_text(self.companyname_validation_message_id, "id")




