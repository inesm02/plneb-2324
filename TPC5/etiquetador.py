import json
import re

file_conceitos = open("conceitos_v2.json", encoding="latin1")
file_livro = open("LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="utf-8")

texto = file_livro.read()
conceitos = json.load(file_conceitos)
texto = re.sub(r'\n',r'<br>',texto)
texto = re.sub(r'\f',r'<hr>',texto)
blacklist=["e", "de", "para", "pelo", "os", "são"]

conceitos_min = {chave.lower(): conceitos[chave] for chave in conceitos}
def etiquetador(matched):
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()
    if palavra in conceitos and palavra not in blacklist:
        descricao = conceitos[palavra]['desc']
        traducao = conceitos[palavra]['en']
        etiqueta = f"<a class='etiqueta' href='' title='En - {traducao}\nDescrição - {descricao}'>{original}</a>"
        return etiqueta
    else:
        return original

expressao = r'[\wáéçãóõàíêâú]+'
texto = re.sub(expressao, etiquetador, texto)
file_out=open("livro.html", "w", encoding="utf-8")
print(texto, file=file_out)




