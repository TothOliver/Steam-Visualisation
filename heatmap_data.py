import pandas as pd
import ast

def create_heatmap_dataset(df):
    #no missing values for these
    heatmap_columns = [
        "appid",
        "name",
        "release_date",
        "genres",
        "tags"
    ]

    heatmap_df = df[heatmap_columns].copy()

    heatmap_df["release_date"] = pd.to_datetime(
        heatmap_df["release_date"],
        errors="coerce"
    )
    heatmap_df["release_year"] = heatmap_df["release_date"].dt.year

    return heatmap_df

def split_genres(df):
    df = df.copy()
    
    df["genre_list"] = df["genres"].apply(ast.literal_eval) 

    exploded_df = df.explode("genre_list")

    exploded_df = exploded_df.rename(columns={
        "genre_list": "genre"
    })

    exploded_df = exploded_df.dropna(subset="genre")

    return exploded_df