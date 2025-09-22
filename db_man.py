# -------------------------------------------------------------------------------
# Database update workers 
# Reference : https://mariadb.com/docs/connectors/mariadb-connector-python/usage
# -------------------------------------------------------------------------------

import mariadb
import configparser

from mariadb.constants import *
class DBManager:
    def __init__(self, user, password, host, port, db):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.conn_params = {
                "user" : user,
                "password" : password,
                "host" : host,
                "port" : port,
                "database" : db
                }
                
    # create new pool
    with mariadb.ConnectionPool(pool_name="dbPool", pool_size=5, **conn_params) as pool:
        print("Pool size of '%s': %s" % (pool.pool_name, pool.pool_size))
        # get a connection from pool
        with pool.get_connection() as conn:
            # print the default database for connection
            print("Current database: %s" % conn.database)
