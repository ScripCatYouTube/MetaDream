import secrets

from datetime import timedelta
from flask import Flask, session, request

from .fabric_user import FabricUser 


def start(server, is_run = False, sessions_days = 2):
    app = Flask(__name__)

    app.secret_key = secrets.token_hex().encode()

    server.app = app

    @app.route("/ping")
    def ping():
        return server.ping_data

    @app.route("/all")
    def all():
        if session.get('user'):
            return {'status': True, 'data': server.msg_tracker.messages}
        return {'status': False, 'data': 'You\'re not logged'}

    @app.route("/local")
    def local(): 
        if session.get('user'):
            return {'status': True, 'data': server.get_user().msg_track.messages}
        return {'status': False, 'data': 'You\'re not logged'}

    @app.route("/response/<json_value>")
    def response(json_value):
        return server.response(json_value)

    @app.route("/logout")
    def logout():
        return server.autho.logout()

    @app.route('/login/<nickname>/<password>')
    def login(nickname, password):
        return server.autho.login(nickname, password)

    @app.route('/register/<nickname>/<password>')
    def register(nickname, password):
        return server.autho.register(nickname, password)

    @app.errorhandler(404)
    def page_not_found(e):
        return {'status': 'error', 'data': 404}

    @app.before_request
    def make_session_permanent():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(days = sessions_days)

    print('Started')
    if is_run: app.run()