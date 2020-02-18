from abc import abstractmethod
from pathlib import Path


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
