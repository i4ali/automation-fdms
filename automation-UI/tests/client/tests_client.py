"""
@package  tests.client

Client page test class to encapsulate test cases related to the clients page for FDMS
web application.

The file is either run individually through pytest testrunner for e.g. 'pytest tests_clients.py' or is run
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

    @pytest.fixture(autouse=True)
    def object_setup(self):
        """
        Instantiates ClientPage, ClientEditPage, TestStatus instance to be used by the test class
        The function is run before every test function is called
        """
        self.teststatus = StatusTest()
        self.clientpage = ClientPage()
        self.clienteditpage = ClientEditPage()

    @pytest.fixture()
    def clear_client_from_db(self):
        """
        Connects to DB and removes the well collection from the database
        fdms
        """
        self.client = DBClient(globalconfig.postgres_conn_URI)
        self.client.delete_table('clients')

    @pytest.mark.smoketest
    def test_can_go_to_clients_page(self):
        """
        Instanstiates clients page and verifies the page can be reached
        successfully from the browser
        """
        result = self.clientpage.is_at()
        self.teststatus.mark_final(result, "URL verification")

    @pytest.mark.usefixtures("clear_client_from_db")
    @data(*getCSVData('tests/testdata/clienttestdata.csv'))
    @unpack
    def test_add_new_client(self, companyname):
        """ FDMS-192
        Adds a new client to the database
        :param companyname: name of the client to be entered into the form
        """
        self.clientpage.add_new_client(companyname)
        result = self.clientpage.client_success_message_pops()
        self.teststatus.mark_final(result, "success toast message")

    @pytest.mark.usefixtures("clear_client_from_db")
    @data(*getCSVData('tests/testdata/validation/companynamevalidation.csv'))
    @unpack
    def test_companyname_validation(self, companyname, validationmessage):
        """FDMS-192
        Validates the companyname field when adding a new client
        :param companyname: name of the well to be entered into the form
        :param validationmessage: the expected validation message
        """
        self.clientpage.click_new_client()
        self.clienteditpage.enter_company_name(companyname)
        self.clienteditpage.click_create_client()
        self.teststatus.mark_final(validationmessage == self.clienteditpage.get_validation_message_companyname(), "company name form validation")



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



