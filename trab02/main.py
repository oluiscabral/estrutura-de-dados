from josephus_solver import JosephusSolver


def main():
    solver = JosephusSolver()
    for i in range(int(input())):
        solver.n = int(input())
        solver.m = int(input())
        print(f"Usando n={solver.n}, m={solver.m}, resultado={solver.solve()}")


if __name__ == '__main__':
    main()
