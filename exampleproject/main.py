import flask
from spicer import Spicer

site:flask.Flask = flask.Flask(__name__)
site.config["constant_folder"] = "constant"
print(site.template_folder)
spicer:Spicer = Spicer(site)

@site.route("/")
def index() -> str:
	rendered:str = flask.render_template("index.html")
	return spicer.patch(rendered)

site.run(host="0.0.0.0",port=2323)