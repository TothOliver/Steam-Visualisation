import plotly.express as px

def create_tag_heatmap(heatmap_matrix, percentage_matrix, fixed_color_scale=False):
    percentage_plot_matrix = percentage_matrix.T
    count_plot_matrix = heatmap_matrix.T

    imshow_settings = {
        "img": percentage_plot_matrix,
        "labels": {
            "x": "Release Years",
            "y": "Steam Tag",
            "color": "Share of Yearly Releases (%)"
        },
        "title": "Steam Game Releases by Tag and Year",
        "aspect": "auto",
        "color_continuous_scale": "YlOrRd" #Viridis, Cividis YlOrRd
    }

    if fixed_color_scale:
        imshow_settings["range_color"] = [0, 100]

    fig = px.imshow(**imshow_settings)

    fig.update_layout(
        width=1200, 
        height=800,
        title={
            "text": "Steam Game Releases by Tag and Year",
            "x": 0.5,
            "xanchor": "center"
        },
        xaxis_title="Release Years",
        yaxis_title="Steam Tag",
        margin=dict(l=120, r=180, t=80, b=80),
        coloraxis_colorbar=dict(
            title=dict(
                text="Games <br>Share <br>(%)",
                side="top",
                font=dict(
                    size=13
                )
            ),
            x=-0.1,
            xanchor="right",
        )
    )

    fig.update_traces(
        customdata=count_plot_matrix.values,
        hovertemplate=(
            "Release Year: %{x}<br>"
            "Steam Tag: %{y}<br>"
            "Share of yearly releases: %{z:.2f}%<br>"
            "Number of Games: %{customdata:.0f}"
            "<extra></extra>"
        )
    )

    fig.update_yaxes(side="right")

    return fig


