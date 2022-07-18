import hashlib
from manager.models.form_data import FormUser
from manager.services.postgre_connect import connect

class UserLogin:

    def __init__(self,
                 form_data: FormUser):
        self.user_email = form_data.user_email
        # Aplicar criptografia no password fornecido pelo usuário antes de submeter ao banco
        self.user_password = hashlib.sha512(str(form_data.user_password).encode("utf-8") ).hexdigest()
        self.connection = None

    def _connect(self):
        self.connection = connect()

    def _find_user(self, user_email, user_password):
        query = f'SELECT * FROM representante WHERE ' \
                f'emailrepresentante = {user_email} AND ' \
                f'senharepresentante = {user_password})'

        cursor = self.connection.cursor()
        cursor.execute(query)

        return cursor.fetchone()

    def _execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def process(self):
        self._connect()
        try:
            self._find_user(self.user_email, self.user_password)
            self.connection.close()

            return 'Login successful!'
        except Exception as err:
            self.connection.close()
            print(err)

            return f'Error: {err}'
