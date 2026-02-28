import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import URL, create_engine
load_dotenv()
data_set = pd.read_csv('online_retail_2010_2011.csv')
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

engine = create_engine(connection_url)
data_set.to_sql('online_retail_2010_2011', engine, if_exists='replace', index=False)