import os
import psycopg2


def connect():
    database_url = os.environ['DATABASE_URL']

    return psycopg2.connect(database_url, sslmode='require')