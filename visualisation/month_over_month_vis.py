import matplotlib.pyplot as plt
import seaborn as sb

def plot_mom_growth(mom_df):
    fig, ax1 = plt.subplots(figsize=(10,6))
    ax1.bar(mom_df.index, mom_df['Monthly Revenue'],width=20, color='lightgray')

    ax2 = ax1.twinx()

    sb.lineplot(
        data = mom_df,
        x = mom_df.index, # same x axis
        y = 'MoM Growth (%)', #diff y axis
        color = 'darkorange',
        marker = 'o',
        ax = ax2
    )
    ax1.set_ylabel('Monthly Revenue ($)')
    ax1.set_xlabel('Sales Month')
    ax2.set_ylabel('MoM Growth (%)')
    ax1.set_title('Revenue vs. Growth Trend')
    ax1.ticklabel_format(style='plain', axis='y')
    plt.show()


