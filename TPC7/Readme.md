# README TPC7

O objetivo do TPC de Processamento de Linguagem Natural desta semana era implementar novas funcionalidades na aplicação Flask dos conceitos médicos, nomeadamente, um motor de pesquisa na página dos conceitos e uma página referente a uma datatable, onde fossem apresentados todos os conceitos. 

## Motor de pesquisa
Primeiro, foi criado um formulário HTML que tem o atributo *action* "/conceitos", o que significa que quando o formulário for submetido, os dados serão enviados para o URL "/conceitos". O método de envio é definido como GET, o que significa que os dados do formulário serão anexados ao URL como parâmetros de consulta. O campo de *input* é um campo de texto onde o utilizador pode inserir a sua pesquisa. O atributo *name* está definido como *search* então quando o formulário for submetido, o valor inserido no campo será enviado com a chave *search*. Quando o botão de *submit* é pressionado, os dados do formulário são enviados para o URL especificado no atributo *action*. Para além disso, foi adionado um botão de "Limpar pesquisa" para que o utilizador consiga voltar para a página com todos os conceitos.

## Datatable
Primeiro, foi criada uma tabela HTML com um cabeçalho (*<thead>*) com seis colunas: conceito, descrição, inglês, espanhol, italiano e francês. Dentro do corpo da tabela existe um ciclo *for* que itera o dicionário "conceitos" e que, para cada conceito, é adicionada uma nova linha. 