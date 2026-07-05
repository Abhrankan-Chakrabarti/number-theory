from Crypto.Util import number
def isPrime(n, r = False, i = 2, c = True):
	if c and number.isPrime(n):
		return True
	if c and not r:
		return r
	if n < 4:
		return n > 1
	isDivisible, k = lambda n, i, r: n if n % i else i if r else r, int(n ** 0.5)
	while i <= k:
		d = isDivisible(n, i, r)
		if d - n:
			return d
		i += i - 1 if i in (2, 3) else (i - 3) % 6
	return True
if __name__ == "__main__":
	print("This program checks whether a natural number, n, is prime or not.")
	n = int(eval(input("Enter n :\t")))
	print(f"{n} is {'' if isPrime(n) else 'not '}prime.")