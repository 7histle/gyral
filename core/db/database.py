# singleton for realization of driver
class DBDriver():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            # create configuration object
            from conf import Config
            conf = Config()
            # get name of database driver from config
            module = __import__('core.db.drivers.'+conf.dbdriver, fromlist=[conf.dbdriver])
            drv = getattr(module, conf.dbdriver)
            # create a object of database driver class
            opt = {}
            opt['dbdriver'] = conf.dbdriver;
            opt['dbuser'] = conf.dbuser;
            opt['dbpass'] = conf.dbpass;
            opt['dbhost'] = conf.dbhost;
            opt['dbname'] = conf.dbname;
            opt['dbprefix'] = conf.dbprefix;
            opt['dbtrace'] = conf.dbtrace;
            d = drv(opt)
            cls.instance = super(drv, d).__new__(drv)
            # initiate a connection
            cls.instance.__init__(opt)
        return cls.instance

# database core functions
class DataBase():
    def __init__(self):
        # get database driver object
        self.drv = DBDriver()

    def initBase(self):
        query = "CREATE TABLE IF NOT EXISTS sample(value TEXT)"
        self.drv.run(query)
        self.drv.commit()
        return True
        
    def insertSample(self,val):
        query = "INSERT INTO sample VALUES (?)" # maybe orm?
        self.drv.run(query,(val,))
        self.drv.commit()
        return True

    def getSample(self):
        query = "SELECT * FROM sample"
        self.drv.run(query)
        self.drv.commit()
        return self.drv.getAll()
