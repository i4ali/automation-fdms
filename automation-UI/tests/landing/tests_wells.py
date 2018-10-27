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
import time

# project import
from pages.wells.well_page import WellPage
from pages.wells.welledit_page import WellEditPage
from utilities.read_data import getCSVData
from utilities.statustest import StatusTest
import globalconfig
from base.DBclient import DBClient


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

    test_add_new_well(wellname, apinumber)
        Verify that new well can be added using the appropriate format for wellname and apinumber
        validating the form entries

    test_wellname_validation(wellname, validationmessage)
        Validate the wellname field of the new well form

    test_apiname_validation(apiname, validationmessage)
        Validate the apiname field of the new well form

    """

    @pytest.fixture(autouse=True)
    def object_setup(self):
        """
        Instantiates LandingPage, TestStatus instance to be used by the test class
        The function is run before every test function is called
        """
        self.teststatus = StatusTest()
        self.wellpage = WellPage()
        self.welleditpage = WellEditPage()

    @pytest.fixture()
    def clear_well_from_db(self):
        """
        Connects to MongoDB and removes the well collection from the database
        service-fdms
        """
        self.client = DBClient(globalconfig.postgres_conn_URI)
        self.client.delete_table('wells')

    @pytest.mark.smoketest
    def test_can_go_to_landing_page(self):
        """
        Instanstiates wells page and verifies the page can be reached
        successfully from the browser
        """
        result = self.wellpage.is_at()
        self.teststatus.mark_final(result, "URL verification")

    @pytest.mark.smoketest
    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('tests/testdata/welltestdata.csv'))
    @unpack
    def test_add_new_well(self, wellname, apinumber):
        """
        Adds a new well to the database
        :param wellname: name of the well to be entered into the form
        :param apinumber: api number to be entered into the form
        :param expectedresult: expected result Pass or Fail for the entry
        """
        self.wellpage.add_new_well(wellname, apinumber)
        result = self.wellpage.well_success_message_pops()
        self.teststatus.mark_final(result, "success toast message")

    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('tests/testdata/validation/wellnamevalidation.csv'))
    @unpack
    def test_wellname_validation(self, wellname, validationmessage):
        """FDMS-183
        Validates the wellname field when adding a new well
        :param wellname: name of the well to be entered into the form
        :param validationmessage: the expected validation message
        """
        self.wellpage.click_new_well()
        self.welleditpage.enter_well_name(wellname)
        self.welleditpage.click_create_well()
        self.teststatus.mark_final(validationmessage == self.welleditpage.get_validation_message_wellname(), "wellname form validation")


    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('tests/testdata/validation/apinamevalidation.csv'))
    @unpack
    def test_apiname_validation(self, apinumber, validationmessage):
        """FDMS-182
        Validates the apiname field when adding a new well
        :param apiname: apiname to be entered into the form
        :param validationmessage: the expected validation message
        """
        self.wellpage.click_new_well()
        self.welleditpage.enter_api_number(apinumber)
        self.welleditpage.click_create_well()
        self.teststatus.mark_final(validationmessage == self.welleditpage.get_validation_message_apiname(), "api name form validation")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_well_pagination_limit_exceed_and_pagination_menu_exists(self):
        # insert bulk data such that pagination limit is exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/wellpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_well(row[0], row[1])
            table_entries+=1
        # verify pagination menu exists
        self.wellpage.page_refresh()
        result = self.wellpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_well_pagination_limit_not_exceed_and_pagination_menu_doesnt_exist(self):
        # insert bulk data such that pagination limit is not exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/wellpaginationnotexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_well(row[0], row[1])
            table_entries+=1
        # verify pagination menu doesnt exists
        self.wellpage.page_refresh()
        result = not self.wellpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_well_pagination_limit_exceed_and_table_has_rows_to_match_default_limit(self):
        # insert bulk data such that pagination limit is exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/wellpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_well(row[0], row[1])
            table_entries += 1
        self.wellpage.page_refresh()
        self.teststatus.mark_final(self.wellpage.get_table_entries_count() == globalconfig.pagination_limit,
                                   "table rows match pagination limit")

    # @pytest.mark.pagination
    # @pytest.mark.usefixtures("clear_well_from_db")
    # def test_well_pagination_limit_exceed_and_entries_to_show_match_number_table_rows(self):
    #     # insert bulk data such that pagination limit is exceeded
    #     self.client = DBClient(globalconfig.postgres_conn_URI)
    #     rows = getCSVData('tests/testdata/pagination/wellpaginationexceed.csv')
    #     table_entries = 0
    #     for row in rows:
    #         self.client.insert_well(row[0], row[1])
    #         table_entries += 1
        # verify entries to show matches number of rows in table


    # def test_well_pagination_limit_exceed_and_can_navigate_to_nxt_page(self):
    #     pass



