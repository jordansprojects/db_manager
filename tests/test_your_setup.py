# This test is specifically for making sure your local configuration and mariadb install are able to interact,
# rather than a standard unit or integration test for developement purposes

import pytest
import json
from db_manager.db_man import DBManager
from db_manager.data_fetcher import DataFetcher

def get_config():
     with open("config.json", 'r') as f:
        properties = json.load(f)
        return properties

def test_connect_to_mariadb():
    print("*** Testing configuration and ability to connect to MariaDB ***")
    db = DBManager()

def test_fetch_data():
    print("Testing that your provided url(s) can be be fetched")
    num_workers = len(get_config()["worker_types"])
    df = DataFetcher()
    for i in range(num_workers):
        df.read_data_from_worker_type(i)