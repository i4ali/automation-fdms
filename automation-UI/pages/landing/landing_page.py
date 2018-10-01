"""
Landing page test to encapsulate all functionality related to the FDMS landing page. This includes the
locators, functions to be performed on the page
"""

from base.webdriver import SeleniumWebDriver


class LandingPage:
    _url = 'http://0.0.0.0:30000/'
    _urlcontains = 'wells'
    _new_well_button = "//button[text()='New Well']"
    _well_fields = {
        'Well Name': 'wellName',
        'UWI/API Number': 'uwi'
    }
    _title = 'FDMS'
    _well_success_message_toast = "//*[contains(text(), 'Well successfully created')]"
    _new_well_ok_button = "//button[text()='OK']"

    def __init__(self, driver):
        self.driver = SeleniumWebDriver(driver)

    def goto(self):
        self.driver.get_url(self._url)

    def isat(self):
        return self._urlcontains in self.driver.getcurrenturl()

    def addnewwell(self, wellname, apinumber):
        new_well_button = self.driver.getElement(self._new_well_button, "xpath")
        new_well_button.click()
        well_name_field = self.driver.getElement(self._well_fields['Well Name'], "name")
        well_name_field.send_keys(wellname)
        well_name_field = self.driver.getElement(self._well_fields['UWI/API Number'], "name")
        well_name_field.send_keys(apinumber)
        self.driver.getElement(self._new_well_ok_button, "xpath").click()

    def wellsuccessmessagepops(self):
        return True if self.driver.getElement(self._well_success_message_toast, "xpath") else False

    def wellexists(self, wellname):
        return True if self.driver.getElement(wellname, "link") else False


    #TODO make this a generic function that every page can use
    # def newprojectbuttonexists(self):
    #     try:
    #         self.driver.find_element_by_xpath(self._new_project_button)
    #     except NoSuchElementException:
    #         return False
    #     else:
    #         return True




