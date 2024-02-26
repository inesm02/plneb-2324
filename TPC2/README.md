O ficheiro Ficha_RE_1_PG53875.py corresponde à resolução da Ficha de Expressões Regulares 1 de Processamento de Linguagem Natural. Uma expressão regular é um método formal de especificar um padrão de texto e que pode ser útil para procura, substituição, validação de formatos e filtragem de informações.

Para isto, foi usado o módulo 're' do Python que é utilizado para manipulação de expressões regulares, fornecendo várias funções que permitem procurar, substituir e manipular strings.

**Exercício 1.1**: para verificar se a palavra 'hello' aparece no início da linha foi usada a função *match* e de maneira a especificar o início da linha foi usado o caracter '^'.

**Exercício 1.2**: para verificar se a 'hello' aparece na linha foi usada a função *search*.

**Exercício 1.3**: para pesquisar todas as ocorrências da palavra 'hello' numa linha foi usada a função *findall* e para não fazer distinção entre palavras escritas com maiúscula ou minúscula foi usada a sequência de caracteres '(?i)'.

**Exercício 1.4**: de modo a substituir as ocorrência da palavra 'hello' com '*YEP*' foi usada a função *sub*, sendo que o primeiro parâmetro é a palavra a ser substituida e o segundo é a palavra pela qual queremos substituir. O *count=0* serve a definir como ilimitado o número de substituições e o *flags=0* serve para indicar que não está a ser feita nenhuma alteração adicional.

**Exercício 1.5**: para fazer uma separação a cada ocorrência de uma vírgula foi usada a função *split*. O campo *maxsplit=0* serve para definir como ilimitado o número de separações a ser feita.

**Exercício 2**: de modo a determinar se uma frase termina com a expressão 'por favor' seguida de um sinal válido de pontuações é usada a função *search*. A expressão regular utilizada foi 'por favor[.!?]+?$'. Os caracteres entre parêntesis retos indicam os sinais de pontuação possíveis, o '+' indica que um ou mais desses caracteres podem estar presentes, o '?' garante que a correspondência é feita com o menir número possível de caracteres e o '$' âncora a expressão no final da linha.

**Exercício 3**: para calcular quantas vezes a palavra 'eu' aparece numa *string* é utilizada a função *findall* que retorna uma lista e depois é utilizada a função *len* para obter o tamanho da lista.

**Exercício 4**: de modo a substituir todas as ocorrências de 'LEI' numa linha pelo nome do curso dado à função é utilizada a função *sub*, em que o primeiro parâmetro é a palavra a ser substituída, o segundo é a palavra pela qual vai ser substituída e o terceiro é a frase(ambos fornecidos à função).

**Exercício 5**: para calcular a soma dos números fornecidos numa *string* separados por vírgulas, é usada a função *split*. Devido aos elementos presentes na lista serem *strings* é necessário torna-los em números usando a função *float*. Por fim, é usada a função *sum* para calcular a soma.

**Exercício 6**: de modo a extrair todos os pronomes pessoais presentes numa frase com atenção a maiúsculas e minúsculas é usada a função *findall*, a expressão regular é '\b(eu|tu|ele|ela|nós|vós|eles|elas)\b' (\b indica que não podem haver outros caracteres alfanuméricos adjacentes) e foi usado *flag=re.IGNORECASE* para não haver distinção entre maiúsculas e minúsculas.

**Exercício 7**: para determinar se uma *string* é um nome válido, ou seja, se começa por uma letra e apenas contém letras, números ou underscores foi usada a função *match* e a expressão regular '^[a-zA-Z_][a-zA-Z0-9_]*$'. O caracter '^' restringe a que no início da *string* haja uma letra.

**Exercício 8**: de modo a extrair todos os números inteiros presentes numa *string*, quer seja positivo ou negativo foi usada a função *findall* e a expressão regular '\b\s-?\d+\b'. O conjunto de caracteres '\s' indica o espaço em branco e o conjunto de caracteres '-?' indica que pode ou não ter o hífen que indica que o número é negativo.

**Exercício 9**: para substituir todos os espaços numa *string* por *underscores* foi usada a função *sub* e a expressão regular '\s+' que indica que pode haver um ou mais espaços em branco.

**Exercício 10**: de modo a dividir os códigos postais de uma lista com base no hífen foi usada a função *split*. Por cada elemento da lista inicial, foi feita a divisão e a lista de 2 elementos resultante foi adicionada a outra chamada codigos. Esta trata-se de uma lista de pares.