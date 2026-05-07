import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

def create_scatter(df, selected_tags):

    filtered_df = df[
    df["tags"].apply(
        lambda game_tags:
        all(tag in game_tags for tag in selected_tags)
    )
    ]

    if filtered_df.empty:
        return px.scatter(title="No data for selected tags")

    fig = px.scatter(
        filtered_df,
        x="price",
        y="popularity",
        hover_data=["name"],
        title="Price vs Popularity (Top Tags)",
        opacity=0.6
    )

    fig.update_layout(width=1000, height=600)
    fig.update_yaxes(type="log")

    return fig