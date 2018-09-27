from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class LandingPage:
    _url = 'http://0.0.0.0:30000/'
    _title = 'FDMS'
    _new_project_button = "//button[text()='New Project']"
    _create_project_button = "//button[text()='Create']"
    _project_fields = {
        'Project Name': 'projectName',
        'Company Name': 'companyName',
        'Well Name': 'wellName',
        'UWI / API Number': 'uwiNumber'
    }

    def goto(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self._url)

    def isat(self):
        return self.driver.title == self._title

    def newprojectbuttonexists(self):
        try:
            self.driver.find_element_by_xpath(self._new_project_button)
        except NoSuchElementException:
            return False
        else:
            return True

    def validatenewprojectfields(self, *args):
        try:
            for arg in args:
                self.driver.find_element_by_name(self._project_fields[arg])
        except NoSuchElementException:
            return False
        else:
            return True

    def clicknewprojectbutton(self):
        new_proj_button = self.driver.find_element_by_xpath(self._new_project_button)
        new_proj_button.click()

    def addnewproject(self, projectname, companyname, wellname, apinumber=None):
        # new_proj_button = self.driver.find_element_by_xpath(self._new_project_button)
        # new_proj_button.click()
        self.clicknewprojectbutton()
        projectname_field = self.driver.find_element_by_name(self._project_fields['Project Name'])
        projectname_field.send_keys(projectname)
        companyname_field = self.driver.find_element_by_name(self._project_fields['Company Name'])
        companyname_field.send_keys(companyname)
        wellname_field = self.driver.find_element_by_name(self._project_fields['Well Name'])
        wellname_field.send_keys(wellname)
        if apinumber is not None:
            apinumber_field = self.driver.find_element_by_name(self._project_fields['UWI / API Number'])
            apinumber_field.send_keys(apinumber)
        self.driver.find_element_by_xpath(self._create_project_button).click()


