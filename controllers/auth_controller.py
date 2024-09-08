from flask import Blueprint, request, session, redirect, url_for, render_template, current_app
from models.user_model import users

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    logger = current_app.logger
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            logger.info(f'User {username} logged in successfully')
            return redirect(url_for('.home'))
        else:
            logger.warning(f'Failed login attempt for user {username}')
            return 'Invalid username or password'
    return render_template('login.html')

@auth_blueprint.route('/logout')
def logout():
    logger = current_app.logger
    session.pop('username', None)
    logger.info('User logged out')
    return redirect(url_for('.login'))

@auth_blueprint.route('/')
def home():
    if 'username' in session:
        return render_template('home.html')
    return redirect(url_for('.login'))
