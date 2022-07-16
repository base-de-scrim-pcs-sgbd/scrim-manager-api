from manager.models.form_data import FormData
from manager.services.postgre_connect import connect


class Manager:

    def __init__(self,
                 form_data: FormData):
        self.team_id = form_data.team_id
        self.team_name = form_data.team_name
        self.team_elo = form_data.team_elo
        self.order_elo = form_data.order_elo
        self.scrim_date = form_data.scrim_date
        self.connection = None

    def _connect(self):
        self.connection = connect()

    def _find_match(self):
        query = f'SELECT * FROM pedidoscrim WHERE ' \
                f'eloequipe >= {self.order_elo} AND ' \
                f'elopedido <= {self.team_elo} AND ' \
                f'datapedido = {self.scrim_date}'

        cursor = self.connection.cursor()
        cursor.execute(query)

        return cursor.fetchone()

    def _execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def _create_scrim(self, team_one, team_two, scrim_date):
        query = f'INSERT INTO scrim ' \
                f'(idequipe1, idequipe2, datascrim) ' \
                f'VALUES ({team_one}, {team_two}, {scrim_date})'

        self._execute_query(query)

    def _create_order(self, team_id, team_elo, order_elo, scrim_date):
        query = f'INSERT INTO pedidoscrim ' \
                f'(idequipe, eloequipe, elopedido, datapedido) ' \
                f'VALUES ({team_id}, {team_elo}, {order_elo}, {scrim_date})'

        self._execute_query(query)

    def _delete_order(self, order_id):
        query = f'DELETE FROM pedidoscrim WHERE idpedido = {order_id}'

        self._execute_query(query)

    def process(self):
        self._connect()
        match = self._find_match()

        if match:
            try:
                self._create_scrim(self.team_id, match[1], self.scrim_date)
                self._delete_order(match[0])
                self.connection.close()

                return 'Scrim found! Check your scrims page'
            except Exception as err:
                self.connection.close()
                print(err)

                return f'Error: {err}'
        else:
            self._create_order(self.team_id, self.team_elo, self.order_elo, self.scrim_date)
            self.connection.close()

            return 'Scrim not found, but we\'ll find a match soon!'
