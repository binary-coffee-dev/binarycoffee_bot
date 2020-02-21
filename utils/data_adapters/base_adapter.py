from abc import abstractmethod


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
