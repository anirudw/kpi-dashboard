import seaborn as sb
import matplotlib.pyplot as plt

sb.set_theme(style='whitegrid')

def plot_top_ten(profile_data):

    fig, ax1 = plt.subplots(figsize=(10,6))
    sb.barplot(
        data = profile_data,
        x = "Customer ID",
        y = "Total Revenue",
        palette='viridis',
        hue="Total Revenue",
        ax = ax1
    )

    ax1.set_title("Top 10 Customers by Revenue")
    ax1.set_xlabel("Customer ID")
    ax1.set_ylabel("Revenue Generated in $")

    return fig


