from App import application
import pandas as pd
import numpy as np
#this is a comment3
from flask import flash, redirect, render_template, request, session, abort, url_for, jsonify



@application.route('/', methods=['GET', 'POST'])
def home():
    return render_template('temp.html')

    