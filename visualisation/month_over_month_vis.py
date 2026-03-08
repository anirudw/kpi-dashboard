import plotly.graph_objects as go


def plot_mom_growth(mom_df):
    fig = go.Figure()

    fig.add_bar(
        x=mom_df.index,
        y=mom_df["Monthly Revenue"],
        name="Revenue",
        marker_color="lightgray"
    )

    fig.add_trace(
        go.Scatter(
            x=mom_df.index,
            y=mom_df["MoM Growth (%)"],
            mode="lines+markers",
            name="MoM Growth",
            yaxis="y2",
            line=dict(color="#2A9D8F", width=3)
        )
    )

    fig.update_layout(
        title="Monthly Revenue vs Growth",
        yaxis=dict(title="Revenue"),
        yaxis2=dict(
            title="MoM Growth (%)",
            overlaying="y",
            side="right"
        ),
        template="plotly_white"
    )
    return fig


