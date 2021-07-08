from random import randint
from josephus_solver import JosephusSolver


def test(repetitions, max_random):
    solver = JosephusSolver()
    f = open('test.output', 'w')
    for i in range(repetitions):
        solver.n = randint(0, max_random)
        solver.m = randint(0, max_random)
        f.write(f"Usando {solver.n}, {solver.m}, resultado={solver.solve()}\n")


if __name__ == "__main__":
    repetitions = int(input())
    max_random = int(input())
    test(repetitions, max_random)
