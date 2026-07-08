from .bernoulli import bernoulli

def B(n):
    return [i for i in zip(range(n+1),bernoulli())][n][1]