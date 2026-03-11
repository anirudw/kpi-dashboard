import plotly.express as px

def churn_num_plot(churn_df):

    fig = px.pie(
        churn_df,
        names="Is Churned",
        values="Customer Count",
        hole=0.4,
        title="Customer Churn Distribution"
    )

    fig.update_layout(template="plotly_white")

    return fig