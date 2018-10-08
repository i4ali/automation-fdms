"""
@package  pages.navigation
"""
from base.seleniumwebdriver import SeleniumWebDriver


class NavigationPage:

    projects_link = "a[href='/projects']"
    wells_link = "a[href='/wells']"
    clients_link = "a[href='/clients']"

    def __init__(self):
        self.driver = SeleniumWebDriver()

    def navigate_to_projects(self):
        self.driver.get_element(self.projects_link, "css").click()

    def navigate_to_wells(self):
        self.driver.get_element(self.wells_link, "css").click()

    def navigate_to_clients(self):
        self.driver.get_element(self.clients_link, "css").click()

