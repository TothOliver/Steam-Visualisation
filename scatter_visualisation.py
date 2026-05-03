import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

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