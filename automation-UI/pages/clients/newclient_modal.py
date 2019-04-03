"""
@package pages.clients

NewClientModalPage class to encapsulate all functionality related to the New Client modal. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage


class NewClientModalPage(BasePage):

    new_client_modal_title_xpath = "//h3[contains(text(), 'New Client')]"

    def __init__(self):
        super().__init__()

    def is_at(self):
        return self.isat(self.new_client_modal_title_xpath, "xpath")



