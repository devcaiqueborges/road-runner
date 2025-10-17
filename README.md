# Road Runner - Jogo de Corrida 2D em Python

<p align="center">
  <img src="https://github.com/devcaiqueborges/road-runner/blob/main/images/demonstracao.gif?raw=true" alt="Demonstração do Jogo" width="300"/>
</p>

> **Nota:** Este projeto foi desenvolvido como a Atividade Prática para a disciplina de Linguagem de Programação Aplicada do centro universitário **UNINTER**. O objetivo foi criar uma demo jogável de um jogo 2D utilizando a linguagem Python e a biblioteca Pygame.

## 📜 Sobre o Projeto

Este é um jogo simples de corrida infinita onde o jogador controla um carro que deve desviar de obstáculos que aparecem aleatoriamente na pista. A pontuação é baseada no tempo de sobrevivência e, ao colidir, uma tela de "Game Over" é exibida com a opção de reiniciar a partida.

## ✨ Funcionalidades

-   **Movimentação do Jogador:** Mude de faixa para a esquerda e direita para desviar dos carros.
-   **Geração de Obstáculos:** Carros inimigos são gerados aleatoriamente em diferentes faixas e velocidades.
-   **Pista Infinita:** O cenário da pista se move continuamente, criando uma ilusão de movimento infinito.
-   **Sistema de Pontuação:** A pontuação aumenta a cada segundo que o jogador sobrevive na pista.
-   **Tela de Game Over:** Ao colidir, o jogo termina e exibe a pontuação final, com opções para reiniciar ou sair.
-   **Música de Fundo:** Uma trilha sonora para deixar a jogabilidade mais divertida.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3
-   **Biblioteca:** Pygame (para a lógica do jogo, gráficos e som)

## 🚀 Como Executar o Projeto

Existem duas maneiras de executar o jogo: usando o **executável** (mais simples, não requer Python) ou rodando o **código-fonte** (necessário para desenvolvedores).

### Opção 1: Executar a Versão Compilada (Recomendado para Jogar)

Você pode rodar o jogo diretamente a partir do executável, sem a necessidade de instalar o Python ou suas dependências.

1.  **Baixe o Projeto:**
    ```bash
    git clone [https://github.com/devcaiqueborges/road-runner.git](https://github.com/devcaiqueborges/road-runner.git)
    # OU baixe o arquivo ZIP do repositório no GitHub.
    ```

2.  **Navegue até a pasta do executável:**
    O executável `main.exe` e os recursos (`assets`) estão localizados dentro da pasta `dist` (distribuição).
    ```bash
    cd road-runner/dist
    ```

3.  **Execute o Jogo:**
    Certifique-se de que a pasta `assets` esteja presente no mesmo diretório que o `main.exe`.
    * **No Windows:** Dê um **duplo clique** no arquivo `main.exe`.
    * **No Terminal:**
        ```bash
        ./main.exe
        ```

### Opção 2: Executar a Partir do Código-Fonte (Para Desenvolvedores)

Para rodar o projeto a partir do código-fonte, você precisará ter o ambiente de desenvolvimento Python configurado.

**Pré-requisitos:**
* Ter o [Python 3](https://www.python.org/downloads/) instalado.
* Ter o `pip` (gerenciador de pacotes do Python) instalado.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/devcaiqueborges/road-runner.git](https://github.com/devcaiqueborges/road-runner.git)
    ```

2.  **Navegue até a pasta raiz do projeto:**
    ```bash
    cd road-runner
    ```

3.  **Instale as dependências (Pygame):**
    ```bash
    pip install -r requirements.txt
    ```
    *(Se você ainda não tem um `requirements.txt`, pode criá-lo com o comando `pip freeze > requirements.txt` no seu terminal)*

4.  **Execute o jogo:**
    ```bash
    python main.py
    ```
