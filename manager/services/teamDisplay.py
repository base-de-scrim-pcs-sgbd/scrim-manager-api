from manager.models.form_data import FormTeamDisplay
from manager.services.postgre_connect import connect

class TeamDisplay:

    def __init__(self,
                 form_data: FormTeamDisplay):
        self.user_id = form_data.user_id
        self.connection = None

    def _connect(self):
        self.connection = connect()

    def _display_team(self, team_id):
        query = f'SELECT * FROM equipe WHERE ' \
                f'idrepresentante = {self.user_id}'
                
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
            self._display_team(self.user_id)
            self.connection.close()

            return 'Teams found!'
        except Exception as err:
            self.connection.close()
            print(err)

            return f'Error: {err}'
