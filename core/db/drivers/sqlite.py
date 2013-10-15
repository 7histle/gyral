import sqlite3
from core.syspath import syspath

class sqlite:
    
    cursor = None
    
    def __init__(self,opt):
        # database file in root folder
        self.conn = sqlite3.connect(syspath.BASE_PATH+syspath.DS+opt['dbprefix']+opt['dbname'])
        if(opt['dbtrace']):
            # enable error reporting
            sqlite3.enable_callback_tracebacks(True)
        
    def run(self,query,t=()):
        self.cursor = self.conn.cursor()
        self.cursor.execute(query,t)
        return True
    
    def commit(self):
        self.conn.commit()
        return True
        
    def rollback(self):
        self.conn.rollback()
        return True
    
    def close(self):
        self.conn.close()
        return True
    
    def getFirst(self):
        return self.cursor.fetchone()[0]
        
    def getAll(self):
        return self.cursor.fetchall()
        
    
