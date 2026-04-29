import pandas as pd

def load_steam_dataset(file_path):
    df = pd.read_csv(file_path)

    #print("\nDATASET SHAPE")
    #print(df.shape)
    #print("\nCOLUMN NAMES")
    #print(df.columns.tolist())
    #print("\nFIRST 5 ROWS")
    #print(df.head())
    #print("\nDATASET INFO")
    #df.info()
    #print("\nMISSING VALUES")
    #print(df.isna().sum().sort_values(ascending=False))

    return df

def create_heatmap_dataset(df):
    #no missing values for these
    heatmap_columns = [
        "appid",
        "name",
        "release_date",
        "genres"
    ]

    heatmap_df = df[heatmap_columns].copy()

    return heatmap_df