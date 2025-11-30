import random
import copy

class GeradorSudoku:
    @staticmethod
    def gerar_completo():
        tab = [[0]*9 for _ in range(9)]
        def resolver():
            for i in range(9):
                for j in range(9):
                    if tab[i][j] == 0:
                        numeros = list(range(1,10))
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
        il, ic = (linha//3)*3, (coluna//3)*3
        for i in range(3):
            for j in range(3):
                if tab[il+i][ic+j] == numero:
                    return False
        return True

    @staticmethod
    def remover_numeros(tab, dificuldade):
        removidos = {"fácil": 35, "médio": 45, "difícil": 55}
        qtd = removidos[dificuldade]
        tabuleiro = copy.deepcopy(tab)
        while qtd > 0:
            i,j = random.randint(0,8), random.randint(0,8)
            if tabuleiro[i][j] != 0:
                tabuleiro[i][j] = 0
                qtd -= 1
        return tabuleiro
