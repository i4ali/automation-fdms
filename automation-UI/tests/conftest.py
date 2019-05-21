"""
@package tests

conftest module for pytest to allow for reusable test fixtures
between all test cases

"""
from base.driver import Driver
from base.DBclient import DBClient
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


@pytest.yield_fixture()
def clear_well_from_db():
    """
    Connects to DB and removes the well collection from the database
    fdms. Teardowns client at the end
    """
    client = DBClient(globalconfig.postgres_conn_URI)
    client.delete_table('wells')
    yield
    client.close()


@pytest.yield_fixture()
def clear_client_from_db():
    """
    Connects to DB and removes the well collection from the database
    fdms. Teardowns client at the end
    """
    client = DBClient(globalconfig.postgres_conn_URI)
    client.delete_table('clients')
    yield
    client.close()


@pytest.yield_fixture()
def clear_project_from_db():
    """
    Connects to DB and removes the project, well and client collection from the database.
    Teardowns client at the end
    """
    client = DBClient(globalconfig.postgres_conn_URI)
    client.delete_table('projects')
    client.delete_table('clients')
    # client.delete_table('wells')
    yield
    client.close()
