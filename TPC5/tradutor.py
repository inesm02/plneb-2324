from deep_translator import GoogleTranslator
import json
import re

file = open("conceitos.json", encoding="utf-8")
conceitos = json.load(file)


novo_dicti = {}

i=0
for designacao_pt in conceitos:
    print(i)
    conceitos[designacao_pt]= re.sub(r"\n",r"",conceitos[designacao_pt])
    designacao_en = GoogleTranslator(source='pt', target='en').translate(designacao_pt)
    novo_dicti[designacao_pt] = {"desc": conceitos[designacao_pt], "en": designacao_en}
    i+=1

file_out = open("conceitos_v2.json", "w")
json.dump(novo_dicti, file_out, indent=4, ensure_ascii = False)

#tpc : pegar no ficheiro txt de termos traduzidos e fazer com que ao passar o rato por cima do termo apareça a "tradução: ____" e na linha seguinte a "descrição: ___"