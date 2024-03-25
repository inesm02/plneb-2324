from flask import Flask, render_template
import json

app = Flask(__name__)

file = open("conceitos.json", encoding="latin1")
conceitos = json.load(file)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/conceitos")
def listar_Conceitos():
    return render_template("conceitos.html", conceitos = conceitos)

@app.route("/conceitos/<conceito>")
def consultar_Conceitos(conceito):
        return render_template("designacao.html",conceitos = conceitos, conceito = conceito, designacao=conceitos[conceito])


@app.route("/conceitos/<designacao>", methods=["PUT"])
def editar_Conceitos(designacao):
    pass

app.run(host="localhost", port=4002, debug=True)

# ao clicar no conceito aparecer a página do conceitos com traduções, descrições e assim