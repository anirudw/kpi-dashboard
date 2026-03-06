import matplotlib.pyplot as plt
import seaborn as sb

sb.set_theme(style='whitegrid')
def plot_mom_growth(mom_df):
    fig, ax1 = plt.subplots(figsize=(10,6))
    ax1.bar(
        mom_df.index,
        mom_df["Monthly Revenue"],
        width=20,
        color="#D3D3D3",
        edgecolor="black",
        linewidth=0.5,
        label="Revenue"
    )
    ax2 = ax1.twinx()
    ax1.set_title(
        "Monthly Revenue and MoM Growth",
        fontsize=14,
        fontweight="bold"
    )
    
    sb.lineplot(
        x=mom_df.index,
        y=mom_df["MoM Growth (%)"],
        marker="o",
        linewidth=2.5,
        markersize=8,
        color="#2A9D8F",
        ax=ax2,
        label="MoM Growth"
    )
    ax1.set_ylabel('Monthly Revenue ($)')
    ax1.set_xlabel('Sales Month')
    ax2.set_ylabel("MoM Growth (%)", fontsize=11)
    ax1.set_title('Revenue vs. Growth Trend')
    ax1.ticklabel_format(style='plain', axis='y')
    ax1.grid(axis="y", linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    sb.despine()
    return fig


