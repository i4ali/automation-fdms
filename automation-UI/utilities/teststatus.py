"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from base.webdriver import SeleniumWebDriver
from traceback import print_stack

class TestStatus:


    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        # super(TestStatus, self).__init__()
        self.driver = SeleniumWebDriver(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                else:
                    self.resultList.append("FAIL")
                    self.driver.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.driver.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.driver.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.resultList.clear()
            assert True == False
        else:
            self.resultList.clear()
            assert True == True
