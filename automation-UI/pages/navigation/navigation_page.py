"""
@package  pages.navigation
"""
from pages.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        # element = WebDriverWait(self.driver, 10).until(
        #             EC.element_to_be_clickable((locatorType, locator)))
        self.driver.get_element(self.projects_link, "css").click()

    def navigate_to_wells(self):
        self.driver.get_element(self.wells_link, "css").click()

    def navigate_to_clients(self):
        self.driver.get_element(self.clients_link, "css").click()



