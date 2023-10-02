import random

def one_sim():
	bulbs = [0,0,1,1,1]
	random.shuffle(bulbs)

	if (sum(bulbs[0:3]) == 1 and sum(bulbs[0:2]) != 0) or sum(bulbs[0:3]) == 3:
		return 1
	else: 
		return 0

def sim(num):
	count_3 = sum(1 for _ in range(num) if one_sim() == 1)
	return count_3 / num		
	
n = 1000 
x = sim(n)
print("simulated probability =",x)



