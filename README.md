*RaCIng*

Equipe:
Arthur Calabria - acvmg
Filipe Santos - fsc5
João Henrique - jhmg
Lucas Felipe - lfla2
Luis Eduardo - lelb2


- ARQUITETURA E ORGANIZAÇÃO DO CÓDIGO
Primeiramente, é importante ressaltar o fato que o projeto como um todo, foi dividido em dois, ou seja, o jogo 2D foi desenvolvido separadamente do jogo 3D, para depois serem unidos em uma única pasta, na qual haveria um arquivo .py capaz de executar, no caso de determinada tecla ter sido pressionada, um dos dois jogos. 
Contudo, mesmo com os desenvolvimentos de cada um desses dois projetos ter sido feito de forma isolada, por requerimentos globais de organização definidos pelo grupo por intermédio do contato e recomendação pelos monitores da disciplina, ambos os códigos são divididos em módulos, que são importados pelos dois módulos principais (main2D e main3D) de modo que seja possível o uso de funções definidas dentro desses arquivos. Destarte, tal técnica foi utilizada de modo a separar cada uma das funcionalidades do código, assim facilitando o processo de “debugging”, logo que, diferentemente do caso em que todas essas funções estivessem juntas em um mesmo arquivo, é possível entender facilmente e sem perda de tempo onde o problema detectado possa estar, de modo que ele possa ser isolado e solucionado eficientemente pela equipe.
Ademais, a organização dos códigos 2D e 3D seguem aproximadamente os mesmos estilos, apenas diferindo no módulo “main”. Desses dois, no primeiro esse arquivo segue uma organização muito mais direta, em que primeiramente é declarado uma série de classes para cada tipo de objeto no jogo, em seguida, são declaradas diversas funções, as quais são de exímia importância tanto pela sinalização de colisões e utilizações dos itens como a exibição de informações durante o jogo e o funcionamento da parte sonora do jogo, aliás toda a parte dos scores e da interface com o usuário, por exemplo a tela de início e fim, funcionam por meio de funções, nesse último caso tais funções estão contidas em módulos, assim como algumas funções de sinalização de colisões que independem de outras funções, o que torna mais fácil a modularização, em seguida é definido o funcionamento básico do jogo, o qual não está disposto em funções, como a definição do tamanho da janela e a importação de imagens, fontes e áudios.
O while loop em que o jogo é executado, no geral a estrutura do código tem uma característica consideravelmente linear, estando disposta de forma bem direta e simples, ao passo que, no segundo, cada componente do código está contido dentro de funções, como o código que exibe o menu principal do jogo, que está contido dentro da função “menu()”, ao passo que o código principal do jogo em sí está contido dentro de outra função, main(), tal que, no corpo principal do código, temos que, sempre que o jogo é iniciado, a função menu() é chamada, inicializando o menu, através do qual é possível chamar o código principal do jogo através do apertar de uma tecla que chama a função main(), depois, dentro de main, caso o jogador morra, a função retorna um valor arbitrário, terminando a execução da função main() e retomando a execução do menu, essencialmente reiniciando o jogo, logo que, para iniciar este mais uma vez, main() teria que ser chamada novamente, colocando o jogador nas mesmas posições iniciais (por essas serem definidas em main()) sempre. Por sua vez, tal estratégia foi adotada de modo a facilitar a localização de cada funcionalidade, ajudando, desse modo, na leitura do código.

- AS FERRAMENTAS, BIBLIOTECAS E FRAMEWORKS UTILIZADOS.
- GITHUB:
Como será descrito em tópicos posteriores, o github foi utilizado de modo a facilitar a troca de códigos entre nossas equipes de programadores, de tal modo que, depois de cumprir suas devidas tarefas dentro do desenvolvimento do código, o membro da equipe em questão poste o código atualizado em seu github, de modo que o membro responsável por modificar o código logo depois destes novos desenvolvimentos possa rapidamente pegar esse código (junto de todos os outros arquivos necessários para rodar o jogo) e modificá-lo, ou adicionar componentes paralelos (como imagens e outros módulos de código) com maior facilidade.
- PARTE  1: FERRAMENTAS	

- REPLIT:
É um complemento do github que foi utilizado em maior escala pelos desenvolvedores do projeto em 2D, que, diferentemente do uso do github, no qual cada desenvolvedor precisa baixar novamente cada versão do código que foi atualizada, permite o desenvolvimento conjunto de dois diferentes desenvolvedores sobre um mesmo código.
VScode e Pycharm:
Foram as duas IDEs utilizadas pelos membros da equipe de desenvolvimento, cada uma proporcionando diferentes vantagens.
ILoveSong
Consiste em uma IA generativa que foi utilizada para desenvolver a trilha sonora do jogo.




- PARTE 2: BIBLIOTECAS

- PYGAME / PYGAME - CE
O uso dessas bibliotecas varia conforme analisamos o código do 2D e do 3D: no primeiro desses, o uso dela pode ser observado em funcionalidades mais elementares do jogo e na obtenção dos inputs do usuário através do teclado, como o “.key.get_pressed()” e o “.key.get_just_pressed()”, por outro lado, na mecânica das colisões entre o jogador e outros objetos,  foram utilizados diversos módulos tanto do pygame, como pygame ce, já que este último é apenas uma versão que recebe mais atualizações, por exemplo o módulo “.spritecollide()”, que junto ao parâmetro “mask” torna as colisões bem mais precisas, logo que são os bits dos sprites que são levados em consideração, outro módulo importante para a fluidez da parte gráfica do jogo em 2D foi o “.get_frect”, que diferente do “.get_rect”, em seguida, para a movimentação, é importante destacar o módulo “.math.Vector2()”, que foi amplamente ao longo do código,  e por fim, dentre vários outros módulos utilizados para a dimensionalização, rotação e coloração dos sprites, fundamentais para tornar o jogo bastante dinâmico. Diferente disso, o jogo tridimensional utiliza essa biblioteca mais como uma ferramenta gráfica, sonora, e capaz de obter o input que o jogador oferece através do teclado, de modo que grande parte do uso dessa biblioteca poderia ter sido substituído por qualquer outra biblioteca gráfica, como, por exemplo, o openGL ou até mesmo o matplotlib.
- NUMBA
Essa biblioteca foi crucial no desenvolvimento do jogo 3D, logo que muitos trechos de seu código podem deixar o jogo consideravelmente lento, de modo que, antes do uso dessa biblioteca, os frames por segundo obtidos no jogo 3D eram consideravelmente baixos, deixando o jogo menos intenso e menos jogável no processo. Nesse aspecto, visando uma maior otimização, importamos essa biblioteca por causa, principalmente, da facilidade de seu uso que, no caso de sua utilização no jogo 3D, consiste apenas na utilização da função “njit”, que deve ser utilizada antes da definição de funções de modo a agilizar sua execução, permitindo um jogo mais fluido.
- NUMPY
Outra biblioteca que foi de extrema importância no jogo 3D, um jogo cuja principal funcionalidade, a renderização do espaço tridimensional, está extremamente conectada às matrizes e aos arrays, duas estruturas cujo uso e manipulação é facilitado imensamente pelo numpy.
- TIME E RANDOM:	
No 2D, RANDOM foi utilizada para auxiliar na seleção aleatória de números usados em índices e posições nas janelas, em que no primeiro caso, foi utilizado a função ‘randint’ para sortear um valor aleatório dentro de um intervalo, o qual define o escopo de uma lista de sprites de carros, com variadas cores, a fim de que sejam gerados carros com cores aleatórias ao longo do jogo, seguindo para o segundo caso, para determinar a disposição dos itens gerados ao longo do eixo horizontal, foi utilizada a função ‘choice’, que retorna um número aleatório entre conjunto pré-definido, que não é necessariamente um intervalo.
Time, no 3D, foi utilizada de modo a criar os delays utilizados para criar determinadas animações, como a explosão, ao passo que random foi utilizada para gerar, de forma pseudo-aleatória, as coordenadas dos itens e das moedas através da função randint().
- OS.PATH:
Utilizada somente no 2D, com o módulo “.join()” a fim de auxiliar a importação de arquivos de imagem, som e fontes de texto.

- DIVISÃO DO TRABALHO
- 2D
Programador principal: jhmg;
Programadores auxiliares: fsc5, lfla2 e lelb2.
- 3D
Programador principal: acvmg;
Programadores auxiliares: jhmg, fsc5, lfla2 e lelb2.
Design de sprites e telas: lelb2, lfla2 e fsc5.
- CONCEITOS APRESENTADOS PELA DISCIPLINA E UTILIZADOS NO PROJETO
Durante a disciplina de IP(Introdução a Programação), introdução a programação, vários métodos de armazenar dados, loops, organização do código foram apresentados. Durante o projeto é notável o uso de estruturas como:

- Listas
- Tuplas
- Funções
- Recursões
- Loops (While e For)
- Condicionais

- LISTAS
Listas foram amplamente utilizadas nas telas de Highscore para manipular a pontuação utilizando de sort() e sort(reverse=true), também utilizou-se o pop e o insert para manipular essas listas e salvar posteriormente no documento TXT.

(vê - se o uso de listas e manipulação das mesmas no nosso código no módulo scores.scorepage).
Observa-se também um vasto uso de listas no armazenamento de coordenadas no caso do jogo 3D(Racing 3D) e no armazenamento e manipulação de sprites em ambos os jogos. conhecimento abordado na lista de listas.

- TUPLAS
Tuplas também são estruturas que foram vastamente utilizadas em nosso código, principalmente porque o próprio pygame exigia o uso de tuplas em vários de seus comandos, mas além disso, o trajeto das IA’s no Racing 3D usa uma lista de tuplas, conhecimento abordado na lista de tuplas e dicionários

(Racing 3D)
Um exemplo do uso de tuplas em nosso código na trajetória das IA 's como mencionado anteriormente.

- FUNÇÕES
Funções são estruturas de organização que foram amplamente utilizadas em todo o escopo dos códigos pois gera variáveis temporárias e consegue dividir bem o código, foi usada amplamente também nos módulos, principalmente utilizando o retorno para determinar se o jogo deveria ser jogado novamente.conhecimento abordado na lista de funções.


No primeiro caso um uso de função nos módulos do jogo e no segundo um caso de uso de função no escopo principal ,“Main” , do código.
(Tela de encerramento Racing 3D  e função do código principal de Racing 3D


- RECURSÕES
Recursões foram utilizadas em situações em que os loops for e while não conseguiam fazer certas operações, como a criação aleatória das coordenadas de itens e das moedas.conhecimento da lista de recursões

aqui é um dos exemplos de uso de recursões.(Racing 3D)

- LOOPS
Loops foram amplamente utilizados por todo o código em ambos os jogos, pois até para iniciar a tela do pygames era necessário um “While True:”, porém usos mais específicos são vistos na leitura dos arquivos do documento TXT e passando essas informações para as listas usando a estrutura FOR.Conhecimento adquirido na lista de Laços de repetição.


(Racing 2D)
Também utilizados na importação de Sprites,usando novamente a estrutura FOR

(Racing 2D)
Exemplo do uso da estrutura WHILE para ativar a invisibilidade do player

(Racing 3D)
E o exemplo de uso “obrigatório” pelo pygame para criar o loop do jogo utilizando o “while true”,porém sua variável era running para permitir o uso de retornos para definir o fim do jogo.

(Racing 2D)

- CONDICIONAIS
Provavelmente as estruturas mais utilizadas em ambos os jogos, são vitais para o funcionamento do jogo e foram utilizadas em todo o escopo dos dois jogos. conhecimento adquirido na lista de condicionais.

(Racing 2D)
um dos incontáveis usos de condicional no item da pílula de encolhimento

- #ERROS, DESAFIOS E LIÇÕES APRESENTADOS PELO PROJETO
-MAIOR ERRO E COMO LIDAMOS COM ELE
-MAIOR DESAFIO E COMO LIDAMOS COM ELE
-LIÇÕES APRENDIDAS

- MAIOR ERRO
Acreditamos que os maiores erros durante o desenvolvimento do jogo tem a ver com a desorganização e com a falta de gerenciamento de pessoas, pois notou-se no decorrer do projeto que várias versões do código estavam sendo desenvolvidas em paralelo, dificultando a integração entre mecanicas criadas por 2 programadores, além disso a pouca utilização inicial da plataforma do github gerou muito esse problema de vários códigos do mesmo jogo com arquivos com nome diferente e variáveis diferentes,e como consequência via-se que só pra voltar ao ritmo era necessário 30 minutos mudando detalhes no código. 
- COMO SUPERAMOS
Ao passar do tempo começamos a fazer uma comunicação mais eficiente e uma divisão de tarefas mais inteligente, de forma a integrar mais facilmente o trabalho de mais de um programador, assim com o uso do github e novas formas de trabalhar em equipe conseguimos nos organizar e diminuir esses problemas. 

- MAIOR DESAFIO
Os maiores desafios do projeto foram provavelmente aprender a utilizar o pygame, cuja sintaxe e lógica eram completamente diferentes ao que estávamos habituados, além de aprender sobre Programação Orientada a Objetos(POO) que não tivemos uma lista para treinar esse conteúdo, e apesar de se utilizar somente o básico inicialmente foi uma barreira, além disso o jogo 3D representou um grande desafio pois ele é extenso em relação tanto a lógica e algoritmo quanto em relação à matemática.
COMO SUPERAMOS
A forma que encontramos para superar foi inicialmente buscar conhecimento sobre como e com o que estávamos trabalhando, então passamos os primeiros dias estudando e tendo ideias do que fazer em relação ao jogo de corrida.
- LIÇÕES APRENDIDAS
Aprendemos a necessidade de manter uma comunicação clara e eficiente com os membros de uma equipe, percebemos que para um bom trabalho ser feito é necessário ir além de bons programadores e bons artistas, é necessário também uma boa gestão do que deve ser feito, principalmente em projetos extensos.Dito isso para sintetizar aprendemos que é necessário uma coordenação eficiente e usar e abusar de plataformas que organizam as versões do código(tal como github e replit).
Também aprendemos como as boas práticas de programação fazem diferença num código extenso, pois quando precisamos alterar dados, imagens e etc… sentimos uma grande dificuldade pois o código não se mostrava bem dividido e com algumas coisas confusas para quem não tinha o olhar treinado.
Conseguimos pontuar também como lição que se houver motivação o bastante, o impossível é o limite, pois com esse prazo do projeto conseguimos aprender e desenvolver 2 jogos utilizando basicamente o conhecimento disponibilizado no youtube. 
Então vê-se que a disciplina de IP foi eficiente em passar à nós alunos a lógica pelo menos introdutória do que seria programar, pois como bem foi dito na primeira aula, sintaxe é somente uma pesquisa, um texto, o que é realmente importante é aprender a pensar como programador e assim conseguir desenvolver tais projetos.






CAPTURAS DE TELA













