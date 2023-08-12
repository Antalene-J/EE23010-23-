import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping

#points
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])

omat = np.array([[0,1],[-1,0]])

def dir_vec(A,B):
  return B-A

#slopes
m1=dir_vec(A,B)
m2=dir_vec(A,C)
#slopes of the sides of triangle is the normal form slope of altitudes
print("line cf1 is: ", m1,"x =",m1@C)
print("line be1 is: ", m2,"x =",m2@B)

#graph

def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#FOOT OF ALTITUDE
F=alt_foot(C,A,B)
E=alt_foot(B,C,A)

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_CF = line_gen(C,F)
x_BE = line_gen(B,E)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
E = E.reshape(-1,1)
F = F.reshape(-1,1)
tri_coords = np.block([[A,B,C,E,F]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','E','F']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig("alt.png")
