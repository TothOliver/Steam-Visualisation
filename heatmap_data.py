import pandas as pd
import ast

def create_heatmap_dataset(df):
    #no missing values for these
    heatmap_columns = [
        "appid",
        "name",
        "release_date",
        "tags"
    ]

    heatmap_df = df[heatmap_columns].copy()

    heatmap_df["release_date"] = pd.to_datetime(
        heatmap_df["release_date"],
        errors="coerce"
    )
    heatmap_df["release_year"] = heatmap_df["release_date"].dt.year

    return heatmap_df

def create_heatmap_matrix(df):
    heatmap_matrix = df.pivot(
        index="release_year",
        columns="tag",
        values="game_count"
    )

    heatmap_matrix = heatmap_matrix.fillna(0)
    return heatmap_matrix


def split_tags(df):
    df = df.copy()

    df["tag_dict"] = df["tags"].apply(ast.literal_eval) 

    exploded_df = df.explode("tag_dict")

    exploded_df = exploded_df.rename(columns={
        "tag_dict": "tag"
    })

    exploded_df = exploded_df.dropna(subset=["tag"])

    return exploded_df

def count_games(df):
    genre_counts = (
        df.groupby(["release_year", "tag"]).size().reset_index(name="game_count")
    )

    return genre_counts

def filter_top_tags(heatmap_matrix, top_n=30):
    tag_totals = heatmap_matrix.sum(axis=0)

    top_tags = (
        tag_totals
        .sort_values(ascending=False)
        .head(top_n)
        .index
    )

    filtered_matrix = heatmap_matrix[top_tags]

    return filtered_matrix

def create_scatter_dataset(df):
    scatter_columns = [
        "appid",
        "name",
        "price",
        "tags",
        "num_reviews_total"
    ]

    scatter_df = df[scatter_columns].copy()

    scatter_df["price"] = pd.to_numeric(scatter_df["price"], errors="coerce")

    scatter_df["popularity"] = (
        scatter_df["num_reviews_total"] 
    )

    scatter_df = scatter_df[
    (scatter_df["price"] > 0) &
    (scatter_df["popularity"] > 10)
    ]

    return scatter_df

def count_tags(df):
    return (
        df.groupby("tag")
        .size()
        .reset_index(name="game_count")
    )

def filter_top_tags_scatter(df, top_n=30):

    tag_counts = count_tags(df)

    top_tags = (
        tag_counts
        .sort_values(by="game_count", ascending=False)
        .head(top_n)["tag"]
    )

    filtered_df = df[df["tag"].isin(top_tags)]

    return filtered_df