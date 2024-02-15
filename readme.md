## Descrição:
Este programa Python simula um ambiente de jogo simples onde um sprite jogador pode se mover para a esquerda, direita e pular em uma tela, enquanto evita colisões com sprites inimigos.

## Arquivos:
**classes.py:** Contém as definições de classe para os objetos Screen e Sprite usados no jogo.
**modules.py:** Inclui funções auxiliares e a lógica principal do jogo para controlar o movimento do jogador, lidar com a entrada do usuário e gerenciar sprites inimigos.
**game.py:** O script principal onde o jogo é inicializado, sprites são criados e o loop do jogo é executado.

## Uso:
Para executar o jogo, execute o script **game.py** usando Python. Certifique-se de ter o Python instalado no seu sistema.

## Controles:
**Mover para a Esquerda:** Pressione a tecla 'a'.
**Mover para a Direita:** Pressione a tecla 'd'.
**Pular:** Pressione a tecla 'w'.
**Sair do Jogo:** Pressione a tecla 'q'.

## Jogabilidade:
O sprite do jogador começa no canto inferior esquerdo da tela.
Navegue com o sprite do jogador para evitar colisões com sprites inimigos que se movem em sua direção.
Colete pontos à medida que o jogo avança.
O jogo termina quando o jogador colide com um sprite inimigo ou pressiona 'q' para sair.

## Objetivo:
O objetivo do jogo é chegar no maior recorde pessoal possível.
Não fiz com que a velocidade aumente com o tempo, então a missão principal é "sobreviver".

## Perguntas adicionais:
### Por que o Sprite herda de Screen?
O sprite é uma herança de screen pois o mesmo também possui o objetivo de ser mostrado na tela.
Ele Utiliza os mesmos atributos de screen para poder ser montado assim como uma screen, porém, com alguns
métodos a mais. Logo, todo Sprite é uma Screen mas nem toda Screen é um Sprite


