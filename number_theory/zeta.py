from .B import B
from .E import E
from fractions import Fraction as Fr
from math import factorial

class zeta:
    def __init__(self, n=0, compute=True, z=0, s=''):
        self.z, self.s = self.calculate(n) if compute else (z, s)
    def __repr__(self):
        return str(self.z) + self.s
    def __str__(self):
        return repr(self)
    def calculate(self, n):
        if n > 0:
            if n % 2:
                print(f"Error: {n} is not an even number.")
                return Fr(E(n-1),2**(n+1)*factorial(n-1)), 'π' + "".join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(x)] for x in f"{n}"]) if n > 1 else "π"
            return (-1)**(n//2+1)*B(n)*2**(n-1)/factorial(n), 'π' + "".join(['⁰¹²³⁴⁵⁶⁷⁸⁹'[int(x)] for x in f"{n}"]) if n > 1 else "π"
        return (-1)**-n*B(1-n)/(1-n), ''

if __name__ == '__main__':
    print("This program calculates ζ(n) for any positive even integer and also for nonpositive integers.")
    n = int(eval(input("\n\tEnter n :\t")))
    print(f"ζ({n}) = {zeta(n)}")