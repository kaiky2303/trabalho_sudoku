from abc import ABC, abstractmethod

class Jogo(ABC):
    @abstractmethod
    def jogar(self):
        pass
