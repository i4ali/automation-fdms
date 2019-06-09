"""
@package pages.projects

ProjectDetailsPage class to encapsulate all functionality related to the FDMS project details page. This includes the
locators, functions to be performed on the page
"""
import re

from pages.base.base_page import BasePage


class ProjectDetailsPage(BasePage):
    regex_url_substring = r"projects/(.+)/details"
    wdvg_wells_checkbox_xpath = "//input[@name='wdvg-wells']"
    map_xpath = "//*[@class='esri-ui-inner-container esri-ui-corner-container']"

    def __init__(self):
        super().__init__()

    def is_at(self):
        match = re.search(self.regex_url_substring, self.driver.get_current_url())
        return True if match else False

    def take_screenshot_map(self):
        ele = self.driver.get_element(self.map_xpath, "xpath")
        file = self.driver.screenshot("map screenshot")
        import cv2, os
        img = cv2.imread(file)
        # ele = self.driver.get_element(self.map_xpath, "xpath")
        ele_y_loc = int(ele.location['y'])
        ele_height = int(ele.size['height'])
        ele_x_loc = int(ele.location['x'])
        ele_width = int(ele.size['width'])
        crop_img = img[ele_y_loc:ele_y_loc+ele_height, ele_x_loc:ele_x_loc+ele_width]
        cv2.imwrite(file, crop_img)
        return file

    def deselect_wells(self):
        self.driver.click_element(self.wdvg_wells_checkbox_xpath, "xpath")

