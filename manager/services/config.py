from dotenv import load_dotenv
from os import environ

from manager.models.sql_credentials import SqlCredentials


def set_config():
    load_dotenv()

    sql_user = environ.get('SQL_USER')
    sql_password = environ.get('SQL_PASSWORD')
    sql_host = environ.get('SQL_HOST')
    sql_database = environ.get('SQL_DATABASE')

    return SqlCredentials(username=sql_user,
                          password=sql_password,
                          host=sql_host,
                          database=sql_database)
