import webbrowser
from threading import Timer
from dash import Dash, dcc, html, Input, Output

from load_dataset import load_steam_dataset
from heatmap_data import prepare_heatmap_data
from heatmap_visalisation import create_tag_heatmap

def create_app():
    file_path = "Dataset/games_march2025_cleaned.csv"
    df = load_steam_dataset(file_path)
    
    heatmap_data = prepare_heatmap_data(df, top_n=30)
    
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            html.H1("Stream Tag Trends"),
            html.Label("Select Steam tags:"),
            dcc.Dropdown(
                id="tag-selector",
                options=[
                    {"label": tag, "value": tag}
                    for tag in heatmap_data["all_tags_sorted"]
                ],
                value=heatmap_data["default_tags"],
                multi=True,
                placeholder="Select tags to display..."
            ),
            dcc.Graph(id="tag-heatmap")
        ]
    )

    @app.callback(
        Output("tag-heatmap", "figure"),
        Input("tag-selector", "value")
    )

    def update_heatmap(selected_tags):
        if not selected_tags:
            selected_tags = heatmap_data["default_tags"]

        selected_tags = [
            tag for tag in selected_tags
            if tag in heatmap_data["full_heatmap_matrix"].columns
        ]

        filtered_heatmap_matrix = heatmap_data["full_heatmap_matrix"][selected_tags]
        filtered_percentage_matrix = heatmap_data["full_percentage_matrix"][selected_tags]

        fig = create_tag_heatmap(
            filtered_heatmap_matrix,
            filtered_percentage_matrix
        )

        return fig
    
    return app


if __name__ == "__main__":
    app = create_app()
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:8050/")).start()
    app.run(debug=True)