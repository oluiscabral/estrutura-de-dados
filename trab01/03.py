def v_repr(n:int)->str:
    if n > 0:
        return str(n) + v_repr(n-1) + str(n)
    elif n < 0:
        return str(n) + v_repr(n+1) + str(n)
    return '00'

def main():
    n = int(input())
    print(v_repr(n))

main()
