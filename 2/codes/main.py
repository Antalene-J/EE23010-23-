import random

#efficient func
def not_adj(desk):
    return "M M" not in " ".join(desk)

def sim(n):
    desks = ["M", "E", "E","M", "E", "E"]
    nonadj_count = sum(not_adj(random.sample(desks, len(desks))) for j in range(n))
    prob = nonadj_count/n
    return prob

n = 100000
result = sim(n)
print("The probability that the married couple will have nonadjacent desks is:",result)
