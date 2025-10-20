# -------------------------------------------------------------------------------
# Retreives data via GET request 
# -------------------------------------------------------------------------------
import requests
import json

class DataFetcher:
    def __init__(self):
        pass # Nothing to add here yet
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
        with open("config.json", 'r') as f:
            workers = json.load(f)["worker_types"]
            return self.get_data(workers[worker_index]["data_source_url"])
             

            
    