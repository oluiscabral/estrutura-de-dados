from estacoes import Estacoes


def main():
    estacoes = Estacoes()
    qtd_vertices = int(input())
    while True:
        valor_pai, valor_filho = [int(w) for w in input().split(',')]
        if valor_pai == -1 and valor_filho == -1:
            break
        estacoes.adicionar_vertice(valor_pai, valor_filho)
    num_maior_estacao = pega_num_maior_estacao(estacoes)
    print(num_maior_estacao)


def pega_num_maior_estacao(estacoes):
    num = 1
    while True:
        try:
            estacoes.pega_estacao(num)
        except:
            break
        num += 1
    return num - 1


if __name__ == '__main__':
    main()
