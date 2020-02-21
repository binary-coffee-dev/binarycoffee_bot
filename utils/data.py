from utils.data_adapters.json_adapter import JsonAdapter
from utils.data_adapters.mongodb_adapter import MongodbAdapter


def get_data_adapter(strategy='JsonAdapter',
                     data_path='',
                     database_url=None,
                     database_port=None,
                     database_name=None):
    if strategy == 'MongodbAdapter':
        database_name = 'bc_db' if database_name is None else database_name
        database_url = 'localhost' if database_url is None else database_url
        database_port = 27017 if database_port is None else database_port
        return MongodbAdapter(database_url=database_url, database_port=database_port, database_name=database_name)
    return JsonAdapter(data_storage_path=data_path)
