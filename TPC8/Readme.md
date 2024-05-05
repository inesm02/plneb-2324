# README TPC 8
O objetivo do TPC desta semana tinha como objetivo explorar a aplicação de modelos Word2Vec nos textos "Harry_Potter_Camara_Secreta-br.txt" e "Harry_Potter_e_A_Pedra_Filosofal.txt" e extrair informações semânticas e relacionamentos entre palavras.

## Conteúdo
Inicialmente é lido o conteúdo de cada ficheiro e feita a tokenização em listas de palavras. De seguida, são treinados dois modelos usando os textos tokenizados, cada um destes com 3 combinações de parâmetros diferentes de modo a explorar qual seria o melhor.

No geral, a combinação de parâmetros 1 mostrou-se ser a melhor, principalmente nos casos de *most similar* e *similarity*.
