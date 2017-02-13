from flask import flash, redirect, render_template, request, session, abort, url_for, jsonify
from dbconnect import Navbar_Search

def get_search_options():
	search_options = Navbar_Search()
	search_options = search_options.set_index('SearchType').T
	return search_options

def search(x,y):
	if x == 'Customer':
		barname = y
		if barname == '':
			return redirect(url_for('home'))
		return redirect('/profile/{0}'.format(barname))

	if x == 'Province':
		province = y
		if province == '':
			return redirect(url_for('home'))
		return redirect(url_for('home'))

	if x == 'Rank':
		province = y
		if province =='':
			return redirect(url_for('home'))
		return redirect(url_for('home'))

	if x == 'Date_Added':
		province = y
		if province == '':
			return redirect(url_for('home'))
		return redirect(url_for('home'))

	if x == 'Date_Uplifted':
		province = y
		if province == '':
			return redirect(url_for('home'))
		return redirect(url_for('home'))





