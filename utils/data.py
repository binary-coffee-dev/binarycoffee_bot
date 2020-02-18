from abc import abstractmethod
from os import path
from pathlib import Path

import json


class DataAdapter:
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def add_and_get_new_items(self, items):
        pass

    @staticmethod
    def check_path(path_name):
        Path(path_name).mkdir(parents=True, exist_ok=True)


class JsonData(DataAdapter):
    def __init__(self, data_storage_path, data_file_name='data.json'):
        self.check_path(data_storage_path)
        self.data_storage_path = path.join(data_storage_path, data_file_name)
        self.data = []
        self.data_map = {}
        self.load_data()
        self.calculate_data_map()

    def calculate_data_map(self):
        self.data_map = {}
        for i in range(len(self.data)):
            it = self.data[i]
            self.data_map[it['id']] = i

    def add_and_get_new_items(self, items=[]):
        new_items = []
        for it in items:
            if self.data_map.get(it['id'], -1) == -1:
                self.data.append(it)
                new_items.append(it)
        if len(new_items) > 0:
            self.calculate_data_map()
            self.save_data()
        return new_items

    def save_data(self):
        with open(self.data_storage_path, 'w+') as database:
            database.write(str(self.data))

    def load_data(self):
        self.data = []
        try:
            file = open(self.data_storage_path, 'r')
            data = file.read().replace("'", '"')
            if len(data) > 0:
                self.data = json.loads(data)
            file.close()
        except:
            pass


def get_data_adapter(strategy='JsonData', data_path=''):
    return JsonData(data_storage_path=data_path)
