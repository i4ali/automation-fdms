"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from base.seleniumwebdriver import SeleniumWebDriver
from traceback import print_stack

class StatusTest:

    def __init__(self):
        """
        Inits CheckPoint class
        """
        # super(TestStatus, self).__init__()
        self.driver = SeleniumWebDriver()
        self.resultList = []

    def set_result(self, result, resultMessage):
        if result is not None:
            if result:
                self.resultList.append("PASS")
            else:
                self.resultList.append("FAIL")
        else:
            self.resultList.append("FAIL")
            self.driver.screenshot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, resultMessage)

    def mark_final(self, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, resultMessage)

        if "FAIL" in self.resultList:
            self.resultList.clear()
            assert True == False
        else:
            self.resultList.clear()
            assert True == True
