import pandas as pd

def process_mom_data(record):
    mom_df = pd.DataFrame(record, columns=['Sales Month', 'Monthly Revenue', 'Previous Month Revenue', 'MoM Growth (%)'])
    mom_df.set_index('Sales Month', inplace=True)
    total_revenue = mom_df["Monthly Revenue"].sum()
    # print(total_revenue)
    return (mom_df,total_revenue)


def process_customer_profile(record):
    profile_df = pd.DataFrame(record, columns=['Customer ID', 'No. of Purchases Done', 'Total Revenue'])
    profile_df.sort_values(by='Total Revenue', ascending=False, inplace=True)
    
    profile_df["Customer ID"] = profile_df['Customer ID'].astype(int)
    profile_df.set_index('Customer ID', inplace=True)
    top_ten_df = profile_df.head(10)
    # print(total_customers)
    return (profile_df, top_ten_df)

def process_customer_churn(record):
    churn_df = pd.DataFrame(record, columns=['Customer ID', 'Date of Last Purchase', 'Days Since Last Purchase', 'Is Churned'])
    churn_df.set_index('Customer ID', inplace=True)
    churn_df.columns=churn_df.columns.str.strip()
    
    churn_num_df = churn_df['Is Churned'].value_counts().reset_index()
    churn_num_df["Is Churned"] = churn_num_df['Is Churned'].map({0:'No', 1:"Yes"})
    churn_num_df.columns =['Is Churned', 'Customer Count']
    # print(churn_num_df)

    #churn rate
    total_customers = churn_df.shape[0]
    is_churned = churn_df[churn_df['Is Churned']==1].shape[0]
    churn_rate = (is_churned/total_customers) * 100

    return (churn_df, churn_num_df,churn_rate,total_customers)






