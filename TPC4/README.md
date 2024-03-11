# README TPC4

O TPC proposto para esta semana, passava pela criação de uma página html acerca de um hobby. Assim sendo, escolhi criar uma página acerca de viagens, visto que é uma coisa que gosto muito e que já fiz algumas vezes. A ideia por detrás da página foi: ter um cabeçalho inicial; uma secção de "Sobre mim"; uma espécie de menu onde o utilizador poderia escolher ir diretamente para uma determinada viagem; um conjunto de secções onde existem fotos e um pequeno texto sobre a viagem; por fim, um rodapé inferior.

Para começar, o título da página exibido na barra de título do navegador foi definido como "Blog de Viagens".

### Styling
O styling usando CSS foi definido no mesmo documento html que o resto da página. Nesta secção foram definidos todos os parâmetros que têm a ver com estilos de letra, cores, tamanhos, posicionamentos, etc. Isto foi feito através da criação de classes e da especificação dos seus parâmetros.

### Body
Nesta secção do código está presente todo o conteúdo visível da página.

### Rodapé superior
Este rodapé trata-se de uma barra muito fininha com texto à esquerda e à direita.

### Header 
No header estão presentes o título da página "Viaja comigo" e uma imagem.

### Secção "Sobre mim"
Aqui é usada a classe "container" para agrupar a imagem e o respetivo texto.

### Menu de viagens
Nesta secção estão presentes diversas fotos com o local e a data da viagem que são clicáveis. Também foi adicionada uma interação com o rato em que quando o utilizador passa o rato por cima da imagem esta aumenta de tamanho. Esta funcionalidade está presnete em todas as outras imagens da página. Aquando do click, a página rola automaticamente para a secção respetiva. Para isto foi usado uma pequena função chamada scrollTosection que aceita um parâmetro "sectionID" que representa o ID da secção para a qual queremos que a página role. Dentro desta função é obtida a referência para o elemento HTML com o ID especificado, e de seguida é usado o "window.scrollTo()" que é um método do objeto "window". Para além disto, é indicado que a posição para a qual a página vai rolar é a posição superior da secção e que o behaviour vai ser smooth. Este menu está entre duas linhas horizontais usando o Horizontal Rule "('<hr>')".

### Secções sobre as viagens
De seguida são apresentadas todas as secções relativas à viagens, cada uma com o seu ID. Aqui é usada a classe "container" de novo para agrupar o texto sobre a viagem e o grupo de imagens. 

### Rodapé inferior
Este rodapé é muito similar ao superior, também com texto à esquerda e à direita.

## Processo e dificuldades
Em geral, o processo de criação da página foi muito interessante, principalmente porque, sendo o tema livre, houve a possibilidade de escolher algo do nosso interesse. No início senti algumas dificuldades no processo criativo, a imaginar como queria que ficasse a minha página mas eventualmente surgiram ideias. Outro aspeto em que senti algumas dificuldades foi na conjugação da imagem com o texto, nomeadamente, a definição da posição de cada coisa e o alinhamento.