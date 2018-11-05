# standard and site-package import
import unittest
from ddt import ddt, data, unpack
from pymongo import MongoClient
import pytest
import time

# project import
from pages.wells.well_page import WellPage
from pages.projects.project_page import ProjectPage
from pages.clients.clientedit_page import ClientEditPage
from pages.clients.client_page import ClientPage
from pages.projects.projectedit_page import ProjectEditPage
from pages.wells.welledit_page import WellEditPage
from utilities.read_data import getCSVData
from utilities.statustest import StatusTest
import globalconfig
from base.DBclient import DBClient


class TestPagination(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self):
        """
        Instantiates LandingPage, TestStatus instance to be used by the test class
        The function is run before every test function is called
        """
        self.teststatus = StatusTest()
        self.wellpage = WellPage()
        self.projectpage = ProjectPage()
        self.welleditpage = WellEditPage()
        self.projecteditpage = ProjectEditPage()
        self.clientpage = ClientPage()
        self.clienteditpage = ClientEditPage()
        self.client = DBClient(globalconfig.postgres_conn_URI)

    @pytest.fixture()
    def clear_well_from_db(self):
        """
        Connects to DB and removes the well collection from the database
        service-fdms
        """
        self.client.delete_table('well')

    @pytest.fixture()
    def clear_client_from_db(self):
        """
        Connects to DB and removes the well collection from the database
        fdms
        """
        self.client.delete_table('client')

    @pytest.fixture()
    def clear_project_from_db(self):
        """
        Connects to DB and removes the project, well and client collection from the database
        """
        self.client.delete_table('project')
        self.client.delete_table('client')
        self.client.delete_table('well')

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_well_pagination_limit_exceed_and_pagination_menu_exists(self):
        """FDMS-189
        insert bulk data such that pagination limit is exceeded then
        verify pagination menu exists
        """
        rows = getCSVData('tests/testdata/pagination/wellpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_well(row[0], row[1])
            table_entries+=1
        self.wellpage.page_refresh()
        result = self.wellpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_well_pagination_limit_not_exceed_and_pagination_menu_doesnt_exist(self):
        """FDMS-189
        insert bulk data such that pagination limit is not exceeded then
        verify pagination menu doesnt exist
        """
        rows = getCSVData('tests/testdata/pagination/wellpaginationnotexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_well(row[0], row[1])
            table_entries+=1
        self.wellpage.page_refresh()
        result = not self.wellpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_well_from_db")
    def test_well_pagination_limit_exceed_and_table_has_rows_to_match_default_limit(self):
        """FDMS-189
        insert bulk data such that pagination limit is exceeded then
        ensure the number of rows in table match the default specified in config
        """
        rows = getCSVData('tests/testdata/pagination/wellpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_well(row[0], row[1])
            table_entries += 1
        self.wellpage.page_refresh()
        self.teststatus.mark_final(self.wellpage.get_table_entries_count() == globalconfig.pagination_limit,
                                   "table rows match pagination limit")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_client_from_db")
    def test_client_pagination_limit_exceed_and_pagination_menu_exists(self):
        """FDMS-189
        insert bulk data such that pagination limit is exceeded then
        verify pagination menu exists
        """
        rows = getCSVData('tests/testdata/pagination/clientpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_client(row[0])
            table_entries += 1
        self.clientpage.page_refresh()
        result = self.clientpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_client_from_db")
    def test_client_pagination_limit_not_exceed_and_pagination_menu_doesnt_exist(self):
        """FDMS-189
        insert bulk data such that pagination limit is not exceeded then
        verify pagination menu doesnt exist
        """
        rows = getCSVData('tests/testdata/pagination/clientpaginationnotexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_client(row[0])
            table_entries += 1
        self.clientpage.page_refresh()
        result = not self.clientpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_client_from_db")
    def test_client_pagination_limit_exceed_and_table_has_rows_to_match_default_limit(self):
        """FDMS-189
        insert bulk data such that pagination limit is exceeded then
        ensure the number of rows in table match the default specified in config
        """
        rows = getCSVData('tests/testdata/pagination/clientpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_client(row[0])
            table_entries += 1
        self.clientpage.page_refresh()
        self.teststatus.mark_final(self.clientpage.get_table_entries_count() == globalconfig.pagination_limit,
                                   "table rows match pagination limit")

    @pytest.mark.usefixtures("clear_project_from_db")
    def test_project_pagination_limit_exceed_and_pagination_menu_exists(self):
        """FDMS-189
        insert bulk data such that pagination limit is exceeded then
        verify pagination menu exists
        """
        rows = getCSVData('tests/testdata/pagination/projectpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_project(row[0])
            table_entries += 1
        self.projectpage.page_refresh()
        result = self.projectpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_project_from_db")
    def test_project_pagination_limit_not_exceed_and_pagination_menu_doesnt_exist(self):
        """FDMS-189
        insert bulk data such that pagination limit is not exceeded then
        verify pagination menu doesnt exist
        """
        rows = getCSVData('tests/testdata/pagination/projectpaginationnotexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_project(row[0])
            table_entries += 1
        self.projectpage.page_refresh()
        result = not self.projectpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu doesnt shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_project_from_db")
    def test_project_pagination_limit_exceed_and_table_has_rows_to_match_default_limit(self):
        """FDMS-189
        insert bulk data such that pagination limit is exceeded then
        ensure the number of rows in table match the default specified in config
        """
        rows = getCSVData('tests/testdata/pagination/projectpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_project(row[0])
            table_entries += 1
        self.projectpage.page_refresh()
        self.teststatus.mark_final(self.projectpage.get_table_entries_count() == globalconfig.pagination_limit,
                                   "table rows match pagination limit")