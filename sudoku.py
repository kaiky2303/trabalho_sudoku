import random
import copy

class Tabuleiro:
    def __init__(self, matriz):
        self.matriz = matriz
        self.original = copy.deepcopy(matriz)

    def exibir(self):
        print("\n   A B C   D E F   G H I")
        for i, linha in enumerate(self.matriz):
            if i % 3 == 0 and i != 0:
                print("   ------+-------+------")
            linha_texto = ""
            for j, v in enumerate(linha):
                if j % 3 == 0 and j != 0:
                    linha_texto += "| "
                linha_texto += str(v) if v != 0 else "."
                linha_texto += " "
            print(f"{i+1}  {linha_texto}")

    def posicao_valida(self, linha, coluna, numero):
        if numero in self.matriz[linha]:
            return False

        for l in range(9):
            if self.matriz[l][coluna] == numero:
                return False

        il = (linha // 3) * 3
        ic = (coluna // 3) * 3

        for i in range(3):
            for j in range(3):
                if self.matriz[il + i][ic + j] == numero:
                    return False

        return True

    def jogo_completo(self):
        for i in range(9):
            for j in range(9):
                n = self.matriz[i][j]
                if n == 0:
                    return False

                self.matriz[i][j] = 0
                valido = self.posicao_valida(i, j, n)
                self.matriz[i][j] = n

                if not valido:
                    return False

        return True

    def inserir_numero(self, linha, coluna, numero):
        if self.original[linha][coluna] != 0:
            return False, "Essa casa não pode ser alterada."

        if not self.posicao_valida(linha, coluna, numero):
            return False, "Movimento inválido!"

        self.matriz[linha][coluna] = numero
        return True, "Número inserido!"


class GeradorSudoku:

    @staticmethod
    def gerar_completo():
        """Gera um sudoku COMPLETO usando backtracking."""
        tab = [[0] * 9 for _ in range(9)]

        def resolver():
            for i in range(9):
                for j in range(9):
                    if tab[i][j] == 0:
                        numeros = list(range(1, 10))
                        random.shuffle(numeros)

                        for n in numeros:
                            if GeradorSudoku.valido(tab, i, j, n):
                                tab[i][j] = n
                                if resolver():
                                    return True
                                tab[i][j] = 0
                        return False
            return True

        resolver()
        return tab

    @staticmethod
    def valido(tab, linha, coluna, numero):
        if numero in tab[linha]:
            return False

        for i in range(9):
            if tab[i][coluna] == numero:
                return False

        il = (linha // 3) * 3
        ic = (coluna // 3) * 3

        for i in range(3):
            for j in range(3):
                if tab[il + i][ic + j] == numero:
                    return False

        return True

    @staticmethod
    def remover_numeros(tab, dificuldade):
        """Remove números conforme a dificuldade."""
        removidos = {
            "fácil": 35,
            "médio": 45,
            "difícil": 55
        }

        qtd = removidos[dificuldade]

        tabuleiro = copy.deepcopy(tab)

        while qtd > 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)

            if tabuleiro[i][j] != 0:
                tabuleiro[i][j] = 0
                qtd -= 1

        return tabuleiro


class SudokuGame:
    def __init__(self):
        self.tabuleiro = None

    def selecionar_dificuldade(self):
        while True:
            print("\nSelecione a dificuldade:")
            print("1 - Fácil")
            print("2 - Médio")
            print("3 - Difícil")
            print("4 - Sair")

            esc = input("Escolha: ")

            if esc == "1":
                dificuldade = "fácil"
            elif esc == "2":
                dificuldade = "médio"
            elif esc == "3":
                dificuldade = "difícil"
            elif esc == "4":
                exit()
            else:
                print("Opção inválida!")
                continue

            completo = GeradorSudoku.gerar_completo()
            incompleto = GeradorSudoku.remover_numeros(completo, dificuldade)

            self.tabuleiro = Tabuleiro(incompleto)
            return

    def ler_entrada(self):
        while True:
            entrada = input("Digite posição e número (ex: A1 5): ").upper()

            try:
                pos, num = entrada.split()
                coluna = "ABCDEFGHI".index(pos[0])
                linha = int(pos[1]) - 1
                numero = int(num)

                if 0 <= linha < 9 and 1 <= numero <= 9:
                    return linha, coluna, numero

            except:
                pass

            print("Entrada inválida!")

    def jogar(self):
        self.selecionar_dificuldade()

        while True:
            self.tabuleiro.exibir()

            if self.tabuleiro.jogo_completo():
                print("\n PARABÉNS! Você ganhou!")
                break

            linha, coluna, numero = self.ler_entrada()

            ok, msg = self.tabuleiro.inserir_numero(linha, coluna, numero)
            print(msg)

if __name__ == "__main__":
    SudokuGame().jogar()
