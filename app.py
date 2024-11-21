from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_session import Session
from atproto import Client
from markupsafe import escape
from dotenv import load_dotenv, dotenv_values
import os

app = Flask(__name__)

session_display_name = "none"
load_dotenv()

@app.route("/", methods=['GET'])
def index():
    try:
        print(profile.display_name)
    except AttributeError:
        print("Not logged in")
    return render_template('index.html', user_display_name=session_display_name)

@app.route('/api/login', methods=['POST'])
def login_user():
    username = request.form['handle']
    password = request.form['password']
    try:
        profile = client.login(username, password)
        session_display_name = profile.display_name
        print('Welcome,', session_display_name)
        return redirect(url_for("index"), user_display_name=session_display_name)
    except Exception as error:
        print("Failed to login,", type(error).__name__, "–", error)
        return render_template('index.html', user_display_name="none")

if __name__ == '__main__':
    client = Client()
    profile = None
    app.run(debug=True)