import sqlite3
from databaseobjects.ddlstatements.dbcreation import *

class SqLiteConnector:
    _db_path_disk= "databaseobjects/gastrotour.db"
    _db_path_memory= ":memory:"

    def __init__(self):
        self.conn = sqlite3.connect(self._db_path_memory)

    def get_db_connection(self):
        cursor = self.conn.cursor()
        cursor.execute(create_dummy_table)
        cursor.execute(insert_dummy_value)
        self.conn.commit
        return self.conn
        
        


