import psycopg2
import pandas as pd
from config import config

# Obtain the configuration parameters
params = config()
# Connect to the PostgreSQL database
conn = psycopg2.connect(**params)
# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database
def create_pandas_table(sql_query, database=conn):
    table = pd.read_sql_query(sql_query, database)
    return table

# Utilize the create_pandas_table function to create a Pandas data frame
# Store the data as a variable
data_emas = create_pandas_table("SELECT * FROM emas")
data_perak = create_pandas_table("SELECT * FROM perak")
data_dolar = create_pandas_table("SELECT * FROM dolar")
# Close the cursor and connection to so the server can allocate

# bandwidth to other requests
cur.close()
conn.close()