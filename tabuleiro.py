import copy

class Tabuleiro:
    def __init__(self, matriz):
        self._matriz = matriz
        self._original = copy.deepcopy(matriz)

    def exibir(self):
        print("\n   A B C   D E F   G H I")
        for i, linha in enumerate(self._matriz):
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
        if numero in self._matriz[linha]:
            return False
        for l in range(9):
            if self._matriz[l][coluna] == numero:
                return False
        il, ic = (linha // 3) * 3, (coluna // 3) * 3
        for i in range(3):
            for j in range(3):
                if self._matriz[il + i][ic + j] == numero:
                    return False
        return True

    def jogo_completo(self):
        for i in range(9):
            for j in range(9):
                n = self._matriz[i][j]
                if n == 0:
                    return False
                self._matriz[i][j] = 0
                valido = self.posicao_valida(i, j, n)
                self._matriz[i][j] = n
                if not valido:
                    return False
        return True

    def inserir_numero(self, linha, coluna, numero):
        if self._original[linha][coluna] != 0:
            return False, "Essa casa não pode ser alterada."
        if not self.posicao_valida(linha, coluna, numero):
            return False, "Movimento inválido!"
        self._matriz[linha][coluna] = numero
        return True, "Número inserido!"
