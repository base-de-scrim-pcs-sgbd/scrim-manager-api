from manager.models.form_data import FormData
from manager.services.postgre_connect import connect


class Manager:

    def __init__(self,
                 form_data: FormData):
        self.team_name = form_data.team_name
        self.team_elo = form_data.team_elo
        self.order_elo = form_data.order_elo
        self.scrim_date = form_data.scrim_date
        self.connection = None

    def _connect(self):
        self.connection = connect()

    def _find_match(self):
        query = f'SELECT * FROM Orders WHERE ' \
                f'TeamElo >= {self.order_elo} AND' \
                f'OrderElo <= {self.team_elo} AND' \
                f'ScrimDate = {self.scrim_date}'

        cursor = self.connection.cursor()
        cursor.execute(query)

        return cursor.fetchone()

    def _execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def _create_scrim(self, team_one, team_two, scrim_date):
        query = f'INSERT INTO scrims ' \
                f'(TeamOne, TeamTwo, ScrimDate) ' \
                f'VALUES ({team_one, team_two, scrim_date})'

        self._execute_query(query)

    def _create_order(self, team_name, team_elo, order_elo, scrim_date):
        query = f'INSERT INTO orders ' \
                f'(TeamName, TeamElo, OrderElo, ScrimDate) ' \
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
