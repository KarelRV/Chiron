from App import application
import pandas as pd
import numpy as np
#this is a comment3
from flask import flash, redirect, render_template, request, session, abort, url_for, jsonify, Response
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 


# flask-login
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = "login"
# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 20       
users = [User(id) for id in range(1, 21)]



@application.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('temp.html')


@application.route('/landing', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            username = request.form['username']
            password = request.form['password']        
            if password == username + "_secret":
                id = username.split('user')[1]
                user = User(id)
                login_user(user)
            return redirect(url_for('home'))
        else:
            return abort(401)
        temp_name = request.form['email']
        print temp_name
        insert_email(temp_name)
        flash("Thank you for signing Up")
    return render_template('index.html')






 
# somewhere to login
@application.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        if password == username + "_secret":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(url_for('home'))
        else:
            return abort(401)
    else:
        return render_template('index.html')


# somewhere to logout
@application.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@application.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

