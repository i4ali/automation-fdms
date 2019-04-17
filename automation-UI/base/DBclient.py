"""
@ package base

The DB API is meant to provide a DB abstraction interface and deal with
different DB implementations(MongoDB or Postgres) providing a common user interface
to test classes

"""
from pydal import DAL, Field
import datetime
import uuid
import logging

# create logger
# logger = logging.getLogger('main.wdvg_edw_to_csv')

class DBClient:

    def __init__(self, uri_db):
        # logger.debug("creating instance of DBClient..")
        self.db = DAL(uri_db, migrate_enabled=False)
        self.wells = self.db.define_table('wells', Field('uuid'), Field('project_uuid'), Field('well_name'), Field('uwi'), Field('created_at'), Field('modified_at'), primarykey=['uuid'])
        self.clients = self.db.define_table('clients', Field('uuid'), Field('company_name'), Field('created_at'), Field('modified_at'), primarykey=['uuid'])
        self.projects = self.db.define_table('projects', Field('uuid'), Field('client_uuid'), Field('name'), Field('created_at'), Field('modified_at'), Field('basin'), Field('shapefile'), primarykey=['uuid'])

    def insert_well(self, *args):
        # logger.debug("inserting well into DB..")
        self.wells.insert(uuid=uuid.uuid4(), well_name=args[0], uwi=args[1], created_at=datetime.datetime.now(), modified_at=datetime.datetime.now())
        self.db.commit()

    def insert_client(self, *args):
        # logger.debug("inserting client into DB..")
        self.clients.insert(uuid=uuid.uuid4(), company_name=args[0], created_at=datetime.datetime.now(), modified_at=datetime.datetime.now())
        self.db.commit()

    # TODO insert project has been modified on the front end such that there is no field called project type on DB table
    # def insert_project(self, *args):
    #     self.insert_client(args[0])
    #     c_uuid = self.clients(company_name=args[0])['uuid']
    #     # self.db.projects.insert(uuid=uuid.uuid4(), name=args[1], client_uuid=c_uuid, basin='Midland', created_at=datetime.datetime.now(), modified_at=datetime.datetime.now())
    #     self.projects.insert(uuid=uuid.uuid4(), name=args[1], client_uuid=c_uuid, basin='midland', created_at=datetime.datetime.now(), modified_at=datetime.datetime.now())
    #     self.db.commit()

    def delete_table(self, tablename):
        # logger.debug("deleteing table {0}".format(tablename))
        table = self.db.get(tablename)
        table.truncate(mode='CASCADE')
        self.db.commit()

    def execute_sql(self, sql):
        # logger.debug("executing sql: '{0}'".format(sql))
        return self.db.executesql(sql)

    def close(self):
        # logger.debug("closing DB instance..")
        self.db.close()


if __name__ == '__main__':
    client = DBClient("postgres://service_toolkit_user:zMw1$ak85N^Zqa@toolkit-qa.cqztu6sln31x.us-east-1.rds.amazonaws.com:5432/service_toolkit_qa")
    print(client.db.tables)





