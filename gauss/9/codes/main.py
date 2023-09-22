from scipy.stats import norm
from scipy.stats import binom
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mping

p = 0.05
n = 5
k = 0
sig = np.sqrt(n*p*(1-p))
print("For k = 0")
print("Probability from Gaussian approximation: ",norm.cdf((k-n*p+0.5)/sig))
print("Probability from Binomial: ",(binom.cdf(k,n,p)))
k = 1
print("For k = 1")
print("Probability from Gaussian approximation: ",norm.cdf((k-n*p+0.5)/sig))
print("Probability from Binomial: ",(binom.cdf(k,n,p)))


sig = np.sqrt(n*p*(1-p))
k = np.linspace(0,n,n+1)
fig, ax = plt.subplots()
xpoints = k
ypoints = np.array(binom.pmf(k,n,p))
ax.stem(xpoints, ypoints,linefmt='r-', markerfmt='ro', basefmt='k--')
xpoints = np.linspace(-n,n,100*n)
ypoints = np.array(norm(n*p,sig).pdf(xpoints))
ax.plot(xpoints, ypoints,'b')
plt.legend(["Gaussian","Binomial"])
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid()
plt.savefig("bg.png")
