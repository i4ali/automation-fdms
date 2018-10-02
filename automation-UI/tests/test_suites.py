import unittest
from tests.landing.tests_landing import LandingPageTest
from tests.project.tests_project import ProjectPageTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LandingPageTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ProjectPageTest)


smoke_test = unittest.TestSuite([tc1, tc2])
# #TODO
# # regression_test
#
# #unittest.TextTestRunner(verbosity=2).run(smoke_test)