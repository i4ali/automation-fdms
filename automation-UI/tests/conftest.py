"""
@package tests

conftest module for pytest to allow for reusable test fixtures
between all test cases

"""
from base.driver import Driver
import pytest
import globalconfig


@pytest.yield_fixture(scope="session", autouse=True)
def session_setup():
    """
    Obtains web driver instance from driver factory to be used by the tests for the entire
    session. The function is run twice as follows:
    a) once before the start of session
    b) after the end of session
    """
    driver = Driver.instance()
    yield
    driver.quit()


@pytest.fixture(autouse=True)
def method_setup():
    """
    Every test would start from the base url (landing page)
    """
    driver = Driver.instance()
    driver.get(globalconfig.base_url)
