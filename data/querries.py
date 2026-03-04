import psycopg2 as ps

def fetch_mom(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * from mom_percent;""")
    mom_record = cursor.fetchall()
    return mom_record

def fetch_profile(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * from customer_profile;""")
    profile_record = cursor.fetchall()
    return profile_record

def fetch_churn(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * from customer_churn;""")
    churn_record = cursor.fetchall()
    return churn_record
    