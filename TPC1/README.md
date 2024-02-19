No ficheiro anagramas.py existe um código Python que identifica anagramas num ficheiro de texto. Um anagrama é uma palavra formada pela rearranjo das letras de outra palavra. O código realiza as seguintes etapas:

- Abre e lê o ficheiro de texto.

- Remove a pontuação e converte o texto para minúsculas.

- Divide o texto em palavras individuais (tokens).

- Identifica anagramas dentro da lista de palavras através da função VerificaAnagramas. Esta função recebe uma lista de palavras como entrada e retorna um dicionário onde as chaves são os anagramas encontrados (as letras das palavras ordenadas alfabeticamente) e os valores são listas das palavras originais que são anagramas entre si. Esta itera sobre cada palavra na lista e verifica se ela é um anagrama de qualquer palavra subsequente. Se encontrar um anagrama, armazena-o no dicionário resultante. Durante o processo, mantém um conjunto de palavras já verificadas para evitar duplicados. Por fim, retorna o dicionário com os anagramas encontrados.

- Imprime os anagramas encontrados.  