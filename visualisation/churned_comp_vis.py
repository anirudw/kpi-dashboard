import matplotlib.pyplot as plt
import seaborn as sb

sb.set_theme(style='whitegrid')

def churn_num_plot(churn_data):
    fig, ax1 = plt.subplots(figsize=(10,6))
    sb.barplot(
        data = churn_data,
        x = 'Is Churned',
        y = 'Customer Count',
        hue="Is Churned",
        palette=['blue', 'red'],
        
        ax = ax1
    )

    ax1.set_title("Number of Churned Customers")
    ax1.set_xlabel("Is Churned?")
    ax1.set_ylabel("Number of Customers")

    return fig
