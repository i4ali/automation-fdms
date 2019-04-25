"""
@package pages.projects

ProjectDetailsPage class to encapsulate all functionality related to the FDMS project details page. This includes the
locators, functions to be performed on the page
"""
from pages.base.base_page import BasePage


class ProjectDetailsPage(BasePage):
    project_details_url_string = 'project-details'

    def __init__(self):
        super().__init__()

    def is_at(self):
        return self.project_details_url_string in self.driver.get_current_url()



