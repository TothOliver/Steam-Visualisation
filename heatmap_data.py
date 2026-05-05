import pandas as pd
import ast

def prepare_heatmap_data(df, top_n=30):
    heatmap_df = create_heatmap_dataset(df)
    exploded_df = split_tags(heatmap_df)

    tag_counts = count_games(exploded_df)
    full_heatmap_matrix = create_heatmap_matrix(tag_counts)
    full_percentage_matrix = create_percentage_matrix(full_heatmap_matrix, heatmap_df)

    tag_totals = full_heatmap_matrix.sum(axis=0).sort_values(ascending=False)
    tags_by_frequency = tag_totals.index.tolist()
    default_tags = tag_totals.head(top_n).index.tolist()
    all_tags_sorted = sorted(full_heatmap_matrix.columns.tolist())


    default_heatmap_matrix = full_heatmap_matrix[default_tags]
    default_percentage_matrix = full_percentage_matrix[default_tags]

    return {
        "full_heatmap_matrix": full_heatmap_matrix,
        "full_percentage_matrix": full_percentage_matrix,
        "default_heatmap_matrix": default_heatmap_matrix,
        "default_percentage_matrix": default_percentage_matrix,
        "tags_by_frequency": tags_by_frequency,
        "default_tags": default_tags,
        "all_tags_sorted": all_tags_sorted
    }

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

def create_percentage_matrix(heatmap_matrix, df):
    games_per_year = (df.groupby("release_year")["appid"].nunique())

    percentage_matrix = heatmap_matrix.div(games_per_year, axis=0) * 100
    percentage_matrix = percentage_matrix.fillna(0)

    return percentage_matrix
