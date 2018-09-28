from pages.landing.landing_page import LandingPage
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pymongo import MongoClient

@ddt
class LandingPageTest(unittest.TestCase):

    def setUp(self):
        conn = MongoClient("mongodb://localhost:31001/")
        db = conn['service-fdms']
        well = db.get_collection('well')
        well.delete_many({})

    def test_can_go_to_landing_page(self):
        self.lp = LandingPage("firefox")
        self.lp.goto()
        assert self.lp.isat()

    @data(*getCSVData('testdata/welltestdata.csv'))
    @unpack
    def test_add_new_well(self, wellname, apinumber):
        self.lp = LandingPage("firefox")
        self.lp.goto()
        self.lp.addnewwell(wellname, apinumber)
        assert self.lp.wellsuccessmessagepops()
        assert self.lp.wellexists(wellname)

    # @data(*getCSVData('../../testdata/welltestdata.csv'))
    # @unpack
    # @unittest.skip("WIP")
    # def test_rem_well(self, wellname, apinumber):
    #     self.lp = LandingPage("firefox")
    #     self.lp.goto()
    #     self.lp.addnewwell(wellname, apinumber)
    #     assert self.lp.wellsuccessmessagepops()
    #     assert self.lp.wellexists(wellname)
    #     self.lp.removewell(wellname)
    #     assert self.lp.welldoesntexist(wellname)


if __name__ == '__main__':
    unittest.main(verbosity=2)


