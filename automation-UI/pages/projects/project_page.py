from base.webdriver import SeleniumWebDriver

class ProjectPage:
    _url = 'http://0.0.0.0:30000/projects'
    _urlcontains = 'projects'
    _new_project_button = "//button[text()='New Project']"
    _create_project_button = "//button[text()='Create']"
    _project_successfully_created_toast = "//*[contains(text(), 'Project successfully created')]"
    _project_fields = {
        'Project Name': 'projectName',
        'Company Name': 'companyName',
        'Well Name': 'wellName',
        'UWI / API Number': 'uwiNumber'
    }

    def __init__(self, driver):
        self.driver = SeleniumWebDriver(driver)

    def addnewproject(self, projectname, companyname, wellname, apinumber=None):
        new_proj_button = self.driver.getElement(self._new_project_button, "xpath")
        new_proj_button.click()
        projectname_field = self.driver.getElement(self._project_fields['Project Name'], "name")
        projectname_field.send_keys(projectname)
        companyname_field = self.driver.getElement(self._project_fields['Company Name'], "name")
        companyname_field.send_keys(companyname)
        wellname_field = self.driver.getElement(self._project_fields['Well Name'], "name")
        wellname_field.send_keys(wellname)
        if apinumber is not None:
            apinumber_field = self.driver.getElement(self._project_fields['UWI / API Number'], "name")
            apinumber_field.send_keys(apinumber)
        self.driver.getElement(self._create_project_button, "xpath").click()

    def goto(self):
        self.driver.get_url(self._url)

    def isat(self):
        return self._urlcontains in self.driver.getcurrenturl()

    def projectexists(self, projectname):
        return True if self.driver.getElement(projectname, "link") else False

    def projectsuccessmessagepops(self):
        return True if self.driver.getElement(self._project_successfully_created_toast, "xpath") else False
