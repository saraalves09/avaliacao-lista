def inicializar_tabuleiro(n):
    # Inicia um tabuleiro NxN
    tabuleiro = [[' ' for _ in range(n)] for _ in range(n)]
    return tabuleiro

def showboard(tabuleiro):
    # Exibe o tabuleiro
    n = len(tabuleiro)
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * (4 * n - 1))

def makemove(tabuleiro, jogador, linha, coluna):
    # Realiza a jogada no tabuleiro.
    n = len(tabuleiro)
    if 0 <= linha < n and 0 <= coluna < n and tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

def checkwinner(tabuleiro, jogador):
    # Checa se o jogador venceu o jogo.
    n = len(tabuleiro)
    
    # Checa colunas/linhas
    for i in range(n):
        if all(tabuleiro[i][j] == jogador for j in range(n)) or all(tabuleiro[j][i] == jogador for j in range(n)):
            return True
    
    # Checa diagonais
    if all(tabuleiro[i][i] == jogador for i in range(n)):
        return True

    if all(tabuleiro[i][n - 1 - i] == jogador for i in range(n)):
        return True

    return False

def jogodavelha():
    """
    Função principal que inicia o jogo da velha NxN.
    """
    n = int(input("Digite o tamanho do tabuleiro (NxN): "))
    tabuleiro = inicializar_tabuleiro(n)
    actual_player = 'X'
    moves = 0

    while True:
        showboard(tabuleiro)
        print(f"Jogador {actual_player}, é sua vez!")

        linha = int(input("Digite o número da linha (0 a {}): ".format(n - 1)))
        coluna = int(input("Digite o número da coluna (0 a {}): ".format(n - 1)))

        if makemove(tabuleiro, actual_player, linha, coluna):
            moves += 1

            if checkwinner(tabuleiro, actual_player):
                showboard(tabuleiro)
                print(f"Parabéns! Jogador {actual_player} é o vencedor!")
                break

            if moves == n * n:
                showboard(tabuleiro)
                print("Deu empate!")
                break

            actual_player = 'O' if actual_player == 'X' else 'X'

        else:
            print("Jogada inválida. Tente novamente.")

if __name__ == "__main__":
    jogodavelha()
