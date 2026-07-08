from .prime import isPrime
def NP(n):
	if n in (2, 3):
		return 2 * n - 1
	m = n + (n - 3) % 6
	while not isPrime(m):
		m += (m - 3) % 6
	return m
if __name__ == "__main__":
	n = int(input("Enter a prime no. :\t"))
	print(f"Next Prime of {n} is {NP(n)}." if isPrime(n) else "Invalid Input.")