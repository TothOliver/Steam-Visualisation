import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

def create_scatter(df, selected_tags, price_range):

    min_price, max_price = price_range

    filtered_df = df[
        df["tags"].apply(
            lambda game_tags:
            all(tag in game_tags for tag in selected_tags)
        )
    ]

    filtered_df = filtered_df[
        (filtered_df["price"] >= min_price) &
        (filtered_df["price"] <= max_price)
    ]

    if filtered_df.empty:
        return px.scatter(title="No matching games")

    fig = px.scatter(
        filtered_df,
        x="price",
        y="popularity",
        hover_data=["name"],
        title="Price vs Popularity",
        opacity=0.6,
        labels={
            "price": "Price (Euro)",
            "popularity": "Popularity (Number of Reviews)"
        }
    )

    fig.update_layout(width=1000, height=600)
    fig.update_yaxes(type="log")

    return fig