from manager.models.form_data import FormTeamCreate
from manager.services.postgre_connect import connect

class TeamRegister:

    def __init__(self,
                 form_data: FormTeamCreate):
        self.user_id = form_data.user_id
        self.team_name = form_data.team_name
        self.connection = None

    def _connect(self):
        self.connection = connect()

    def _create_team(self, user_id, team_name):
        query = f'INSERT INTO equipe ' \
                f'(nomeequipe, numeroatletas, eloequipe, idrepresentante) ' \
                f'VALUES (\'{team_name}\', 0, 0, {user_id})'

        self._execute_query(query)

    def _execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def process(self):
        self._connect()
        try:
            self._create_team(self.user_id, self.team_name)
            self.connection.close()

            return 'Team registration sucessful!'
        except Exception as err:
            self.connection.close()
            print(err)

            return f'Error: {err}'
