from flask import Flask, render_template
from spicer import Spicer

site:Flask = Flask(__name__)
spicer:Spicer = Spicer(site)

@site.route("/")
def index() -> str:
	#render_template()
	#return spicer.render_template("index.html")
	#return spicer.patch( render_template("index.html") )
	return spicer.patch(spicer.render_template("index"))

site.run(host="0.0.0.0",port=2323)