# -------------------------------------------------------------------------------
# Run database update workers 
# -------------------------------------------------------------------------------

from db_manager.db_man import DBManager
from db_manager.data_fetcher import DataFetcher

df = DataFetcher()
manager = DBManager()

def worker_task(thead_id, data_chunk):