from manager.models.form_data import FormScrimHistory
from manager.services.postgre_connect import connect

class ScrimHistory:

    def __init__(self,
                 form_data: FormScrimHistory):
        self.team_id = form_data.team_id

    def _connect(self):
        self.connection = connect()

    def _display_scrim_history(self):
        today = 1657986217
        query = f'SELECT * ' \
                f'FROM scrim AS sc ' \
                f'INNER JOIN avaliacao AS av ON av.idscrim = sc.idscrim ' \
                f'WHERE ' \
                f'sc.datascrim < {today} AND ' \
                f'idequipe = {self.team_id}'

        cursor = self.connection.cursor()
        cursor.execute(query)

    def _execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

        self._execute_query(query)

    def process(self):
        self._connect()
        try:
            self._display_scrim_history()
            self.connection.close()

            return 'Team history found!'
        except Exception as err:
            self.connection.close()
            print(err)

            return f'Error: {err}'
