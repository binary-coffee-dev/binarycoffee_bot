from pymongo import MongoClient

from utils.data_adapters.base_adapter import DataAdapter


class MongodbAdapter(DataAdapter):
    def __init__(self, database_url='http://localhost', database_port=27017, database_name='bc_db'):
        self.database_url = database_url
        self.database_port = database_port
        self.database_name = database_name
        self.client = MongoClient(host=database_url, port=database_port)
        self.db = self.client[database_name]

    def add_and_get_new_items(self, items=None):
        new_items = []
        for item in items:
            exist = self.db['items'].find({'id': item.get('id')}).count() > 0
            if not exist:
                new_items.append(item)
        for item in new_items:
            self.db.get_collection('items').insert_one(item)
        return new_items

    def save_data(self):
        pass

    def load_data(self):
        pass
