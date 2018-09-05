from datetime import datetime
import pandas as pd


class Calculations:

    def __init__(self):
        pass

    def append_week_info(self, df_data):
        """
        method that appends the number of week in a dataframe with date column
        :param df_data: the dataframe with data
        :return: the dataframe with the week numbers appended
        """
        weeks = []
        for date in df_data['Date']:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            year = date_obj.isocalendar()[0]
            weeknumber = date_obj.isocalendar()[1]
            info = str(year) + ' week ' + str(weeknumber)
            weeks += [info]

        df_data = pd.concat([df_data, pd.DataFrame(weeks, columns=['week'])], axis=1, join_axes=[df_data.index])

        return df_data

    def get_average_values(self, df_data):
        """
        method that calculates the average close price per week
        :param df_data: the dataframe with data
        :return: a dataframe with the average close prices
        """
        average_values = df_data.groupby('week').mean()
        average_values.columns = ['Average Close Price']

        return average_values

    def get_relative_spans(self, df_data):
        """
        method that calculates the relative span per week
        :param df_data: the dataframe with data
        :return: a dataframe with the relative spans
        """
        groups = df_data.groupby('week').agg({'4a. close (USD)': ['min', 'max']})
        groups['relative_span'] = (groups['4a. close (USD)']['max'] - groups['4a. close (USD)']['min']) \
                                  / groups['4a. close (USD)']['min']

        relative_spans = groups['relative_span']

        return relative_spans
