from sklearn import preprocessing
import pandas as pd


def readcsv(filename):
    return pd.read_csv(filename)


def normalize(df):
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(df)
    df_normalized = pd.DataFrame(x_scaled)
    return df_normalized


def get_stock(data):
    return data[data.columns[2]]


def get_total_gdp(data):
    return data[data.columns[10]]
