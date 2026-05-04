import plotly.express as px

def create_tag_heatmap(heatmap_matrix, percentage_matrix):
    heatmap_matrix = heatmap_matrix.T
    percentage_matrix = percentage_matrix.T

    fig = px.imshow(
        heatmap_matrix,
        labels={
            "x": "Release Years",
            "y": "Steam Tag",
            "color": "Number of Games"
        },
        title="Steam Game Releases by Tag and Year",
        aspect="auto",
        color_continuous_scale="Viridis" #Plasma, Cividis, Blues, YlOrRd, Turbo
    )

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
            title="Games",
            x=-0.05,
            xanchor="right"
        )
    )

    fig.update_traces(
        customdata=percentage_matrix.values,
        hovertemplate=(
            "Release Year: %{x}<br>"
            "Steam Tag: %{y}<br>"
            "Number of Games: %{z:.0f}<br>"
            "Share of yearly releases: %{customdata:.2f}%"
            "<extra></extra>"
        )
    )

    fig.update_yaxes(side="right")

    return fig


