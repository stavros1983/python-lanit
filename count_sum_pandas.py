import pandas as pd


def count_sum(data):
    return pd.DataFrame(data.groupby('Товар')['Количество'].sum())