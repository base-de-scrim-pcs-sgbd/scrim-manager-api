from flask import Flask, request

from manager.models.form_data import FormData
from manager.services.manager import Manager
from manager.services.config import set_config

app = Flask(__name__)


@app.route('/scrim-search', methods=['POST'])
def find_scrim():
    sql_credentials = set_config()
    form_data = FormData(team_name=request.form['team_name'],
                         team_elo=request.form['team_elo'],
                         order_elo=request.form['order_elo'],
                         scrim_date=request.form['scrim_date']
                         )
    scrim_manager = Manager(sql_credentials, form_data)
    return scrim_manager.process()
