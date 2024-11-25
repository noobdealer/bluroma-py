import os
import sqlite3

from atproto import Client
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt

from bluroma.db import db
from bluroma.login import session, user_resolution

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
bcrypt = Bcrypt(app)
resolver = user_resolution

client = None
profile = None

session_display_name = "none"
load_dotenv()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dash')
def dashboard():
    return render_template('dash.html')

@app.route('/api/login', methods=['POST'])
def login():
    if request.method != 'POST':
        return "Invalid request method"

    username = request.form['handle']
    password = request.form['password']
    try:
        user_did = resolver.resolve_did(username)
        print("DID logging in:", user_did)
        user_did_doc = resolver.resolve_did_doc(user_did)
        user_pds = resolver.resolve_pds(user_did_doc)
        client = Client(user_pds)
        profile = client.login(username, password)
        print('Welcome,', profile.display_name)
        # TODO: This is for sure not how authentication should work but I can't really tell what's happening here
        session.create_auth_session(username, password)
        session.create_session(username, profile.display_name)
        return redirect(url_for("dashboard"))
    except Exception as error:
        print("Failed to login -", error)
        return render_template('index.html')

@app.route('/api/logout')
def logout():
    session.pop_session()
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("Welcome to bluroma")
    if (os.getenv("SECRET_KEY") == "ChangeMeA$AP!") & (os.getenv("DEBUG") == "False"):
        print("CHANGE YOUR SECRET KEY BEFORE DEPLOYING.")
        exit(1)
    print("Connecting to DB...")
    db_conn = sqlite3.connect(os.getenv('DB_NAME'))
    try:
        db.check_migration_level(db_conn)
    except Exception as error:
        print("Error while checking DB migrations -", error)
        exit(1)
    print("Connected to DB, starting app...")

    # Launch app now that the DB connection is established
    app.run(debug=os.getenv('DEBUG_APP'))