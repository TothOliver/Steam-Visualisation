import pandas as pd

def load_steam_dataset(file_path):
    df = pd.read_csv(file_path)

    #check_dataset(df)

    return df

def check_dataset(df):
    print("\nDATASET SHAPE")
    print(df.shape)
    print("\nCOLUMN NAMES")
    print(df.columns.tolist())
    print("\nFIRST 5 ROWS")
    print(df.head())
    print("\nDATASET INFO")
    df.info()
    print("\nMISSING VALUES")
    print(df.isna().sum().sort_values(ascending=False))