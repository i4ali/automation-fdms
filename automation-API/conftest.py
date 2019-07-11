import pytest
from DBclient import DBClient


@pytest.fixture
def clean_tables_from_db():
    client = DBClient("postgres://service-toolkit-user:JgR6zYpVmsny@toolkit-qa.cqztu6sln31x.us-east-1.rds.amazonaws.com:5432/service-toolkit-qa")
    client.delete_table('projects')
    client.delete_table('clients')
    yield
    client.close()