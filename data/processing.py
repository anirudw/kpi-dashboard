import pandas as pd

def process_mom_data(record):
    mom_df = pd.DataFrame(record, columns=['Sales Month', 'Monthly Revenue', 'Previous Month Revenue', 'MoM Growth (%)'])
    mom_df.set_index('Sales Month', inplace=True)

    return mom_df


def process_customer_profile(record):
    profile_df = pd.DataFrame(record, columns=['Customer ID', 'No. of Purchases Done', 'Total Revenue'])
    profile_df.set_index('Customer ID', inplace=True)
    return profile_df

def process_customer_churn(record):
    churn_df = pd.DataFrame(record, columns=['Customer ID', 'Date of Last Purchase', 'Days Since Last Purchase', 'Is Churned'])
    churn_df.set_index('Customer ID', inplace=True)

    
    churn_df.columns=churn_df.columns.str.strip()
    churn_num_df = churn_df['Is Churned'].value_counts().reset_index()
    churn_num_df.columns =['Is Churned', 'Customer Count']
    print(churn_num_df)

    return (churn_df, churn_num_df)

