import flask
from flask import Flask
from flask_spicer import Spicer

site:Flask = Flask(__name__)
spicer:Spicer = Spicer(site)

@site.route("/")
def index():
	# Any of the two following ways renders & patches the template + any spices
	#return spicer.patch( flask.render_template("index.html") )
	return spicer.render_template("index")

@site.route("/home")
def home():
	return spicer.render_template("home")

@site.route("/about")
def about():
	return spicer.render_template("about")

site.run(host="0.0.0.0",port=2323)