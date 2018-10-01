from pages.projects.project_page import ProjectPage
import unittest
from pymongo import MongoClient
from utilities.read_data import getCSVData
from ddt import ddt, data, unpack
from utilities.teststatus import TestStatus
from base.webdriverfactory import WebDriverFactory

@ddt
class ProjectPageTest(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def object_setup(self):
        self.wdf = WebDriverFactory("chrome")
        self.driver = self.wdf.getWebDriverInstance()
        self.teststatus = TestStatus(self.driver)
        self.landingpage = LandingPage(self.driver)

    def setUp(self):
        conn = MongoClient("mongodb://localhost:31001/")
        db = conn['service-fdms']
        project = db.get_collection('project')
        client = db.get_collection('client')
        project.delete_many({})
        client.delete_many({})


    def test_can_go_to_project_page(self):
        self.pp = ProjectPage("firefox")
        self.pp.goto()
        assert self.pp.isat()

    @data(*getCSVData('testdata/projecttestdatagood.csv'))
    @unpack
    def test_add_new_project(self, Projectname, Companyname, Wellname, APInumber):
        self.pp = ProjectPage("firefox")
        self.pp.goto()
        self.pp.addnewproject(Projectname, Companyname, Wellname, APInumber)
        assert self.pp.projectsuccessmessagepops()
        assert self.pp.projectexists(Projectname)