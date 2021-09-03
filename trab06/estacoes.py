from typing import List

from grafo import Grafo
from vertice import Vertice


class Estacoes(Grafo):
    def __init__(self) -> None:
        super().__init__()

    def pega_estacao(self, num: int) -> List[Vertice]:
        compare_num = num-1
        estacao = []
        for v in self.vertices:
            if v.altura == compare_num:
                estacao.append(v)
        if len(estacao) == 0:
            raise Exception(f"Estação de trabalho de número {num} não existe.")
        estacao.sort()
        return estacao
