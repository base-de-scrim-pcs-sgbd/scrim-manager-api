from manager.models.form_data import FormTeamDisplay
from manager.services.postgre_connect import connect

class TeamDisplay:

    def __init__(self,
                 form_data: FormTeamDisplay):
        self.user_id = form_data.user_id
        self.team_id = form_data.team_id
        self.connection = None

    def _connect(self):
        self.connection = connect()

    def _display_team(self):
        query = f'SELECT * FROM equipe WHERE ' \
                f'idrepresentante = {self.user_id}' \
                f'AND idequipe = {self.team_id}'
                
        cursor = self.connection.cursor()
        cursor.execute(query)

        return cursor.fetchone()

    def _execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

        self._execute_query(query)

    def process(self):
        self._connect()
        try:
            team = self._display_team()
            self.connection.close()

            return f'Team found! : {team}'
        except Exception as err:
            self.connection.close()
            print(err)

            return f'Error: {err}'
