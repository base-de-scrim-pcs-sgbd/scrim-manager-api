from flask import Flask, request

from manager.models.form_data import FormScrimHistory, FormScrimScore, FormScrimSearch, FormTeamCreate, FormTeamEdit, FormUser
from manager.services.userRegister import UserRegister
from manager.services.userLogin import UserLogin
from manager.services.teamRegister import TeamRegister
from manager.services.teamEdit import TeamEdit
from manager.services.teamDisplay import TeamDisplay
from manager.services.scrimSearch import ScrimSearch
from manager.services.scrimHistory import ScrimHistory
from manager.services.scrimScore import ScrimScore


app = Flask(__name__)


@app.route('/user-register', methods=['POST'])
def create_user():
    try:
        form_post = request.form
        form_data = FormUser(user_id=form_post['user_id'],
                             user_email=form_post['user_email'],
                             user_password=form_post['user_password'])
    except Exception:
        print(Exception)
        raise Exception

    manager = UserRegister(form_data)
    return manager.process()


@app.route('/user-login', methods=['GET'])
def find_user():
    try:
        form_get = request.form
        form_data = FormUser(user_id=form_get['user_id'],
                             user_email=form_get['user_email'],
                             user_password=form_get['user_password'])
    except Exception:
        print(Exception)
        raise Exception

    manager = UserLogin(form_data)
    return manager.process()


@app.route('/team-register', methods=['POST'])
def create_team():
    try:
        form_post = request.form
        form_data = FormTeamCreate(user_id=form_post['user_id'],
                                   team_name=form_post['team_name'])
    except Exception:
        print(Exception)
        raise Exception

    manager = TeamRegister(form_data)
    return manager.process()


@app.route('/team-display', methods=['GET'])
def display_team():
    try:
        form_get = request.form
        form_data = FormTeamCreate(team_id=form_get['team_id'])
    except Exception:
        print(Exception)
        raise Exception

    manager = TeamDisplay(form_data)
    return manager.process()


@app.route('/team-edit', methods=['POST'])
def edit_team():
    try:
        form_post = request.form
        form_data = FormTeamEdit(team_id=form_post['team_id'],
                                 player_name=form_post['player_name'],
                                 player_elo=form_post['player_elo'],
                                )
    except Exception:
        print(Exception)
        raise Exception

    manager = TeamEdit(form_data)
    return manager.process()


@app.route('/scrim-search', methods=['POST'])
def find_scrim():
    try:
        form_post = request.form
        form_data = FormScrimSearch(team_id=form_post['team_id'],
                                    team_name=form_post['team_name'],
                                    team_elo=form_post['team_elo'],
                                    order_elo=form_post['order_elo'],
                                    scrim_date=form_post['scrim_date'])
    except Exception:
        print(Exception)
        raise Exception

    manager = ScrimSearch(form_data)
    return manager.process()


@app.route('/scrim-history', methods=['GET'])
def display_scrim_history():
    try:
        form_get = request.form
        form_data = FormScrimHistory(team_id=form_get['team_id'])
    except Exception:
        print(Exception)
        raise Exception

    manager = ScrimHistory(form_data)
    return manager.process()


@app.route('/scrim-score', methods=['POST'])
def send_scrim_score():
    try:
        form_post = request.form
        form_data = FormScrimScore(scrim_id=form_post['scrim_id'],
                                   team_id=form_post['team_id'],
                                   scrim_score=form_post['scrim_score'])
    except Exception:
        print(Exception)
        raise Exception

    manager = ScrimScore(form_data)
    return manager.process()