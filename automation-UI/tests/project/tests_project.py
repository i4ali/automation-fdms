from pages.projects.project_page import ProjectPage
import unittest


class ProjectPageTest(unittest.TestCase):


    def test_can_go_to_project_page(self):
        self.pp = ProjectPage("firefox")
        self.pp.goto()
        assert self.pp.isat()

    def test_add_new_project(self):
        self.pp = ProjectPage("firefox")
        self.pp.goto()
        self.pp.addnewproject('test8', 'test8', 'test8')
        assert self.pp.projectsuccessmessagepops()
        assert self.pp.projectexists('test8')