from Data import Data
from Calculations import Calculations

## LOAD DATA - SAVE TO CSV
data = Data()

json_data = data.api_request()
df_data = data.data_transformation(json_data)
data.data_to_csv(df_data, filename='files/cryptocurrency_daily_data.csv')
print 'Data saved in files/cryptocurrency_daily_data.csv'

## CALCULATIONS
calculations = Calculations()

cryptocurrency_data = data.load_from_csv('files/cryptocurrency_daily_data.csv')
print 'Loaded data from files/cryptocurrency_daily_data.csv'

# close prices
close_prices = cryptocurrency_data[['Date', '4a. close (USD)']]
close_prices = calculations.append_week_info(close_prices)

average_closes = calculations.get_average_values(close_prices)
data.data_to_csv(average_closes, 'files/average_close_prices.csv')
print 'Average close prices saved in files/cryptocurrency_daily_data.csv'

# relative spans
relative_spans = calculations.get_relative_spans(close_prices)
print 'The week with minimum relative span is: ' + relative_spans.idxmin(axis=1)