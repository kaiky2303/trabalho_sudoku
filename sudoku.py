import copy

def tabuleiro_facil():
    return [
        [0, 0, 4, 8, 0, 0, 1, 0, 7],
        [6, 7, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 9, 1],
        [2, 0, 9, 0, 0, 6, 5, 0, 0]
    ]

def tabuleiro_medio():
    return [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0]
    ]

def tabuleiro_dificil():
    return [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 2, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0]
    ]

def tabuleiro_muito_dificil():
    return [
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 2, 0, 0, 0, 0, 0, 0, 0]
    ]

def exibir_tabuleiro(tabuleiro):
    print("   A B C   D E F   G H I")
    for i, linha in enumerate(tabuleiro):
        if i % 3 == 0 and i != 0:
            print("   ------+-------+------")
        linha_formatada = ""
        for j, num in enumerate(linha):
            if j % 3 == 0 and j != 0:
                linha_formatada += "| "
            linha_formatada += str(num) if num != 0 else "."
            linha_formatada += " "
        print(f"{i+1}  {linha_formatada}")

def posicao_valida(linha, coluna, numero, tabuleiro):
    if numero in tabuleiro[linha]:
        return False
    for i in range(9):
        if tabuleiro[i][coluna] == numero:
            return False
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(3):
        for j in range(3):
            if tabuleiro[inicio_linha + i][inicio_coluna + j] == numero:
                return False
    return True

def jogo_completo(tabuleiro):
    for i in range(9):
        for j in range(9):
            num = tabuleiro[i][j]
            if num == 0:
                return False
            tabuleiro[i][j] = 0
            if not posicao_valida(i, j, num, tabuleiro):
                tabuleiro[i][j] = num
                return False
            tabuleiro[i][j] = num
    return True

def ler_entrada():
    while True:
        entrada = input("Digite a posição (ex: A1) e o número (ex: A1 5): ").upper()
        if len(entrada) >= 4:
            pos, num = entrada[:2], entrada[3:]
            if pos[0] in "ABCDEFGHI" and pos[1].isdigit() and num.isdigit():
                coluna = "ABCDEFGHI".index(pos[0])
                linha = int(pos[1]) - 1
                numero = int(num)
                if 0 <= linha < 9 and 1 <= numero <= 9:
                    return linha, coluna, numero
        print("Entrada inválida. Tente novamente.")

def selecionar_dificuldade():
    while True:
        print("\nSelecione o modo de dificuldade:")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Difícil")
        print("4 - Muito Difícil")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            return tabuleiro_facil()
        elif escolha == '2':
            return tabuleiro_medio()
        elif escolha == '3':
            return tabuleiro_dificil()
        elif escolha == '4':
            return tabuleiro_muito_dificil()
        elif escolha == '5':
            print("Saindo do jogo. Até logo!")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

def jogar():
    tabuleiro = selecionar_dificuldade()
    tabuleiro_original = copy.deepcopy(tabuleiro)

    while True:
        exibir_tabuleiro(tabuleiro)

        if jogo_completo(tabuleiro):
            print("\nParabéns! Você completou o Sudoku corretamente! 🏆")
            break

        linha, coluna, numero = ler_entrada()

        if tabuleiro_original[linha][coluna] != 0:
            print("Você não pode alterar um número fixo do tabuleiro.")
            continue

        if posicao_valida(linha, coluna, numero, tabuleiro):
            tabuleiro[linha][coluna] = numero
        else:
            print("Jogada inválida! Número conflitante com linha, coluna ou subgrade.")

if __name__ == "__main__":
    jogar()
