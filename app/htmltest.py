# Jednostavna skripta za testiranje htmlova napisanih u Jinji

from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def index():
    # Prvi parametar je html koji se prikazuje, main_title je naslov kartice
    return render_template("index.html", main_title="Index")


application.run(debug=True)