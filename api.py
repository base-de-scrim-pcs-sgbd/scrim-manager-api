from flask import Flask

from manager.models.form_data import FormData
from manager.services.manager import Manager
from manager.services.config import set_config

app = Flask(__name__)


@app.route('/scrim-search', methods=['POST'])
def find_scrim():
    sql_credentials = set_config()
    form_data = FormData(team_name=['team_name'],
                         team_elo=['team_elo'],
                         order_elo=['order_elo'],
                         scrim_date=['scrim_date'])
    scrim_manager = Manager(sql_credentials, form_data)
    return scrim_manager.process()
