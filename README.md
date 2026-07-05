# number-theory

A small pure-Python library of exact and semi-exact number theory computations: Bernoulli numbers, Euler (zigzag) numbers, the Riemann zeta function at integers, and a primality/prime-generation toolkit that ties them together into an Euler-product approximation of π.

No dependencies beyond the standard library, except `prime.py` which uses `pycryptodome` for a fast Miller-Rabin primality check.

---

## Table of Contents

- [Modules](#modules)
- [Installation](#installation)
- [Usage](#usage)
- [How It Fits Together](#how-it-fits-together)
- [Examples](#examples)
- [Limitations](#limitations)
- [License](#license)

---

## Modules

| Module | Purpose |
|---|---|
| `bernoulli.py` | Generates Bernoulli numbers B(n) lazily and exactly as `Fraction`s |
| `B.py` | `B(n)` — returns the n-th Bernoulli number |
| `zigzag.py` | Computes zigzag (Euler up/down) numbers via dynamic programming |
| `E.py` | `E(n)` — returns the n-th Euler zigzag number, `zigzag(n, n)` |
| `zeta.py` | `zeta(n)` — exact closed form of ζ(n) for even positive and all non-positive integers |
| `prime.py` | `isPrime(n)` — hybrid primality test (Miller-Rabin via pycryptodome, with optional trial-division fallback) |
| `nextPrime.py` | `NP(n)` — next prime after `n`, using a 6k±1 wheel |
| `piprime.py` | `piprime(n, iters)` — approximates π via the Euler product formula for ζ(n) |

---

## Installation

```bash
git clone https://github.com/Abhrankan-Chakrabarti/number-theory.git
cd number-theory
pip install -e .
```

This installs the `number_theory` package in editable mode along with its one dependency, `pycryptodome`.

---

## Usage

Import the public API directly from the package:

```python
from number_theory import B, E, zeta, isPrime, NP, piprime

B(10)              # Fraction(5, 66)
E(4)               # 5
zeta(4)            # 1/90π⁴  (exact, as a formatted string)
isPrime(97)        # True
NP(97)             # 101
piprime(2, 1000)   # ≈ 3.14157...
```

Each module can also be run standalone via `python -m`:

```bash
python -m number_theory.bernoulli   # prints B(0) through B(60)
python -m number_theory.prime       # prompts for n, checks primality
python -m number_theory.nextPrime   # prompts for a prime, finds the next one
python -m number_theory.zeta        # prompts for n, prints ζ(n)
python -m number_theory.piprime     # prompts for n and iteration count, approximates π
```

---

## How It Fits Together

```
number_theory/
├── __init__.py    (exposes the public API)
├── piprime.py
│   ├── nextPrime.py → prime.py → Crypto.Util.number (Miller-Rabin)
│   └── zeta.py
│       ├── B.py → bernoulli.py   (exact Bernoulli numbers via Fraction)
│       └── E.py → zigzag.py      (Euler zigzag numbers via DP table)
```

**Bernoulli numbers** (`bernoulli.py`) are generated with the Akiyama–Tanigawa-style triangle algorithm, yielding exact `Fraction` values lazily — no floating-point error, no recomputation from scratch for each index.

**Zigzag numbers** (`zigzag.py`) count alternating permutations and appear in the odd-argument case of ζ via their connection to tangent/secant numbers.

**`zeta(n)`** returns an exact closed form:
- **Positive even n:** ζ(n) = (−1)^(n/2+1) · B(n) · 2^(n−1) / n! · πⁿ
- **Non-positive n:** ζ(n) = (−1)^(−n) · B(1−n) / (1−n) — the "trivial" values, all rational
- **Positive odd n:** no known closed form exists (this is genuinely open in general — ζ(3) is Apéry's constant); `zeta.py` prints a warning and returns an Euler-number-based expression rather than a proven identity

**`piprime.py`** uses the Euler product ζ(n) = ∏ₚ (1 − p⁻ⁿ)⁻¹ over the first `iters` primes, rearranged to solve for π:

```
π = ( ∏ₚ(1 − p⁻ⁿ) · ζ(n) )^(−1/n)
```

Since ζ(n) is known exactly for even n, this converges to π as more primes are included — a nice way to derive π purely from the distribution of primes.

**`prime.py`** and **`nextPrime.py`** provide the prime stream `piprime.py` walks over: `isPrime` uses `pycryptodome`'s Miller-Rabin test by default (fast, probabilistic but effectively certain for practical sizes), with an optional 6k±1 trial-division mode; `NP` finds the next prime by stepping along the same 6k±1 wheel.

---

## Examples

```python
>>> from zeta import zeta
>>> zeta(2)
1/6π²
>>> zeta(4)
1/90π⁴
>>> zeta(-1)
-1/12
>>> zeta(-3)
1/120
```

```python
>>> from piprime import piprime
>>> piprime(2, 1000)
3.1415727030005223
>>> piprime(2, 100000)
3.14159260...
```

More iterations (more primes in the product) converge more closely to π, though slowly — this is a demonstration of the identity, not an efficient way to compute π.

---

## Limitations

- **Odd zeta values** (ζ(3), ζ(5), ...) have no known closed form in terms of π and rationals; `zeta.py`'s odd-n branch returns an Euler-number expression as a placeholder, not a mathematically proven identity. Treat this case as exploratory only.
- `piprime.py` converges slowly — it's a demonstration of the Euler product identity, not a practical π-computation algorithm.
- `prime.py`'s trial-division fallback (`r=True, c=False`) is only efficient for small `n`; the default Miller-Rabin path via `pycryptodome` should be used for anything large.

---

## License

MIT — see [LICENSE](LICENSE) for details.

