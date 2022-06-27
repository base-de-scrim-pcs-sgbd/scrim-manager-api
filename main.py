from dotenv import load_dotenv
from os import environ

load_dotenv()

sql_user = environ.get('SQL_USER')
sql_password = environ.get('SQL_PASSWORD')
sql_host = environ.get('SQL_HOST')
sql_database = environ.get('SQL_DATABASE')
