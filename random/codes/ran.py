import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
#graph codes at line 250
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]])

A = np.array([-3, 0])
B = np.array([0, -4])
C = np.array([-4, -3])

#1.1.1
m1 = B-A
m2 = C-B
m3 = A-C
print("m=",m1,m2,m3)

#1.1.2
norm_m1 = np.linalg.norm(m1)
norm_m2 = np.linalg.norm(m2)
norm_m3 = np.linalg.norm(m3)
print(norm_m1,norm_m2,norm_m3)

#1.1.3
mat1 = np.array([[1,1,1],[A[0],B[0],C[0]],[A[1],B[1],C[1]]])
r1 = np.linalg.matrix_rank(mat1)
print("rank=",r1)

#1.1.4
print("parametric of AB form is x:",A,"+ k",m1)
print("parametric of BC form is x:",B,"+ k",m2)
print("parametric of CA form is x:",C,"+ k",m3)

#1.1.5
n1 = omat@m1
n2 = omat@m2
n3 = omat@m3
print("n=",n1,n2,n3)

#1.1.6
x = np.cross(m1,m2)
area = 0.5*(np.linalg.norm(x))
print("area=",area)

#1.1.7
dotA = (B-A)@(C-A).T
NormA = (np.linalg.norm(B-A))*(np.linalg.norm(C-A))
angle_A = np.degrees(np.arccos((dotA)/NormA))
dotB = (A-B)@(C-B).T
NormB = (np.linalg.norm(A-B))*(np.linalg.norm(C-B))
angle_B = np.degrees(np.arccos((dotB)/NormB))
dotC = (A-C)@(B-C).T
NormC = (np.linalg.norm(A-C))*(np.linalg.norm(B-C))
angle_C = np.degrees(np.arccos((dotC)/NormC))
print("angles=",angle_A,angle_B,angle_C)


#1.2.1
D = (B + C)/2
E = (A + C)/2
F = (A + B)/2
print("D,E,F =",D,E,F)

#1.2.2
m4 = D-A
m5 = E-B
m6 = F-C
n4 = omat@m4
n5 = omat@m5
n6 = omat@m6
print("m =",m4,m5,m6)
print("n =",n4,n5,n6)

#1.2.3
G=(A+B+C)/3
print("G =",G)

#1.2.4
norm_AG = np.linalg.norm(A-G)
norm_DG = np.linalg.norm(D-G)
norm_BG = np.linalg.norm(B-G)
norm_EG = np.linalg.norm(E-G)
norm_CG = np.linalg.norm(C-G)
norm_FG = np.linalg.norm(F-G)
print("AG,DG,BG,EG,CG,FG =",norm_AG,norm_DG,norm_BG,norm_EG,norm_CG,norm_FG)

#1.2.5
mat2 = np.array([[1,1,1],[A[0],D[0],G[0]],[A[1],D[1],G[1]]])
r2 = np.linalg.matrix_rank(mat2)
mat3 = np.array([[1,1,1],[B[0],E[0],G[0]],[B[1],E[1],G[1]]])
r3 = np.linalg.matrix_rank(mat3)
mat4 = np.array([[1,1,1],[C[0],F[0],G[0]],[C[1],F[1],G[1]]])
r4 = np.linalg.matrix_rank(mat4)
print("rank =",r2,r3,r4)

#1.2.7
AF = A-F
ED = E-D
print("AF,ED =",AF, ED)


#1.3.2
n7 = C-B
n8 = A-C
n9 = B-A
print("Altidudes normal =",n7,n8,n9)

#1.3.4
angles = np.array([angle_A,angle_B,angle_C])
angles = angles*np.pi/180
tan = np.tan(angles)
hx=(A[0]*tan[0]+B[0]*tan[1]+C[0]*tan[2])/(tan[0]+tan[1]+tan[2])
hy=(A[1]*tan[0]+B[1]*tan[1]+C[1]*tan[2])/(tan[0]+tan[1]+tan[2])
H = np.array([hx,hy])
print("H=",H)


#1.4.2
def ccircle_O(A,B,C):
  p = np.zeros(2)
  n1 = B-A
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = C-B
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.block([[n1],[n2]])
  O=-np.linalg.solve(N,p)
  r = np.linalg.norm(A -O)
  return O
  
def ccircle_R(A,B,C):
  p = np.zeros(2)
  n1 = B-A
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = C-B
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.block([[n1],[n2]])
  O=np.linalg.solve(N,p)
  r = np.linalg.norm(A +O)
  return r
O = ccircle_O(A,B,C)
print("circumcentre =",O)

#1.4.4
R = ccircle_R(A,B,C)
print("radius =",R)


#1.5.1
def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@dir_vec(A,B)
  
t = norm_vec(B,C) 
n10 = t/np.linalg.norm(t) #unit normal vector
t = norm_vec(C,A)
n11 = t/np.linalg.norm(t)
t = norm_vec(A,B)
n12 = t/np.linalg.norm(t)

m_a=norm_vec(n11,n12)
m_b=norm_vec(n10,n12)
m_c=norm_vec(n10,n11)
print("slopes of angular bis",m_a,m_b,m_c)

#1.5.2
def icircle(A,B,C):
  k1 = 1
  k2 = 1
  p = np.zeros(2)
  t = norm_vec(B,C)
  n1 = t/np.linalg.norm(t)
  t = norm_vec(C,A)
  n2 = t/np.linalg.norm(t)
  t = norm_vec(A,B)
  n3 = t/np.linalg.norm(t)
  p[0] = n1@B- k1*n2@C
  p[1] = n2@C- k2*n3@A
  #Intersection
  N=np.block([[n1 - k1 * n2],[ n2 - k2 * n3]])
  I=np.linalg.solve(N,p)
  r = n1@(I-B)
  return I,r
  
[I,i_r] = icircle(A,B,C)
print("incentre =",I)

#1.5.3
BA = A - B
CA = A - C
BC = B - C
IA = A - I
IB = B - I
IC = C - I

def angle_btw_vectors(v1, v2):
    dot_product = v1 @ v2
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    angle = np.arccos(dot_product / norm)
    angle_in_deg = np.degrees(angle)
    return angle_in_deg

angle_BAI = angle_btw_vectors(BA, IA)
angle_CAI = angle_btw_vectors(CA, IA)
angle_ABI = angle_btw_vectors(BA, IB)
angle_CBI = angle_btw_vectors(BC, IB)
angle_BCI = angle_btw_vectors(BC, IC)
angle_ACI = angle_btw_vectors(CA, IC)
print("Angle BAI:", angle_BAI)
print("Angle CAI:", angle_CAI)
print("Angle ABI:", angle_ABI)
print("Angle CBI:", angle_CBI)
print("Angle BCI:", angle_BCI)
print("Angle ACI:", angle_ACI)

#1.5.6
t1 = norm_vec(B,C)
t2 = norm_vec(C,A)
t3 = norm_vec(A,B)

r1 = abs((t3@I) - (t3@A))/(np.linalg.norm(t3))   #r1 is distance between I and AB
r2 = abs((t2@I) - (t2@C))/(np.linalg.norm(t2))   #r2 is distance between I and AC
r3 = abs((t1@I) - (t1@C))/(np.linalg.norm(t1))   #r2 is distance between I and BC

print("Distance between I and AB is",r1)
print("Distance between I and AC is",r2)
print("Distance between I and BC is",r3)

#1.5.7
k2 = ((I-A)@(A-B))/((A-B)@(A-B))
k1 = ((I-A)@(A-C))/((A-C)@(A-C))
k3 = ((I-B)@(B-C))/((B-C)@(B-C))
E3 = A+(k1*(A-C))
F3 = A+(k2*(A-B))
D3 = B+(k3*(B-C))
print("E3 = ",E3)
print("F3 = ",F3)
print("D3 = ",D3)










#graph withn triangle only
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

A1 = A.reshape(-1,1)
B1 = B.reshape(-1,1)
C1 = C.reshape(-1,1)

tri_coords = np.block([[A1,B1,C1]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
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
plt.savefig("tri.png")
plt.clf()

#graph with centroids
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D)
x_BE = line_gen(B,E)
x_CF = line_gen(C,F)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')

D1 = D.reshape(-1,1)
E1 = E.reshape(-1,1)
F1 = F.reshape(-1,1)
G1 = G.reshape(-1,1)

tri_coords = np.block([[A1,B1,C1,D1,E1,F1,G1]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F','G']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid() # minor
plt.savefig("centr.png")
plt.clf()

#graph with altitudes
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
  
D1= alt_foot(A,B,C)
E1= alt_foot(B,C,A)
F1= alt_foot(C,A,B)

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD = line_gen(A,D1)
x_BE = line_gen(B,E1)
x_CF = line_gen(C,F1)

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_CF[0,:],x_CF[1,:],label='$CF$')

D1 = D1.reshape(-1,1)
E1 = E1.reshape(-1,1)
F1 = F1.reshape(-1,1)
H1 = H.reshape(-1,1)

tri_coords = np.block([[A1,B1,C1,D1,E1,F1,H1]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F','H']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid() # minor
plt.savefig("alt.png")
plt.clf()


#graph with circumcentre
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_OD = line_gen(O,D)
x_OE = line_gen(O,E)
x_OF = line_gen(O,F)
x_ccirc= circ_gen(O,R)

plt.plot(x_ccirc[0,:],x_ccirc[1,:],label='$circumcircle$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$')
plt.plot(x_OE[0,:],x_OE[1,:],label='$OE$')
plt.plot(x_OF[0,:],x_OF[1,:],label='$OF$')

D1 = D.reshape(-1,1)
E1 = E.reshape(-1,1)
F1 = F.reshape(-1,1)
O1 = O.reshape(-1,1)

tri_coords = np.block([[A1,B1,C1,D1,E1,F1,O1]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D','E','F','O']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid() # minor
plt.savefig("cir.png")
plt.clf()

#graph with incircle
incircle=circ_gen(I,i_r)
plt.plot(incircle[0,:],incircle[1,:],label='$incircle$')
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AI = line_gen(A,I)
x_BI = line_gen(B,I)
x_CI = line_gen(C,I)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AI[0,:],x_AI[1,:],label='$AI$')
plt.plot(x_BI[0,:],x_BI[1,:],label='$BI$')
plt.plot(x_CI[0,:],x_CI[1,:],label='$CI$')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
D3 = D3.reshape(-1,1)
E3 = E3.reshape(-1,1)
F3 = F3.reshape(-1,1)
I = I.reshape(-1,1)
tri_coords = np.block([[A,B,C,D3,E3,F3,I]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','$D_3$','$E_3$','$F_3$','I']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,0), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig("incir.png")
