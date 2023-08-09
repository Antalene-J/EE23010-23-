import numpy as np



I=(1/(np.sqrt(37) + 4 + np.sqrt(61)))*np.array([[np.sqrt(61) - 16 - 3*np.sqrt(37)],[-np.sqrt(61) + 24 - 5*np.sqrt(37)]]) #incnetre
n = np.array([[11], [1]]) #normal vector 
nT = n.T #transpose of normal
r = abs((nT @ I) - 50)/(np.linalg.norm(n)) #distance

print("distance is",r)

