from utils.data_adapters.base_adapter import DataAdapter


class MemoryAdapter(DataAdapter):
    def __init__(self):
        self.data = []
        self.data_map = {}

    def add_and_get_new_items(self, items=None):
        if items is None:
            return []
        new_items = []
        for it in items:
            if self.data_map.get(it['id'], -1) == -1:
                new_items.append(it)

        if len(self.data) > 0:
            self.data = items
            self.calculate_data_map()
        else:
            self.data = items
            return []

        new_items.sort(key=lambda item: item['date_modified'], reverse=False)
        return new_items

    def calculate_data_map(self):
        self.data_map = {}
        for i in range(len(self.data)):
            it = self.data[i]
            self.data_map[it['id']] = i

    def save_data(self):
        pass

    def load_data(self):
        pass
