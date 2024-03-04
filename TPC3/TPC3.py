import re

file = open("dicionario_medico.txt",  encoding = "utf-8")
texto = file.read()

texto = re.sub(r'\n\f', "",texto)
texto = re.sub(r'\f',"",texto)

texto = re.sub(r'\n\n(.+\n)', r'\n\n@\1', texto)
texto = re.sub(r'(\n?@)(\d+)', r"\2", texto)
#print(texto)

descricoes = []
descricoes = re.findall(r'@.+\n([^@]+)',texto)

termos = []
termos = re.findall(r'@(.+)\n([^@]+)',texto)


#Gerar HTML
titulo = "<div style='text-align: center; background-color: #F0FFF0; padding: 10px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'><h1 style='color: #333;'> DICIONÁRIO MÉDICO </h1></div>"
descricao = "<p style='text-align: center; color: #666;'> [ Dicionário médico desenvolvido na disciplina de PLNEB ] </p>"

html = f"<html><head><title>Dicionário Médico</title><style>.rodape {{ position: fixed; left: 54; bottom: 0; width: 90%; background-color: #008080;  padding: 5px;font-size: 14px; }}</style></head><body>{titulo}{descricao}"

# Adicionar botões para cada letra
html += "<div style='text-align: center; margin-bottom: 20px;'>"
for letra in sorted(set(termo[0][0].upper() for termo in termos)):
    html += f"<button type='button' onclick='rolarParaLetra(\"{letra}\")' style='margin: 3px 3px; padding: 15px 23px;font-size: 19px; background-color: #F0FFF0; color: #008080; border: dotted; border-radius: 8px; cursor: pointer;font-family: Georgia;'>{letra}</button>"
html += "</div>"

# Adicionar termos médicos para cada letra
for letra in sorted(set(termo[0][0].upper() for termo in termos)):
    html += f"<div id='letra_{letra}' style='margin: 0 auto; width: 80%;'>"
    for termo in termos:
        if termo[0][0].upper() == letra:
            html += f"<div style='margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;'><h2 style='color: #333;'>{termo[0]}</h2>"
            html += f"<p style='color: #666;'>Definição: {termo[1]}</p></div>"
    html += "</div>"

html += "</body><script>function rolarParaLetra(letra) { var elemento = document.getElementById('letra_' + letra); if (elemento) { elemento.scrollIntoView({ behavior: 'smooth' }); } }</script></html>"
rodape = "<footer class='rodape'><div style='color: white;float: left;'>Processamento de Linguagem Natural em Engenharia Biomédica 23/24</div><div style='color: white;float: right;'>Inês Margarida Sousa Mendes, pg53875</div></div>"
html += rodape
html += "</body></html>"

# Escrever o HTML num arquivo
with open("dicionario_medico.html", "w") as file_out:
    file_out.write(html)