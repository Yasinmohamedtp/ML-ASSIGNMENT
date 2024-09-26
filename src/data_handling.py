# data_handling.py
import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the provided file path.
    """
    return pd.read_csv(file_path)

def save_data(df, file_path):
    """
    Save the dataframe to the given file path.
    """
    df.to_csv(file_path, index=False)
