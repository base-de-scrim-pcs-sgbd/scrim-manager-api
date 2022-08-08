from manager.models.form_data import FormScrimScore
from manager.services.postgre_connect import connect

class ScrimScore:

    def __init__(self,
                 form_data: FormScrimScore):
        self.scrim_id = form_data.scrim_id
        self.team_id = form_data.team_id
        self.scrim_score = form_data.scrim_score

    def _connect(self):
        self.connection = connect()

    def _create_scrim_score(self, scrim_id, team_id, scrim_score):
        query = f'INSERT INTO avaliacao' \
                f'(idscrim, idequipe, notascrim)' \
                f'VALUES ({scrim_id}, {team_id}, {scrim_score})'

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
            self._create_scrim_score(self.scrim_id, self.team_id, self.scrim_score)
            self.connection.close()

            return 'Team score sent!'
        except Exception as err:
            self.connection.close()
            print(err)

            return f'Error: {err}'
