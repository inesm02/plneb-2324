## README TPC3 

O código *python* presente no ficheiro TPC3.py tem como objetivo criar um dicionário médico a partir de um ficheiro de texto "dicionario_medico.txt". É realizado o processamento do texto de modo a extrair os termos médicos e as suas descrições e, em seguida, é gerado um ficheiro HTML chamado dicionario_medico.html onde os termos são organizados de forma alfabética e permite uma navegação fácil através de botões para cada letra do alfabeto.

Primeiramente, é aberto o ficheiro de texto em modo de leitura, considerando a codificação UTF-8 para lidar com caracteres especiais. De modo a lidar com as quebras de páginas e marcar os termos médicos com o caracter "@", facilitando o manuseamento do documento, foi usada a função *sub* da bibliotce re.
Depois, é usada a função *findall* para encontrar todos os termos e todas as decrições e armazena-los em listas. Para os termos é usada a expressão regular r'@.+\n([^@]+)' e para as descrições r'@(.+)\n([^@]+)'.

De seguida, é gerada a página web a partir das listas de termos e descrições, utilizando HTML e CSS. É definido um título e subtítulo, são criados botões para cada letra do alfabeto, permitindo a navegação rápida para termos por ela iniciados. Por fim, o conteúdo HTML é escrito num arquivo chamado dicionario_medico.html, que pode ser aberto num navegador web para visualização.

# Dificuldades
A principal dificuldade foi garantir que o texto a partir do qual foram extraidos os termos e as descrições estava bem formatado e estruturado de forma consistente. O maior problema foram as quebras de linha e de página, principalmente quando estas aconteciam no meio de uma descrição.