# README TPC6

O TPC proposto foi desenvolver a aplicação *Flask* desenvolvida na aula de modo que, ao clicar em algum conceito, haja o direcionamento para uma nova página com a sua descrição e as várias traduções.

Para fazer isto, foi criado um novo template chamado designacoes.html onde é apresentada a descrição do conceito e as suas traduções em inglês, espanhol, italiano e francês. Para além disto, foram adicionados 3 botões: um para voltar à página anterior, um para ir para o conceito anterior e outro para avançar para o conceito seguinte. 
Para a funcionalidade de voltar à página anterior foi usada a função *window.history.back()*. Para avançar e retroceder nos termos foram criados alguns scripts de modo a obter o indice do conceito anterior ou seguinte e atualizar a página. Para fazer a atualização da página foi usada a função *window.location.href()*.
Para a estética da página foi usada a *framework Bootstrap* de modo a otimizar o desenvolvimento do *front-end*.

## Dificuldades
A principal dificuldade surgiu aquando do desenvolvimento da funcionalidade de avançar e retroceder nos termos, principalmente a nível de manuseamento dos índices e do dicionário em si.