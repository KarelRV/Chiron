from App import application
from dbconnect import enteremail,createusernameandpassword,retrieve_email, complete_profiles
from Emailer import send_mail
import pandas as pd
import numpy as np
#this is a comment3
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, jsonify, Response
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
from flask_mail import Mail, Message


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


#would like to get this section out of this .py file


@application.route('/<username>', methods=['GET', 'POST'])
@login_required
def home(username):
    return render_template('temp.html', username=username)



@application.route('/test_mail')
def test_mail():
    send_mail('karelrverhoeven@gmail.com')
    return 'Mail sent'

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['btn'] == 'Login':
            username = request.form['username']
            password = request.form['password']        
            if password == username + "_secret":
                id = username.split('user')[1]
                user = User(id)
                login_user(user)
                return redirect(url_for('home', username=username))
            else:
                return abort(401)
        if request.form['btn'] == 'Signup':
            print "1"
            email = request.form['email']
            print "2"
            enteremail(email)
            print "3"
            session['email'] = email
            return redirect(url_for('complete_registration'))
    return render_template('index.html')


@application.route('/complete_profile', methods=['GET', 'POST'])
def complete_profile():
    if request.method == 'POST':
        if request.form['btn'] == 'Complete':
            email = session.get('email', None)
            location = request.form['location']
            job = request.form['job']
            complete_profiles(email,location,job)
            return render_template('temp_landing.html')
    return render_template('complete_profile.html')

@application.route('/complete_registration', methods=['GET', 'POST'])
def complete_registration():
    if request.method == 'POST':
        if request.form['btn'] == 'Register':
            username = request.form['username']
            password = request.form['password']
            email = session.get('email', None)
            print email
            createusernameandpassword(email,username,password)
            send_mail(email,username)
            return render_template('temp.html')
    return render_template('complete_registration.html')

@application.route('/welcome_page/<username>', methods=['GET', 'POST'])
def welcome(username):
    if request.method == 'POST':
        print "1"
        #if request.form['btn'] == 'Complete':
        print "2"
        email = retrieve_email(username)
        print "3"
        session['email'] = email
        print "4"
        return redirect(url_for('complete_profile'))
        print "5"
    return render_template('temp.html',username=username)

# somewhere to logout
@application.route("/logout")
@login_required
def logout():
    logout_user()
    # return Response('<p>Logged out</p>')
    return render_template('logout.html')


############################################coetzee additions - employer related##########################################
##Remove comments later
############################################coetzee additions - employer related##########################################
# employer home page
@application.route('/employerhome/<username>', methods=['GET','POST'])
@login_required
def employerhome(username):

    return render_template('employer_home.html', username=username)

# employer edit page
@application.route('/employeredit/<username>', methods=['GET','POST'])
@login_required
def employeredit(username):

    return render_template('edit_employer_profile.html', username=username)

# employer add vacancy
@application.route('/employeraddvacancy/<username>', methods=['GET','POST'])
@login_required
def employeraddvacancy(username):

    return render_template('employer_add_vacancy.html', username=username)

# employer edit vacancy
@application.route('/employereditvacancy/<username>', methods=['GET','POST'])
@login_required
def employereditvacancy(username):

    return render_template('employer_edit_vacancy.html', username=username)

# view employees
@application.route('/viewemployees/<username>', methods=['GET','POST'])
@login_required
def viewemployees(username):

    return render_template('view_employees.html', username=username)

############################################coetzee additions - employer related##########################################


# handle login failed
@application.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

