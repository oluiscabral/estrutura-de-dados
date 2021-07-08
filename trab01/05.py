def interval_sum(n:int)->int:
    if n < 1:
        raise Exception("Intervalo inválido! `n` deve ser maior que 0.")
    if n == 1:
        return 1
    return n + interval_sum(n-1)

def main():
    n = int(input())
    result = interval_sum(n)
    print(f'a soma do intervalo [1,{n}] é: {result}')

main()
