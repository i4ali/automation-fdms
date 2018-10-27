"""
@package  pages.navigation
"""
from pages.base.base_page import BasePage


class NavigationPage(BasePage):

    projects_link = "a[href='/projects']"
    wells_link = "a[href='/wells']"
    clients_link = "a[href='/clients']"
    logo_link = "a[href='/']"

    def __init__(self):
        super().__init__()

    def navigate_to_logolink(self):
        self.driver.get_element(self.logo_link, "css").click()

    def navigate_to_projects(self):
        self.driver.get_element(self.projects_link, "css").click()

    def navigate_to_wells(self):
        self.driver.get_element(self.wells_link, "css").click()

    def navigate_to_clients(self):
        self.driver.get_element(self.clients_link, "css").click()



