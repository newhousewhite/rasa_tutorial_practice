import pandas as pd
import mysql.connector

from sqlalchemy import create_engine


df_products = pd.read_csv("phones_laptops_database_NEW.csv")
df_news = pd.read_csv("laptops_phones_news.csv")

hostname = "localhost"
username = "rasa-user"
password = "password123"
database = "shopping_db"
# Open database connection
# engine = create_engine('mysql+mysqlconnector://<username>:<password>@<hostname>:3306/<database>', echo=False)
print('mysql+mysqlconnector://{:s}:{:s}@{:s}:3306/shopping_db'.format(username, password, hostname))
engine = create_engine(
    'mysql+mysqlconnector://{:s}:{:s}@{:s}:3306/shopping_db'.format(username, password, hostname),
    echo=False
)

df_products.to_sql('products', con=engine, if_exists='replace', index=False)
df_news.to_sql('news', con=engine, if_exists='replace', index=False)
