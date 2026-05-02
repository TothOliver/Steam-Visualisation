import plotly.express as px

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