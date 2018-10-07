"""
@package  tests.wells

Landing page test class to encapsulate test cases related to the wells page for FDMS
web application.

The file is either run individually through pytest testrunner for e.g. 'pytest tests_wells.py' or is run
as part of the test_suites file through pytest testrunner for e.g. 'pytest test_suites.py'.
"""

# standard and site-package import
import unittest
from ddt import ddt, data, unpack
from pymongo import MongoClient
import pytest

# project import
from pages.wells.well_page import WellPage
from pages.wells.welledit_page import WellEditPage
from utilities.read_data import getCSVData
from utilities.teststatus import TestStatus
import globalconfig


@ddt
class TestWells(unittest.TestCase):
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
    wellpage : LandingPage instance


    Methods
    -------
    clearWellFromDB()
        Fixture to clear Well collection from DB before making any changes to the well DB
        i.e. adding or removing well for e.g.

    test_can_go_to_landing_page()
        Verify that the wells page comes up successfully

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
        Instantiates LandingPage, TestStatus instance to be used by the test class
        The function is run before every test function is called
        """
        self.teststatus = TestStatus()
        self.wellpage = WellPage()
        self.welleditpage = WellEditPage()

    @pytest.fixture()
    def clear_well_from_db(self):
        """
        Connects to MongoDB and removes the well collection from the database
        service-fdms
        """
        self.conn = MongoClient(globalconfig.mongoDB_conn_URI)
        self.database = self.conn[globalconfig.mongoDB]
        self.well = self.database.get_collection('well')
        self.well.delete_many({})

    @pytest.mark.smoketest
    def test_can_go_to_landing_page(self):
        """
        Instanstiates wells page and verifies the page can be reached
        successfully from the browser
        """
        self.wellpage.goto()
        result = self.wellpage.isat()
        self.teststatus.markFinal(result, "URL verification")

    @pytest.mark.smoketest
    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('testdata/welltestdata.csv'))
    @unpack
    def test_add_new_well(self, wellname, apinumber):
        """
        Adds a new well to the database
        :param wellname: name of the well to be entered into the form
        :param apinumber: api number to be entered into the form
        :param expectedresult: expected result Pass or Fail for the entry
        """
        self.wellpage.goto()
        self.wellpage.add_new_well(wellname, apinumber)
        result1 = self.wellpage.well_success_message_pops()
        self.teststatus.mark(result1, "success toast message")
        result2 = self.wellpage.well_exists(wellname)
        self.teststatus.markFinal(result2, "check well existance in table")

    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('testdata/wellnamevalidation.csv'))
    @unpack
    def test_wellname_validation(self, wellname, validationmessage):
        """FDMS-182"""
        self.wellpage.goto()
        self.wellpage.click_new_well()
        self.welleditpage.enter_well_name(wellname)
        self.welleditpage.click_create_well()
        assert self.welleditpage.get_validation_message_wellname() == validationmessage.strip()


    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('testdata/apinamevalidation.csv'))
    @unpack
    def test_apiname_validation(self, apinumber, validationmessage):
        """FDMS-183"""
        self.wellpage.goto()
        self.wellpage.click_new_well()
        self.welleditpage.enter_api_number(apinumber)
        self.welleditpage.click_create_well()
        assert self.welleditpage.get_validation_message_apiname() == validationmessage.strip()




    # @data(*getCSVData('../../testdata/welltestdata.csv'))
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


