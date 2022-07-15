from flask import Flask, request

from manager.models.form_data import FormData
from manager.services.manager import Manager

app = Flask(__name__)


@app.route('/scrim-search', methods=['POST'])
def find_scrim():
    try:
        form_post = request.form
        form_data = FormData(team_name=form_post['team_name'],
                             team_elo=form_post['team_elo'],
                             order_elo=form_post['order_elo'],
                             scrim_date=form_post['scrim_date'])
    except Exception:
        print(Exception)
        raise Exception

    scrim_manager = Manager(form_data)
    return scrim_manager.process()
