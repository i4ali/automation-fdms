"""
Landing page test class to encapsulate test cases related to the landing page for FDMS
web application.

The file is either run individually through pytest testrunner for e.g. 'pytest tests_landing.py' or is run
as part of the test_suites file through pytest testrunner for e.g. 'pytest test_suites.py'.
"""

# standard and site-package import
import unittest
from ddt import ddt, data, unpack
from pymongo import MongoClient
import pytest

# project import
from pages.landing.landing_page import LandingPage
from utilities.read_data import getCSVData
from utilities.teststatus import TestStatus
from base.webdriverfactory import WebDriverFactory


@ddt
class LandingPageTest(unittest.TestCase):
    """
    Landing page test class

    Attributes
    ----------
    wdf : WebDriverFactory instance
    driver : web driver instance obtained from web driver factory instance
    teststatus : TestStatus instance
    conn : MongoClient connection instance
    database : 'service-fdms' database
    well : well collection from the db
    landingpage : LandingPage instance


    Methods
    -------
    clearWellFromDB()
        Fixture to clear Well collection from DB before making any changes to the well DB
        i.e. adding or removing well for e.g.

    test_can_go_to_landing_page()
        Verify that the landing page comes up successfully

    test_add_new_well_success(wellname, apinumber)
        Verify that new well can be added using the appropriate format for wellname and apinumber
        validating the form entries

    test_add_new_well_failure(wellname, apinumber)
        Verify that new well cannot be added for the inappropriate wellname and apinumber
        validating the form entries

    """


    @pytest.fixture(autouse=True)
    def object_setup(self):
        """
        Obtains web driver instance from web driver factory
        Instantiates LandingPage, TestStatus instance to be used by the test class
        The function is called before every test function runs automagically
        """
        self.wdf = WebDriverFactory("chrome")
        self.driver = self.wdf.getWebDriverInstance()
        self.teststatus = TestStatus(self.driver)
        self.landingpage = LandingPage(self.driver)

    @pytest.fixture()
    def clear_well_from_db(self):
        """
        Connects to MongoDB and removes the well collection from the database
        service-fdms
        """
        self.conn = MongoClient("mongodb://localhost:31001/")
        self.database = self.conn['service-fdms']
        self.well = self.database.get_collection('well')
        self.well.delete_many({})

    def test_can_go_to_landing_page(self):
        """
        Instanstiates landing page and verifies the page can be reached
        successfully from the browser
        """
        self.landingpage.goto()
        result = self.landingpage.isat()
        self.teststatus.markFinal("can_go_to_landing_page", result, "URL verification")

    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('testdata/welltestdatagood.csv'))
    @unpack
    def test_add_new_well_success(self, wellname, apinumber):
        """
        Adds a new well to the database
        :param wellname: name of the well to be entered into the form
        :param apinumber: api number to be entered into the form
        """
        self.landingpage.goto()
        self.landingpage.addnewwell(wellname, apinumber)
        result1 = self.landingpage.wellsuccessmessagepops()
        self.teststatus.mark(result1, "success toast message")
        result2 = self.landingpage.wellexists(wellname)
        self.teststatus.markFinal("add_new_well_success", result2, "check well existance in table")


    # @data(*getCSVData('testdata/welltestdatabad.csv'))
    # @unpack
    # def test_add_new_well_fail(self, wellname, apinumber):
    #     pass

    # @data(*getCSVData('../../testdata/welltestdatagood.csv'))
    # @unpack
    # @unittest.skip("WIP")
    # def test_rem_well(self, wellname, apinumber):
    #     self.lp = LandingPage("firefox")
    #     self.lp.goto()
    #     self.lp.addnewwell(wellname, apinumber)
    #     assert self.lp.wellsuccessmessagepops()
    #     assert self.lp.wellexists(wellname)
    #     self.lp.removewell(wellname)
    #     assert self.lp.welldoesntexist(wellname)


