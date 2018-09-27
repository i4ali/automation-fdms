from pages.landing.landing_page import LandingPage
import unittest



class LandingPageTest(unittest.TestCase):

    def setUpClass(cls):
        pass

    def test_can_go_to_landing_page(self):
        self.lp = LandingPage("firefox")
        self.lp.goto()
        assert self.lp.isat()

    def test_add_new_well(self):
        self.lp = LandingPage("firefox")
        self.lp.goto()
        self.lp.addnewwell('test', '12')
        assert self.lp.wellsuccessmessagepops()
        assert self.lp.wellexists('test')

    def tearDownClass(cls):
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)


