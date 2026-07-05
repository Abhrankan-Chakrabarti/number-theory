from fractions import Fraction as Fr

def bernoulli():
    A, m = [], 0
    while True:
        A.append(Fr(1, m+1))
        for j in range(m, 0, -1):
          A[j-1] = j*(A[j-1] - A[j])
        yield A[0] # (which is Bm)
        m += 1

if __name__ == '__main__':
    bn = [ix for ix in zip(range(61), bernoulli())]
    bn = [(i, b) for i,b in bn if b]
    width = max(len(str(b.numerator)) for i,b in bn)
    for i,b in bn:
        print('B(%2i) = %*i/%i' % (i, width, b.numerator, b.denominator))