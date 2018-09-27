from pages.landing.landing_page import LandingPage
import unittest


class LandingPageTest(unittest.TestCase):

    def test_can_go_to_landing_page(self):
        self.lp = LandingPage()
        self.lp.goto()
        assert self.lp.isat()

    def test_new_project_button_exists(self):
        self.lp = LandingPage()
        self.lp.goto()
        assert self.lp.newprojectbuttonexists()

    def test_validate_add_new_project_window_fields(self):
        self.lp = LandingPage()
        self.lp.goto()
        self.lp.clicknewprojectbutton()
        assert self.lp.validatenewprojectfields('Project Name', 'Company Name', 'Well Name', 'UWI / API Number')

    @unittest.skip("WIP")
    def test_add_new_project(self):
        self.lp = LandingPage()
        self.lp.goto()
        self.lp.addnewproject('test4', 'test4', 'test4')
        #assert lp.projectexists()



if __name__ == '__main__':
    unittest.main(verbosity=2)


