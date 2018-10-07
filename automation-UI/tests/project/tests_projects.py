"""
@package tests.project

Project page test class to encapsulate test cases related to the project page for FDMS
web application

The file is either run individually through pytest testrunner for e.g. 'pytest tests_projects.py' or is run
as part of the test_suites file through pytest testrunner for e.g. 'pytest tests_projects.py'.
"""

# standard and site-package import
import unittest
from pymongo import MongoClient
from ddt import ddt, data, unpack
import pytest

# project import
from utilities.teststatus import TestStatus
from utilities.read_data import getCSVData
from pages.wells.well_page import WellPage
from pages.projects.project_page import ProjectPage
from pages.projects.projectedit_page import ProjectEditPage
import globalconfig


@ddt
class TestProjects(unittest.TestCase):
    """
        Project page test class

        Attributes
        ----------
        wdf : WebDriverFactory instance
        driver : web driver instance obtained from web driver factory instance
        teststatus : TestStatus instance
        conn : MongoClient connection instance
        database : 'service-fdms' database
        well : well collection from the db
        projectpage : ProjectPage instance


        Methods
        -------
        object_setup()
            Fixture to setup objects needed for every test

        clear_project_from_db()
            Fixture to clear project from DB before making any changes to the DB
            i.e. adding or removing project. Every time a data

        test_can_go_to_project_page()
            Verify that the project page comes up successfully

        test_add_new_project_success(Projectname, Companyname, Wellname, APInumber)
            Verify that new well can be added using the appropriate format for Projectname,
            Companyname, Wellname, APInumber and validating the form entries

        test_add_new_well_failure(wellname, apinumber)
            Verify that new well cannot be added using the inappropriate format for Projectname,
            Companyname, Wellname, APInumber and validating the form entries

        """

    @pytest.fixture(autouse=True)
    def object_setup(self):
        """
        Instantiates ProjectPage, TestStatus instance to be used by the test class
        The function is run before every test function is called
        """
        self.teststatus = TestStatus()
        self.wellpage = WellPage()
        self.projectpage = ProjectPage()
        self.projecteditpage = ProjectEditPage()

    @pytest.fixture()
    def clear_project_from_db(self):
        """
        Connects to MongoDB and removes the project, well and client collection from the database
        service-fdms
        """
        conn = MongoClient(globalconfig.mongoDB_conn_URI)
        db = conn[globalconfig.mongoDB]
        project = db.get_collection('project')
        client = db.get_collection('client')
        well = db.get_collection('well')
        project.delete_many({})
        client.delete_many({})
        well.delete_many({})

    @pytest.mark.smoketest
    def test_can_go_to_project_page(self):
        """
        Instanstiates wells page and verifies the page can be reached
        successfully from the browser
        """
        self.wellpage.goto()
        self.wellpage.navigate_to_projects()
        result = self.projectpage.isat()
        self.teststatus.markFinal(result, "can go to project page")

    @pytest.mark.smoketest
    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('testdata/projecttestdata.csv'))
    @unpack
    def test_add_new_project(self, projectname, companyname, wellname, apinumber):
        """
        Adds a new well to the database
        :param wellname: name of the well to be entered into the form
        :param apinumber: api number to be entered into the form
        :param projectname: project name to entered into the form
        :param companyname: client/company name to be entered into the form
        :param expectedresult: expected result Pass or Fail
        """
        self.wellpage.goto()
        self.wellpage.navigate_to_projects()
        self.projectpage.add_new_project(projectname, companyname, wellname, apinumber)
        result = self.projectpage.project_success_message_pops()
        self.teststatus.mark(result, "project success message pops")
        result2 = self.projectpage.project_exists(projectname)
        self.teststatus.markFinal(result2, "project exists in table")

    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('testdata/wellnamevalidation.csv'))
    @unpack
    def test_wellname_validation(self, wellname, validationmessage):
        """FDMS-182"""
        self.wellpage.goto()
        self.wellpage.navigate_to_projects()
        self.projectpage.click_new_project()
        self.projecteditpage.enter_well_name(wellname)
        self.projecteditpage.click_create_project()
        assert self.projecteditpage.get_validation_message_wellname() == validationmessage.strip()

    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('testdata/apinamevalidation.csv'))
    @unpack
    def test_apiname_validation(self, apinumber, validationmessage):
        """FDMS-183"""
        self.wellpage.goto()
        self.wellpage.navigate_to_projects()
        self.projectpage.click_new_project()
        self.projecteditpage.enter_api_number(apinumber)
        self.projecteditpage.click_create_project()
        assert self.projecteditpage.get_validation_message_apiname() == validationmessage.strip()


    # @pytest.mark.usefixtures("clear_well_from_db")
    # @data(*getCSVData('testdata/projectnamevalidation.csv'))
    # @unpack
    # def test_project_name_validation(self, wellname, apinumber, validationmessage):
    #     """FDMS-183"""
    #     pass