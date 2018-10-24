"""
@ package base

The DB API is meant to provide a DB abstraction interface and deal with
different DB implementations(MongoDB or Postgres) providing a common user interface
to test classes

"""
from pydal import DAL

class DBClient:

    def __init__(self, uri_db):
        self.db = DAL(uri_db, migrate_enabled=False)


    def delete_table(self, tablename):
        self.db.define_table(tablename)
        table = self.db.get(tablename)
        table.truncate(mode='CASCADE')
        self.db.commit()



if __name__ == '__main__':
   pass
