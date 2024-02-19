
filename = "CIH Bilingual Medical Glossary English-Spanish.txt"
file = open(filename, "r", encoding = "utf-8")
text = file.read()

text.replace("."," ")
text.replace(","," ")
text.replace("-"," ")
text.replace(":"," ")
text.replace("/"," ")
text.replace("'"," ")
text.replace("("," ")
text.replace(")"," ")
text = text.lower()

tokens = text.split()

def anagram(p1,p2):
    return sorted(p1.lower()) == sorted(p2.lower())


def VerificaAnagrama(s):
    PalavrasVerificadas = set()
    Anagramas = {}

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] not in PalavrasVerificadas and anagram(s[i],s[j]):
                palavra_chave = ''.join(sorted(s[i]))
                if palavra_chave not in Anagramas:
                    Anagramas[palavra_chave] = [s[i]]
                else:
                    Anagramas[palavra_chave].append(s[i])
                PalavrasVerificadas.add(s[i])

    return Anagramas

resultado = VerificaAnagrama(tokens)
for chave, valores in resultado.items():
    print(f'{chave}: {valores}')
