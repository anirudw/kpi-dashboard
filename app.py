from data.connection import get_connection
from data.processing import process_mom_data, process_customer_churn, process_customer_profile
from data.querries import fetch_mom, fetch_churn, fetch_profile
from visualisation.month_over_month_vis import plot_mom_growth
from visualisation.churned_comp_vis import churn_num_plot

def main():
    connection = get_connection()
    mom = process_mom_data(fetch_mom(connection))
    # plot_mom_growth(mom)

    churn, churn_num = process_customer_churn(fetch_churn(connection))
    profile = process_customer_profile(fetch_profile(connection))
    churn_num_plot(churn_num)



if __name__ == '__main__':
    main()

