import random

def not_adj(desk):
    return "M M" not in " ".join(desk)

def sim(n):
    desks = ["M", "M", "E", "E", "E", "E"]
    nonadj_counts = map(lambda _: not_adj(random.sample(desks, len(desks))), range(n))
    prob = sum(nonadj_counts) / n
    return prob

n = 100000
result = sim(n)
print("The probability that the married couple will have nonadjacent desks is:",result)
