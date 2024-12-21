pip install sqlalchemy pymysql
from sqlalchemy import create_engine
import pandas as pd

# Replace with your MySQL credentials
username = 'root'
password = 'manobrathdutta.'
host = 'localhost:3306'
database = 'sportify'

# Create the connection URL
connection_url = f'mysql+pymysql://{username}:{password}@{host}/{database}'

try:
    # Create an SQLAlchemy engine
    engine = create_engine(connection_url)
    print("Connected to the database successfully.")

    # Create a DataFrame to upload
    accounts_df = pd.read_csv('Spotify.csv')
    print("CSV file loaded successfully.")

    # Upload the DataFrame to MySQL
    accounts_df.to_sql('song', con=engine, if_exists='replace', index=False)
    print("Data uploaded successfully.")

except Exception as e:
    print("An error occurred:", e)
