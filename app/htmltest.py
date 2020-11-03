# Jednostavna skripta za testiranje htmlova napisanih u Jinji

from flask import Flask, render_template

application = Flask(__name__)


@application.route("/")
def index_main():
    # Prvi parametar je html koji se prikazuje, main_title je naslov kartice
    return render_template("index.html", main_title="Index")

@application.route("/index.html")
def index():
    return render_template("index.html", main_title="Index")

@application.route("/citavaPrica.html")
def citavaPrica():
    return render_template("citavaPrica.html", main_title="Prica")

@application.route("/price.html")
def price():
    return render_template("price.html", main_title="Price")

@application.route("/makete.html")
def makete():
    return render_template("makete.html", main_title="Makete")

@application.route("/narudzba.html")
def narudzba():
    return render_template("narudzba.html", main_title="Narudzba")

@application.route("/narudzbe.html")
def narudzbe():
    return render_template("narudzbe.html", main_title="Narudzbe")

@application.route("/prihvat_makete.html")
def prihvat_makete():
    return render_template("prihvat_makete.html", main_title="Prihvat makete")

@application.route("/prihvat_price.html")
def prihvat_price():
    return render_template("prihvat_price.html", main_title="Prihvat price")

@application.route("/prijava.html")
def prijava():
    return render_template("prijava.html", main_title="Prijava")

@application.route("/prijedlog_price.html")
def prijedlog_price():
    return render_template("prijedlog_price.html", main_title="Prijedlog price")

@application.route("/registracija.html")
def registracija():
    return render_template("registracija.html", main_title="Registracija")

application.run(debug=True)