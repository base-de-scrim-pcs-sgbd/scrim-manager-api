from manager.models.form_data import FormTeamEdit
from manager.services.postgre_connect import connect

class TeamEdit:

    def __init__(self,
                 form_data: FormTeamEdit):
        self.team_id = form_data.team_id
        self.player_name = form_data.player_name
        self.player_elo = form_data.player_elo
        self.connection = None

    def _connect(self):
        self.connection = connect()

    def _edit_team(self, team_id, player_name, player_elo):
        query = f'INSERT INTO atleta ' \
                f'(idequipe, nomeatleta, eloatleta)  ' \
                f'VALUES ({team_id}, {player_name}, {player_elo})'

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
            self._edit_team(self.team_id, self.player_name, self.player_elo)
            self.connection.close()

            return 'Player added successfully!'
        except Exception as err:
            self.connection.close()
            print(err)

            return f'Error: {err}'
