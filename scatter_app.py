import webbrowser
from threading import Timer
from dash import Dash, dcc, html, Input, Output, ctx

from load_dataset import load_steam_dataset
from scatter_data import prepare_scatter_data
from scatter_visualisation import create_scatter

def create_app():
    file_path = "Dataset/games_march2025_cleaned.csv"
    df = load_steam_dataset(file_path)

    scatter_data = prepare_scatter_data(df, top_n=1)

    app = Dash(__name__)
    
    app.layout = html.Div(
        children=[
            html.H1("Price - Popularity Scatter", style={"textAlign": "center"}),
            html.Div(
                children=[
                    #heatmap
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="scatter-plot",
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

                            dcc.Dropdown(
                                id="tag-selector",
                                options=[
                                    {"label": tag, "value": tag}
                                    for tag in scatter_data["all_tags_sorted"]
                                ],
                                value=scatter_data["default_tags"],
                                multi=True,
                                placeholder="Select tags to display...",
                                optionHeight=35,
                                maxHeight=500,
                                style={"width": "100%"}
                            ),
                            html.Br(),
                            html.Label("Price Range"),
                            dcc.RangeSlider(
                                id="price-slider",
                                min=0,
                                max=100,
                                step=1,
                                value=[0, 100],

                                marks={
                                    0: "0",
                                    20: "20",
                                    40: "40",
                                    60: "60",
                                    80: "80",
                                    100: "100"
                                },

                                tooltip={"placement": "bottom"}
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
    Output("scatter-plot", "figure"),
    Input("tag-selector", "value"),
    Input("price-slider", "value"),
    )
    def update_scatter(selected_tags, price_range):

        if not selected_tags:
            selected_tags = scatter_data["default_tags"]

        fig = create_scatter(
            scatter_data["df"],
            selected_tags,
            price_range
        )

        return fig
    return app

if __name__ == "__main__":
    app = create_app()
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:8050/")).start()
    app.run(debug=False)