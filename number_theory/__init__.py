"""number_theory — exact number theory computations in Python.

Public API:
    B(n)          -- n-th Bernoulli number (exact Fraction)
    E(n)          -- n-th Euler zigzag number
    zeta(n)       -- exact closed-form zeta(n) for even n > 0 and n <= 0
    isPrime(n)    -- primality test
    NP(n)         -- next prime after n
    piprime(n, iters) -- Euler product approximation of pi
"""

from .B import B
from .E import E
from .zeta import zeta
from .prime import isPrime
from .nextPrime import NP
from .piprime import piprime
from .bernoulli import bernoulli
from .zigzag import zigzag

__all__ = ["B", "E", "zeta", "isPrime", "NP", "piprime", "bernoulli", "zigzag"]
__version__ = "2.0.1"

