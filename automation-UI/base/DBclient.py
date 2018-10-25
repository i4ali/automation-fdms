"""
@ package base

The DB API is meant to provide a DB abstraction interface and deal with
different DB implementations(MongoDB or Postgres) providing a common user interface
to test classes

"""
from pydal import DAL, Field
import datetime
import uuid

class DBClient:

    def __init__(self, uri_db):
        self.db = DAL(uri_db, migrate_enabled=False)
        self.db.define_table('wells', Field('uuid'), Field('project_uuid'), Field('well_name'), Field('uwi'), Field('created_at'), Field('modified_at'), primarykey=['uuid'])

    def insert_well(self, *args):
        self.db.wells.insert(uuid=uuid.uuid4(), well_name=args[0], uwi=args[1], created_at=datetime.datetime.now(), modified_at=datetime.datetime.now())
        self.db.commit()

    def insert_project(self, *args):
        raise NotImplementedError

    def delete_table(self, tablename):
        table = self.db.get(tablename)
        table.truncate(mode='CASCADE')
        self.db.commit()



if __name__ == '__main__':
   pass
