import pandas as pd

def read_csv_file(path: str, chunk_size: int = 5000):
    return pd.read_csv(path, chunksize=chunk_size)
