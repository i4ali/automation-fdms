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
from utilities.statustest import StatusTest
from utilities.read_data import getCSVData
from pages.wells.well_page import WellPage
from pages.projects.project_page import ProjectPage
from pages.projects.projectedit_page import ProjectEditPage
import globalconfig
from base.DBclient import DBClient


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

        test_add_new_project(Projectname, Companyname, Wellname, APInumber)
            Verify that new well can be added using the appropriate format for Projectname,
            Companyname, Wellname, APInumber and validating the form entries

        test_wellname_validation(wellname, validationmessage)
            Validate the wellname field of the new well form

        test_apiname_validation(apiname, validationmessage)
            Validate the apiname field of the new well form

        """

    @pytest.fixture(autouse=True)
    def object_setup(self):
        """
        Instantiates ProjectPage, TestStatus instance to be used by the test class
        The function is run before every test function is called
        """
        self.teststatus = StatusTest()
        self.wellpage = WellPage()
        self.projectpage = ProjectPage()
        self.projecteditpage = ProjectEditPage()

    @pytest.fixture()
    def clear_project_from_db(self):
        """
        Connects to MongoDB and removes the project, well and client collection from the database
        service-fdms
        """
        self.client = DBClient(globalconfig.postgres_conn_URI)
        self.client.delete_table('projects')
        self.client.delete_table('clients')
        self.client.delete_table('wells')

    @pytest.mark.smoketest
    def test_can_go_to_project_page(self):
        """
        Instanstiates wells page and verifies the page can be reached
        successfully from the browser
        """
        result = self.projectpage.is_at()
        self.teststatus.mark_final(result, "can go to project page")

    @pytest.mark.inprogress
    @pytest.mark.smoketest
    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/projecttestdata.csv'))
    @unpack
    def test_add_new_project(self, projectname, companyname):
        """
        Adds a new well to the database
        :param wellname: name of the well to be entered into the form
        :param apinumber: api number to be entered into the form
        :param projectname: project name to entered into the form
        :param companyname: client/company name to be entered into the form
        :param expectedresult: expected result Pass or Fail
        """
        self.projectpage.add_new_project(projectname, companyname)
        result = self.projectpage.project_success_message_pops()
        self.teststatus.mark_final(result, "project success message pops")

    @pytest.mark.usefixtures("clear_project_from_db")
    def test_companyname_validation(self):
        """FDMS-182
        Validates the apiname field when adding a new project
        :param apiname: apiname to be entered into the form
        :param validationmessage: the expected validation message
        """
        self.projectpage.click_new_project()
        self.projecteditpage.click_create_project()
        result = self.projecteditpage.companyname_validation_message_shows()
        self.teststatus.mark_final(result, "verify validation message for company name")

    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/validation/projectnamevalidation.csv'))
    @unpack
    def test_projectname_validation(self, projectname, validationmessage):
        """FDMS-182
        Validates the apiname field when adding a new project
        :param apiname: apiname to be entered into the form
        :param validationmessage: the expected validation message
        """
        self.projectpage.click_new_project()
        self.projecteditpage.enter_project_name(projectname)
        self.projecteditpage.click_create_project()
        self.teststatus.mark_final(validationmessage == self.projecteditpage.get_validation_message_projectname(), "project name validation")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_project_from_db")
    def test_project_pagination_limit_exceed_and_pagination_menu_exists(self):
        # insert bulk data such that pagination limit is exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/projectpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_project(row[0])
            table_entries += 1
        # verify pagination menu exists
        self.projectpage.page_refresh()
        result = self.projectpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_project_from_db")
    def test_well_pagination_limit_not_exceed_and_pagination_menu_doesnt_exist(self):
        # insert bulk data such that pagination limit is not exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/projectpaginationnotexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_project(row[0])
            table_entries += 1
        # verify pagination menu doesnt exists
        self.projectpage.page_refresh()
        result = not self.projectpage.pagination_menu_exists()
        self.teststatus.mark_final(result, "check the pagination menu doesnt shows up")

    @pytest.mark.pagination
    @pytest.mark.usefixtures("clear_project_from_db")
    def test_well_pagination_limit_exceed_and_table_has_rows_to_match_default_limit(self):
        # insert bulk data such that pagination limit is exceeded
        self.client = DBClient(globalconfig.postgres_conn_URI)
        rows = getCSVData('tests/testdata/pagination/projectpaginationexceed.csv')
        table_entries = 0
        for row in rows:
            self.client.insert_project(row[0])
            table_entries += 1
        self.projectpage.page_refresh()
        self.teststatus.mark_final(self.projectpage.get_table_entries_count() == globalconfig.pagination_limit,
                                   "table rows match pagination limit")


    # @pytest.mark.usefixtures("clear_well_from_db")
    # @data(*getCSVData('testdata/projectnamevalidation.csv'))
    # @unpack
    # def test_project_name_validation(self, wellname, apinumber, validationmessage):
    #     """FDMS-183"""
    #     pass
