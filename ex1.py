def startboard():
    # Inicializa o tabuleiro 4x4
    tabuleiro = [[' ' for _ in range(4)] for _ in range(4)]
    return tabuleiro

def showboard(tabuleiro):
    # Exibe o tabuleiro
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * 13)

def makemove(tabuleiro, jogador, linha, coluna):
    # Realiza a jogada de um jogador no tabuleiro
    if 0 <= linha < 4 and 0 <= coluna < 4 and tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

def checkwinner(tabuleiro, jogador):
    # Checa se o jogador venceu
    # Checa linhas
    for linha in tabuleiro:
        if all(cell == jogador for cell in linha):
            return True

    # Checa colunas
    for coluna in range(4):
        if all(tabuleiro[i][coluna] == jogador for i in range(4)):
            return True

    # Checa diagonais
    if all(tabuleiro[i][i] == jogador for i in range(4)):
        return True
    if all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False

def jogodavelha():
    # Função que inicia o jogo
    tabuleiro = startboard()
    actualplayer = 'X'
    moves = 0

    while True:
        showboard(tabuleiro)
        print(f"Jogador {actualplayer}, é sua vez!")

        linha = int(input("Digite o número da linha (0 a 3): "))
        coluna = int(input("Digite o número da coluna (0 a 3): "))

        if makemove(tabuleiro, actualplayer, linha, coluna):
            moves += 1

            if checkwinner(tabuleiro, actualplayer):
                showboard(tabuleiro)
                print(f"Parabéns! Jogador {actualplayer} venceu!")
                break

            if moves == 16:
                showboard(tabuleiro)
                print("O jogo empatou!")
                break

            actualplayer = 'O' if actualplayer == 'X' else 'X'

        else:
            print("Jogada inválida. Tente novamente.")

if __name__ == "__main__":
    jogodavelha()
