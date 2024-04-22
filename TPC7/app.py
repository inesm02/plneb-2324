from flask import Flask, render_template, request
import json
import os


app = Flask(__name__)

file = open("conceitos.json", encoding="CP1252")
conceitos = json.load(file)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/conceitos")
def listar_Conceitos():
    search_query = request.args.get('search')
    if search_query:
        # Filtrar os conceitos com base na pesquisa
        resultados = {key: value for key, value in conceitos.items() if search_query.lower() in key.lower()}
        return render_template("conceitos.html", conceitos=resultados)
    else:
        return render_template("conceitos.html", conceitos=conceitos)

@app.route("/conceitos/<conceito>")
def consultar_Conceitos(conceito):
    if conceito in conceitos.keys():
        return render_template("designacao.html",conceitos = conceitos, conceito = conceito, designacao=conceitos[conceito])
    else:
        mensagem = f"O conceito {conceito} não existe no dicionário."
        return render_template("erro.html", mensagem = mensagem)

@app.route("/conceitos", methods = ["POST"])
def adicionar_conceitos():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    en = request.form.get("en")
    es = request.form.get("es")
    it = request.form.get("it")
    fr = request.form.get("fr")
    conceitos[designacao] = {"desc": designacao, "en": en, "es": es, "it": it, "fr": fr}
    return render_template("conceitos.html", conceitos = conceitos)

@app.route("/conceitos/<conceito>", methods = ["DELETE"])
def delete_conceitos(conceito):
    print("AAAAAAAAAAAAAAAAAAAAAA")
    os.rename("conceitos.json", "conceitos_backup.json")
    file_out = open("conceitos.json", "w")
    del conceitos[conceito]
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    print("@@@@@@@@@@@@@@@@@@@@@2")
    return render_template("conceitos.html", conceitos=conceitos)



@app.route("/conceitos/<designacao>", methods=["PUT"])
def editar_Conceitos(designacao):
    pass

@app.route("/table")
def table():
    return render_template("table.html", conceitos=conceitos)

app.run(host="localhost", port=4002, debug=True)
