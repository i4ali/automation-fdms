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

    def setResult(self, result,  resultMessage, expectedresult):
        try:
            if result is not None:
                if result == expectedresult:
                    self.resultList.append("PASS")
                else:
                    self.resultList.append("FAIL")
                    self.driver.screenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.driver.screenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.driver.screenshot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage, expectedresult="pass"):
        """
        Mark the result of the verification point in a test case
        """
        if expectedresult.strip().lower() == "pass":
            expectedresult = True
        else:
            expectedresult = False
        self.setResult(result, resultMessage, expectedresult)

    def markFinal(self, result, resultMessage, expectedresult="pass"):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        if expectedresult.strip().lower() == "pass":
            expectedresult = True
        else:
            expectedresult = False
        self.setResult(result, resultMessage, expectedresult)

        if "FAIL" in self.resultList:
            # print(self.resultList)
            self.resultList.clear()
            assert True == False
        else:
            self.resultList.clear()
            assert True == True