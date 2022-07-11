import mysql.connector

from manager.models.form_data import FormData
from manager.models.sql_credentials import SqlCredentials


class Manager:

    def __init__(self,
                 sql_credentials: SqlCredentials,
                 form_data: FormData):
        self.sql_user = sql_credentials.username
        self.sql_password = sql_credentials.password
        self.sql_host = sql_credentials.host
        self.sql_database = sql_credentials.database
        self.team_name = form_data.team_name
        self.team_elo = form_data.team_elo
        self.order_elo = form_data.order_elo
        self.scrim_date = form_data.scrim_date
        self.connection = None

    def _connect(self):
        self.connection = mysql.connector.connect(self.sql_user,
                                                  self.sql_password,
                                                  self.sql_host,
                                                  self.sql_database)

    def _find_match(self):
        query = f'SELECT * FROM orders WHERE ' \
                f'team_elo >= {self.order_elo} AND' \
                f'order_elo <= {self.team_elo} AND' \
                f'scrim_date = {self.scrim_date}'

        cursor = self.connection.cursor()
        cursor.execute(query)

        return cursor.fetchone()

    def _execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def _create_scrim(self, team_one, team_two, scrim_date):
        query = f'INSERT INTO scrims ' \
                f'(team_one, team_two, scrim_date) ' \
                f'VALUES ({team_one, team_two, scrim_date})'

        self._execute_query(query)

    def _create_order(self, team_name, team_elo, order_elo, scrim_date):
        query = f'INSERT INTO orders ' \
                f'(team_name, team_elo, order_elo, scrim_date) ' \
                f'VALUES ({team_name, team_elo, order_elo, scrim_date})'

        self._execute_query(query)

    def process(self):
        self._connect()
        match = self._find_match()

        if match:
            try:
                self._create_scrim(self.team_name, match.team_name, self.scrim_date)
                self.connection.close()

                return 'Scrim found! Check your scrims page'
            except Exception as err:
                self.connection.close()
                print(err)

                return f'Error: {err}'
        else:
            self._create_order(self.team_name, self.team_elo, self.order_elo, self.scrim_date)
            self.connection.close()

            return 'Scrim not found, but we\'ll find a match soon!'

