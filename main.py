import os
import psycopg2 as ps
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


try:
    connection = ps.connect(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"), database=os.getenv("DB_NAME"))
    cursor = connection.cursor()
    # print("PSQL connection params: ")
    # print(connection.get_dsn_parameters(),"\n")

    cursor.execute("""SELECT * from mom_percent;""")
    mom_record = cursor.fetchall()
    cursor.execute("""SELECT * from customer_churn;""")
    churn_record = cursor.fetchall()
    # print(churn_record);
    cursor.execute("""SELECT  * from customer_profile;""")

    # print("RECORD:", record)
except (Exception) as error:
    print("ERROR CONNECTING TO DB")

mom_df = pd.DataFrame(mom_record, columns=['Sales Month', 'Monthly Revenue', 'Previous Month Revenue', 'MoM Growth (%)'])
mom_df.set_index("Sales Month", inplace=True)

churn_df = pd.DataFrame(churn_record, columns=['Customer ID', 'Date of Last Purchase', ' Days since Last Purchase', 'Is Churned'])
churn_df.set_index("Customer ID", inplace = True)
# churn_df.index = churn_df['Customer ID']
print(churn_df.head())
# print(mom_df.head())



# data_set = pd.read_csv('online_retail_2010_2011.csv')
# print(data_set.head())