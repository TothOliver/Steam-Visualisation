import pandas as pd

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