import flask

site:flask.Flask = flask.Flask(__name__)

spicer:Spicer = Spicer(site)

@site.index("/")
def index() -> str:
	return flask.render_template_string(spicer.render("index.html"))

site.run(host="0.0.0.0",port="2323")