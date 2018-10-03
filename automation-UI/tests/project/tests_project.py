"""
@package tests.project

Project page test class to encapsulate test cases related to the project page for FDMS
web application

The file is either run individually through pytest testrunner for e.g. 'pytest tests_project.py' or is run
as part of the test_suites file through pytest testrunner for e.g. 'pytest tests_project.py'.
"""

# standard and site-package import
import unittest
from pymongo import MongoClient
from ddt import ddt, data, unpack
import pytest

# project import
from utilities.teststatus import TestStatus
from utilities.read_data import getCSVData
from pages.projects.project_page import ProjectPage
import globalconfig
from base.driver import Driver

@ddt
class ProjectPageTest(unittest.TestCase):
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

    @pytest.yield_fixture(scope="class", autouse=True)
    def class_setup(self):
        self.driver = Driver.instance()
        yield
        self.driver.quit()

    @pytest.yield_fixture(autouse=True)
    def object_setup(self):
        """
        Obtains web driver instance from web driver factory
        Instantiates LandingPage, TestStatus instance to be used by the test class
        The function is run twice as follows:
        a) before every test function and runs the code before the yield keyword
        b) after every test function and runs the code after the yield keyword
        """
        self.teststatus = TestStatus()
        self.projectpage = ProjectPage()

    @pytest.fixture()
    def clear_project_from_db(self):
        """
        Connects to MongoDB and removes the project, well and client collection from the database
        service-fdms
        """
        conn = MongoClient(globalconfig.mongoDB_conn_URI)
        db = conn['service-fdms']
        project = db.get_collection('project')
        client = db.get_collection('client')
        well = db.get_collection('well')
        project.delete_many({})
        client.delete_many({})
        well.delete_many({})


    def test_can_go_to_project_page(self):
        """
        Instanstiates landing page and verifies the page can be reached
        successfully from the browser
        """
        self.projectpage.goto()
        result = self.projectpage.isat()
        self.teststatus.markFinal(result, "can go to project page")

    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('testdata/projecttestdataandexpectedresult.csv'))
    @unpack
    def test_add_new_project(self, projectname, companyname, wellname, apinumber, expectedresult):
        """
        Adds a new well to the database
        :param wellname: name of the well to be entered into the form
        :param apinumber: api number to be entered into the form
        :param projectname: project name to entered into the form
        :param companyname: client/company name to be entered into the form
        :param expectedresult: expected result Pass or Fail
        """
        self.projectpage.goto()
        self.projectpage.add_new_project(projectname, companyname, wellname, apinumber)
        result = self.projectpage.project_success_message_pops()
        self.teststatus.mark(result, "project success message pops", expectedresult)
        result2 = self.projectpage.project_exists(projectname)
        self.teststatus.markFinal(result2, "project exists in table", expectedresult)