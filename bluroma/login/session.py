from flask_bcrypt import Bcrypt
from flask import session

bcrypt = Bcrypt()

def create_password_hash(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password_hash(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)

def create_session(key, value):
    session['user'] = value

def create_auth_session(key, value):
    session_value = create_password_hash(value)
    session.clear()
    session[key] = session_value

def pop_session():
    session.pop('user', None)