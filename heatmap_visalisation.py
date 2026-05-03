import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

def create_genre_heatmap(heatmap_matrix):
    fig = px.imshow(
        heatmap_matrix,
        labels={
            "x": "Tags",
            "y": "Release Year",
            "color": "Number of Games"
        },
        title="Heatmap Steam Games Tags",
        aspect="auto",
        color_continuous_scale="YlOrRd"
    )

    fig.update_layout(width=1200, height=800)

    return fig

def create_scatter(filtered_df):

    if filtered_df.empty:
        return px.scatter(title="No data for selected tags")

    fig = px.scatter(
        filtered_df,
        x="price",
        y="popularity",
        color="tag",
        hover_data=["name"],
        title="Price vs Popularity (Top Tags)",
        opacity=0.6
    )

    fig.update_layout(width=1000, height=600)
    fig.update_yaxes(type="log")

    return fig
