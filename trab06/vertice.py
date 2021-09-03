from typing import Set, List


class Vertice:
    def __init__(self, valor: int) -> None:
        self.__valor: int = valor
        self.__pais: Set['Vertice'] = set()
        self.__filhos: List['Vertice'] = list()
        self.__altura = 0
        self.__tem_altura = True

    @property
    def valor(self):
        return self.__valor

    @property
    def pais(self):
        return self.__pais.copy()

    @property
    def filhos(self):
        return self.__filhos.copy()

    @property
    def altura(self):
        if not self.__tem_altura:
            self.__altura = 1 + max({v.altura for v in self.__pais})
            self.__tem_altura = True
        return self.__altura

    def adicionar_filho(self, filho: 'Vertice') -> None:
        filho.adicionar_pai(self)
        self.__filhos.append(filho)
        self.__filhos.sort()

    def adicionar_pai(self, pai: 'Vertice') -> None:
        self.__pais.add(pai)
        self.__tem_altura = False

    def pega_vizinhos(self) -> List['Vertice']:
        lst = []
        for v in self.__pais:
            lst.append(v)
        for v in self.__filhos:
            lst.append(v)
        lst.sort()
        return lst

    def __lt__(self, v):
        return self.valor < v.valor

    def __le__(self, v):
        return self.valor <= v.valor

    def __eq__(self, v):
        return self.valor == v.valor

    def __ne__(self, v):
        return not self.__eq__(v)

    def __gt__(self, v):
        return self.valor > v.valor

    def __ge__(self, v):
        return self.valor >= v.valor

    def __hash__(self):
        return hash(self.valor)

    def __repr__(self):
        return str(self.valor)
