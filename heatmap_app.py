from dash import Dash, dcc, html

from load_dataset import load_steam_dataset
from heatmap_data import prepare_heatmap_data
from heatmap_visalisation import create_tag_heatmap

def create_app():
    file_path = "Dataset/games_march2025_cleaned.csv"
    df = load_steam_dataset(file_path)
    
    heatmap_data = prepare_heatmap_data(df, top_n=30)

    fig1 = create_tag_heatmap(
        heatmap_data["default_heatmap_matrix"], 
        heatmap_data["default_percentage_matrix"]
    )
    
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            html.H1("Stream Tag Trends"),
            dcc.Graph(id="tag-heatmap", figure=fig1)
        ]
    )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)