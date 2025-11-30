from jogo import Jogo
from tabuleiro import Tabuleiro
from gerador import GeradorSudoku

class SudokuGame(Jogo):
    def __init__(self):
        self._tabuleiro = None

    def selecionar_dificuldade(self):
        while True:
            print("\nSelecione a dificuldade:")
            print("1 - Fácil\n2 - Médio\n3 - Difícil\n4 - Sair")
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
            self._tabuleiro = Tabuleiro(incompleto)
            return

    def ler_entrada(self):
        while True:
            entrada = input("Digite posição e número (ex: A1 5): ").upper()
            try:
                pos, num = entrada.split()
                coluna = "ABCDEFGHI".index(pos[0])
                linha = int(pos[1])-1
                numero = int(num)
                if 0 <= linha < 9 and 1 <= numero <= 9:
                    return linha, coluna, numero
            except:
                pass
            print("Entrada inválida!")

    def jogar(self):
        self.selecionar_dificuldade()
        while True:
            self._tabuleiro.exibir()
            if self._tabuleiro.jogo_completo():
                print("\nPARABÉNS! Você ganhou!")
                break
            linha, coluna, numero = self.ler_entrada()
            ok, msg = self._tabuleiro.inserir_numero(linha, coluna, numero)
            print(msg)
