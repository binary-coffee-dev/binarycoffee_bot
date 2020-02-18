from utils.data_adapters.json_adapter import JsonAdapter


def get_data_adapter(strategy='JsonAdapter', data_path=''):
    return JsonAdapter(data_storage_path=data_path)
