# -------------------------------------------------------------------------------
# Database update workers 
# Reference : https://mariadb.com/docs/connectors/mariadb-connector-python/usage
# -------------------------------------------------------------------------------

import mariadb
import json
import sys
import requests

from mariadb.constants import *
class DBManager:
    def __init__(self):
        self.config = self.read_config()
        self.conn_params = self.config["database"]
        self.worker_types = self.config["worker_types"]
    def read_config(self):
        with open("config.json", 'r') as f:
            properties = json.load(f)
            return properties        
        
    # -------------------------------------------------------------------------------
    # Database Connection Functions
    # -------------------------------------------------------------------------------    
    def create_pool(self):
        # create new pool
        pool = mariadb.ConnectionPool(pool_name="dbPool", pool_size=5, **self.conn_params)
        print("Pool size of '%s': %s" % (pool.pool_name, pool.pool_size))
        return pool
    def get_connection(self):
        conn = self.pool.get_connection()
        return conn
    
    def task(self, thread_id, data_chunk, conn, query):
        cursor = conn.cursor
        try:
            for item in data_chunk:
                cursor.execute(query, item.values()) 
        except Exception as e:
            print(f"Thread {thread_id}: Error during update: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
            
            
    # -------------------------------------------------------------------------------
    #  Helper function to retrieve source data to populate db
    # ------------------------------------------------------------------------------
    def get_data(self, url):
        try:
            response = requests.get(url);
            print(f"Status Code: {response.status_code}")
            if response.status_code < 200 or response.status_code > 200:
                raise Exception(f"Url [{url}] returned invalid status code [{response.status_code}]")
            print(f"Response Text: {response.text}")
            data = response.json()
            print(f"Response JSON: {data}")
        except requests.exceptions.JSONDecodeError:
            print("Response is not valid JSON.")
        return data
    
    def read_data_from_worker_type(self, worker_index):
        return self.get_data(self.worker_types[worker_index]["data_source_url"])
        