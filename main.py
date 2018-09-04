from pprint import pprint
from Data import Data


data = Data()
json_data = data.api_request()
df_data = data.data_transformation(json_data)
data.data_to_csv(df_data, filename='cryptocurrency_daily_data.csv')