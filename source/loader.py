import pandas as pd

def load_facets(path: str):
    df = pd.read_csv(path)
    return df
