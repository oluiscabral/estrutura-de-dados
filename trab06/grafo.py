from typing import List

from vertice import Vertice


class Grafo:
    def __init__(self):
        self.vertices: List[Vertice] = list()

    def adicionar_vertice(self, valor_pai: int, valor_filho: int) -> None:
        pai = self.__manuseia_vertice(Vertice(valor_pai))
        filho = self.__manuseia_vertice(Vertice(valor_filho))
        pai.adicionar_filho(filho)

    def __manuseia_vertice(self, vertice: Vertice):
        if vertice in self.vertices:
            i = self.vertices.index(vertice)
            return self.vertices[i]
        self.vertices.append(vertice)
        return vertice

    def pega_vizinhos(self, valor: int):
        compare_v = Vertice(valor)
        for v in self.vertices:
            if compare_v == v:
                return v.pega_vizinhos()
        raise Exception(f'Não foi possível encontrar o valor `{valor}` na lista')
