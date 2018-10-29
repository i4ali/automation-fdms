"""
@package  tests.client

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
from pages.clients.client_page import ClientPage
from pages.clients.clientedit_page import ClientEditPage
from pages.wells.welledit_page import WellEditPage
from utilities.read_data import getCSVData
from utilities.statustest import StatusTest
import globalconfig
from base.DBclient import DBClient


@ddt
class TestClients(unittest.TestCase):
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
        self.clientpage = ClientPage()
        self.clienteditpage = ClientEditPage()

    @pytest.fixture()
    def clear_well_from_db(self):
        """
        Connects to MongoDB and removes the well collection from the database
        service-fdms
        """
        self.client = DBClient(globalconfig.postgres_conn_URI)
        self.client.delete_table('clients')

    @pytest.mark.smoketest
    def test_can_go_to_clients_page(self):
        """
        Instanstiates wells page and verifies the page can be reached
        successfully from the browser
        """
        result = self.clientpage.is_at()
        self.teststatus.mark_final(result, "URL verification")

    @pytest.mark.smoketest
    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('tests/testdata/clienttestdata.csv'))
    @unpack
    def test_add_new_client(self, companyname):
        """
        Adds a new well to the database
        :param wellname: name of the well to be entered into the form
        :param apinumber: api number to be entered into the form
        :param expectedresult: expected result Pass or Fail for the entry
        """
        self.clientpage.add_new_client(companyname)
        result = self.clientpage.client_success_message_pops()
        self.teststatus.mark_final(result, "success toast message")

    @pytest.mark.usefixtures("clear_well_from_db")
    @data(*getCSVData('tests/testdata/validation/companynamevalidation.csv'))
    @unpack
    def test_companyname_validation(self, companyname, validationmessage):
        """FDMS-183
        Validates the wellname field when adding a new well
        :param wellname: name of the well to be entered into the form
        :param validationmessage: the expected validation message
        """
        self.clientpage.click_new_client()
        self.clienteditpage.enter_company_name(companyname)
        self.clienteditpage.click_create_client()
        self.teststatus.mark_final(validationmessage == self.clienteditpage.get_validation_message_companyname(), "company name form validation")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_client_pagination_limit_exceed_and_pagination_menu_exists(self):
        # insert bulk data such that pagination limit is exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/clientpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_client(row[0])
            table_entries+=1
        # verify pagination menu exists
        self.clientpage.page_refresh()
        result = self.clientpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_client_pagination_limit_not_exceed_and_pagination_menu_doesnt_exist(self):
        # insert bulk data such that pagination limit is not exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/clientpaginationnotexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_client(row[0])
            table_entries+=1
        # verify pagination menu doesnt exists
        self.clientpage.page_refresh()
        result = not self.clientpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_client_pagination_limit_exceed_and_table_has_rows_to_match_default_limit(self):
        # insert bulk data such that pagination limit is exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/clientpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_client(row[0])
            table_entries += 1
        self.clientpage.page_refresh()
        self.teststatus.mark_final(self.clientpage.get_table_entries_count() == globalconfig.pagination_limit,
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



