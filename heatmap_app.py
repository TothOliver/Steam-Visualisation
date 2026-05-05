import webbrowser
from threading import Timer
from dash import Dash, dcc, html, Input, Output, ctx

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
            html.H1("Steam Tag Trends", style={"textAlign": "center"}),
            html.Div(
                children=[
                    #heatmap
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="tag-heatmap",
                                style={
                                    "height": "850px"
                                }
                            )
                        ],
                        style={
                            "width": "55%",
                            "display": "inline-block",
                            "verticalAlign": "top",
                            "paddingRight": "100px"
                        }
                    ),

                    #dropdown
                    html.Div(
                        children=[
                            html.H3("Tag Selection"),
                            html.Label("Select Steam tags:"),
                            html.Div(
                                children=[
                                    html.Button("Top 10", id="top-10-button", n_clicks=0, style={"flex": "1"}),
                                    html.Button("Top 20", id="top-20-button", n_clicks=0, style={"flex": "1"}),
                                    html.Button("Top 30", id="top-30-button", n_clicks=0, style={"flex": "1"}),
                                    html.Button("Top 40", id="top-40-button", n_clicks=0, style={"flex": "1"}),
                                ],
                                style={
                                    "display": "flex",
                                    "gap": "6px",
                                    "width": "100%",
                                    "marginBottom": "12px"
                                }
                            ),

                            dcc.Dropdown(
                                id="tag-selector",
                                options=[
                                    {"label": tag, "value": tag}
                                    for tag in heatmap_data["all_tags_sorted"]
                                ],
                                value=heatmap_data["default_tags"],
                                multi=True,
                                placeholder="Select tags to display...",
                                optionHeight=35,
                                maxHeight=500,
                                style={"width": "100%"}
                            )
                        ],
                        style={
                            "width": "30%",
                            "display": "inline-block",
                            "verticalAlign": "top",
                            "paddingLeft": "100px",
                            "paddingRight": "10px"
                        }
                    )
                ],
                style={"width": "100%"}
            )
        ],
        style={"padding": "20px"}
    )

    @app.callback(
        Output("tag-heatmap", "figure"),
        Input("tag-selector", "value"),
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
    
    @app.callback(
        Output("tag-selector", "value"),
        Input("top-10-button", "n_clicks"),
        Input("top-20-button", "n_clicks"),
        Input("top-30-button", "n_clicks"),
        Input("top-40-button", "n_clicks"),
        prevent_initial_call=True
    )
    def update_tag_selection(top_10, top_20, top_30, top_40):
        clicked_button = ctx.triggered_id
        print("Clicked button", clicked_button)

        if clicked_button == "top-10-button":
            return heatmap_data["tags_by_frequency"][:10]
        
        if clicked_button == "top-20-button":
            return heatmap_data["tags_by_frequency"][:20]
        
        if clicked_button == "top-30-button":
            return heatmap_data["tags_by_frequency"][:30]
        
        if clicked_button == "top-40-button":
            return heatmap_data["tags_by_frequency"][:40]

        return heatmap_data["default_tags"]

    return app


if __name__ == "__main__":
    app = create_app()
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:8050/")).start()
    app.run(debug=False)