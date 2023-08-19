import numpy as np

n=1000
set=np.random.randint(1,100,size=n)

div=0
for i in range(n):
    if (set[i]%7 == 0):
        div+=1

print("prb of div =",div/n)
print("prb of not div =",(n-div)/n)

