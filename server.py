from flask import Flask, render_template, request, session, flash, g, redirect, url_for
from flask_restful import reqparse, abort, Api, Resource
import os
import json
from datetime import date, datetime

#from models import Cat, Purch, db

app = Flask(__name__)
api = Api(app)

app.config.update(dict(SEND_FILE_MAX_AGE_DEFAULT=0))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'server.db')

app.config.from_object(__name__)
app.config.from_envvar('BUDGET_SETTINGS', silent=True)
app.debug = True

#db.init_app(app)

#@app.cli.command('initdb')
#def initdb_command():
	#db.drop_all()
	#db.create_all()
	#db.session.commit()
	#print("Initialized the database")

@app.route("/")
def home():
	return render_template("home.html")
	
@app.route("/about_me")
def about():
	return render_template("about.html")
	
@app.route("/education")
def education():
	return render_template("education.html")
	
@app.route("/projects")
def projects():
	return render_template("projects.html")
	
@app.route("/links")
def links():
	return render_template("links.html")
	
@app.route("/experience")
def experience():
	return render_template("experience.html")
	
@app.route("/login")
def admin_login():
	return None