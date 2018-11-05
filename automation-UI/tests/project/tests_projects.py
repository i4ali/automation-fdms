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
from pages.clients.clientedit_page import ClientEditPage
import globalconfig
from base.DBclient import DBClient


@ddt
class TestProjects(unittest.TestCase):

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
        self.clienteditpage = ClientEditPage()

    @pytest.fixture()
    def clear_project_from_db(self):
        """
        Connects to DB and removes the project, well and client collection from the database
        """
        self.client = DBClient(globalconfig.postgres_conn_URI)
        self.client.delete_table('project')
        self.client.delete_table('client')
        self.client.delete_table('well')

    @pytest.mark.smoketest
    def test_can_go_to_project_page(self):
        """
        Instanstiates project page and verifies the page can be reached
        successfully from the browser
        """
        result = self.projectpage.is_at()
        self.teststatus.mark_final(result, "can go to project page")

    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/projecttestdata.csv'))
    @unpack
    def test_add_new_project(self, projectname, companyname):
        """FMDS-193
        Adds a new project to the database
        :param projectname: name of the project to be entered into the form
        :param companyname: client/company name to be entered into the form
        """
        self.projectpage.add_new_project(projectname, companyname)
        result = self.projectpage.project_success_message_pops()
        self.teststatus.mark_final(result, "project success message pops")

    @pytest.mark.usefixtures("clear_project_from_db")
    def test_companyname_validation(self):
        """FDMS-182
        Validates the companyname field when adding a new project
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
        :param projectname: apiname to be entered into the form
        :param validationmessage: the expected validation message
        """
        self.projectpage.click_new_project()
        self.projecteditpage.enter_project_name(projectname)
        self.projecteditpage.click_create_project()
        self.teststatus.mark_final(validationmessage == self.projecteditpage.get_validation_message_projectname(), "project name validation")

    @pytest.mark.smoketest
    def test_create_new_company_link_on_new_project_page(self):
        """FDMS-193
        Validates that the create new company link works from the new project page
        """
        self.projectpage.click_new_project()
        self.projecteditpage.click_create_new_company()
        result = self.clienteditpage.is_at()
        self.teststatus.mark_final(result, "click new client link works from new project page")





    # @pytest.mark.usefixtures("clear_well_from_db")
    # @data(*getCSVData('testdata/projectnamevalidation.csv'))
    # @unpack
    # def test_project_name_validation(self, wellname, apinumber, validationmessage):
    #     """FDMS-183"""
    #     pass
