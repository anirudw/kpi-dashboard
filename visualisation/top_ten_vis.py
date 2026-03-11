import plotly.express as px

def plot_top_ten(top_ten_df):
    top_ten_df = top_ten_df.copy()
    top_ten_df.index = top_ten_df.index.astype(str)

    fig = px.bar(
        top_ten_df,
        x="Total Revenue",
        y=top_ten_df.index,
        orientation="h",
        title="Top 10 Customers by Revenue",
        color="Total Revenue",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        template="plotly_white",
        yaxis=dict(type="category", title="Customer ID"),
        xaxis=dict(title="Total Revenue ($)", tickformat=",")
    )

    return fig