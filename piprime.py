from nextPrime import NP
from zeta import zeta
def piprime(n, iters):
    t, p = 1, 2
    for i in range(iters):
        t *= 1 - p ** -n
        p = NP(p)
    return 1 / (t * zeta(n).z) ** (1 / n)
if __name__ == '__main__':
    n = int(input('Enter n :\t'))
    iters = int(input('Enter the number of iterations :\t'))
    print(f'π = {piprime(n, iters)}...')