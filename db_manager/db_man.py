# -------------------------------------------------------------------------------
# Database update workers 
# Reference : https://mariadb.com/docs/connectors/mariadb-connector-python/usage
# -------------------------------------------------------------------------------


# TO-DO : Write something that tries to connect to mariadb - if it fails exit the program
# TO-DO : Makes sure multiple threads are running per command 


import mariadb
import json
import sys

from mariadb.constants import *
class DBManager:
    def __init__(self):
        self.conn_params = self.read_config()["database"]
        try:
           self.pool = self.create_pool()
        except Exception as e :
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    
    def read_config(self):
        with open("config.json", 'r') as f:
            properties = json.load(f)
            return properties
    def create_pool(self):
        # create new pool
        pool = mariadb.ConnectionPool(pool_name="dbPool", pool_size=5, **self.conn_params)
        print("Pool size of '%s': %s" % (pool.pool_name, pool.pool_size))
        return pool

        
        