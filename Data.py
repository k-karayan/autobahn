import requests
import pandas as pd


class Data:

    def __init__(self):
        pass

    def api_request(self):
        payload = {'function': 'DIGITAL_CURRENCY_DAILY', 'symbol': 'BTC', 'market': 'USD', 'apikey': 'ZTATAV46GI7K6LJU'}
        data = requests.get('https://www.alphavantage.co/query', params=payload)

        return data.json()

    def data_transformation(self, json_data):
        actual_data = json_data['Time Series (Digital Currency Daily)']
        df_data = pd.DataFrame.from_dict(actual_data).transpose()
        df_data.index.name = 'Date'

        return df_data

    def data_to_csv(self, df_data, filename):
        df_data.to_csv(filename)

    def load_from_csv(self, filename):
        df_data = pd.read_csv(filename)

        return df_data