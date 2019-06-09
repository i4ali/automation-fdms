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
from pages.projects.projectdetails_page import ProjectDetailsPage
from pages.projects.projectaoi_page import ProjectAOIPage
from pages.clients.clientedit_page import ClientEditPage
from pages.clients.newclient_modal import NewClientModalPage
from pages.acreage.acreage_planner import AcreagePlanner
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
        self.newclientmodalpage = NewClientModalPage()
        self.acreageplannerpage = AcreagePlanner()
        self.projectdetailpage = ProjectDetailsPage()
        self.projectaoipage = ProjectAOIPage()

    """Tests"""
    @pytest.mark.regression
    @pytest.mark.smoketest
    def test_can_go_to_project_page(self):
        """
        Instanstiates project page and verifies the page can be reached
        successfully from the browser
        """
        result = self.projectpage.is_at()
        self.teststatus.mark_final(result, "can go to project page")

    @pytest.mark.regression
    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/projecttestdata.csv'))
    @unpack
    def test_add_new_project(self, projectname, companyname, basin):
        """FMDS-193
        Adds a new project to the database
        :param projectname: name of the project to be entered into the form
        :param companyname: client/company name to be entered into the form
        """
        self.projectpage.add_new_project(projectname, companyname, basin)
        result = self.projectpage.project_success_message_pops()
        self.teststatus.mark_final(result, "project success message pops")

    @pytest.mark.regression
    @pytest.mark.usefixtures("clear_project_from_db")
    def test_companyname_validation(self):
        """FDMS-182
        Validates the companyname field when adding a new project
        """
        self.projectpage.click_new_project()
        self.projecteditpage.click_create_project()
        result = self.projecteditpage.companyname_validation_message_shows()
        self.teststatus.mark_final(result, "verify validation message for company name")

    @pytest.mark.regression
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

    @pytest.mark.regression
    @pytest.mark.smoketest
    def test_create_new_client_link_on_new_project_page(self):
        """FDMS-193
        Validates that the create new company link works from the new project page
        """
        self.projectpage.click_new_project()
        self.projecteditpage.click_create_new_company()
        result = self.newclientmodalpage.is_at()
        self.teststatus.mark_final(result, "click new client link works from new project page")

    @pytest.mark.regression
    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/projecttestdata.csv'))
    @unpack
    def test_basin_exists_in_project_table(self, projectname, companyname, basin):
        """FDMS-668
        Checks that the basin name is shown in the project table after a new project is created
        """
        self.projectpage.add_new_project(projectname,companyname,basin)
        actual_basin = self.projectpage.get_basin_for_a_project_from_table(projectname)
        self.teststatus.mark_final(actual_basin == basin, "basin name exist in project table")

    @pytest.mark.regression
    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/projecttestdata.csv'))
    @unpack
    def test_load_shapefile_when_creating_project(self, projectname, companyname, basin):
        """
        Check that the shapefile is successfully loaded when creating a project
        """
        self.projectpage.add_new_project(projectname, companyname, basin)
        self.projectpage.go_to_project(projectname)
        self.projectaoipage.upload_acreage('tests/testdata/sable-shapefiles.zip')
        result = self.projectaoipage.upload_acreage_success_message_pops()
        self.teststatus.mark_final(result, "project acreage upload success message pops")

    @pytest.mark.regression
    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/projecttestdata.csv'))
    @unpack
    def test_delete_project(self, projectname, companyname, basin):
        """
        Deletes a project and checks the toast message for success
        """
        self.projectpage.add_new_project(projectname, companyname, basin)
        self.projectpage.delete_project(projectname)
        result = self.projectpage.project_delete_success_message_pops()
        self.teststatus.mark_final(result, "project delete success message pops")

    @pytest.mark.regression
    @pytest.mark.usefixtures("clear_project_from_db")
    @data(*getCSVData('tests/testdata/projecttestdata.csv'))
    @unpack
    def test_view_project(self, projectname, companyname, basin):
        """
        Clicks on view project after adding that project. Then checks that view project
        takes to the project details page
        """
        self.projectpage.add_new_project(projectname, companyname, basin)
        self.projectpage.click_view_project(projectname)
        result = self.projectdetailpage.is_at()
        self.teststatus.mark_final(result, "view project goes to project")
