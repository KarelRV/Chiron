from App import application
from flask_mail import Mail, Message
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, jsonify, Response

def send_mail(email_adress):
	application.config.update(
	MAIL_SERVER = 'smtp.gmail.com',
	MAIL_PORT = 465,
	MAIL_USE_SSL = True,
	MAIL_USERNAME = 'projectchiron123@gmail.com',
	MAIL_PASSWORD = 'WhyAlwaysMe',
	MAIL_USE_TLS = False
	)
	mail = Mail()
	mail.init_app(application)
	msg = mail.send_message(
		'Welcome to Chiron!',
		sender='projectchiron123@gmail.com',
		recipients=[email_adress],
		body="Confirm Email >>>   http://0.0.0.0:4000/"
	)


