Pt=100
F=100
U1=50
z1=0.3
z2=0.3
z3=0.4
V1=0
V2=150
V3=float(input("Donner V3 "))
V4=float(input("Donner V4 "))
V5=float(input("Donner V5 "))
T1=float(input("Donner T1 "))
T2=float(input("Donner T2 "))
T3=float(input("Donner T3 "))
T4=float(input("Donner T4 "))
T5=float(input("Donner T5 "))
## Matrice d'élément C3:
## calcule des Aj:
A12=int(V2)-int(U1)
print ("A12= ", A12)
A13=int(V3)-int(U1)
print ("A13= ", A13)
A14=int(V4)+int(F)-int(U1)
print ("A14= ", A14)
A15=int(V5)+int(F)-int(U1)
print ("A15= ", A15)
##calcule de Dj:
D13=-F*z1
print ("D13=", D13)
D11=0
D12=0
D14=0
D15=0
##calcule de Bj:
    ##calcule de Kij:
A1=6.8196
B1=785
C1=247
P11 = float((10**(A1-(B1/(C1+(T1-32)*(5/9)))))/51.715)
print("P11=", P11)
P12 = float((10 **(A1-(B1/(C1+(T2-32)*(5/9)))))/51.715)
print("P31=", P12)
P13 = float((10**(A1-(B1/(C1+(T3-32)*(5/9)))))/51.715)
print("P13=", P13)
P14 = float((10 **(A1-(B1 /(C1+(T4-32)*(5/9)))))/51.715)
print("P14=", P14)
P15 = float((10 **(A1-(B1/(C1+(T5-32)*(5/9)))))/51.715)
print("P15=", P15)
K11 = P11 / Pt
print("K11=", K11)
K12 = P12 / Pt
print("K12=", K12)
K13 = P13 / Pt
print("K13=", K13)
K14 = P14 / Pt
print("K14=", K14)
K15 = P15 / Pt
print("K15=",K15)
##calcule de Bj:
B11=-V2
print("B11=", B11)
B12=-(V3-U1+V2*K12)
print("B12=", B12)
B13=-(V4-U1+F+V3*K13)
print("B13=", B13)
B14=-(V5-U1+F+V4*K14)
print("B14=", B14)
B15=-(F-U1+V5*K15)
print("B15=", B15)
##calcule de Cj:
C11=V2*K12
print("C11=", C11)
C12=V3*K13
print("C12=", C12)
C13=V4*K14
print("C13=", C13)
C14=V5*K15
print("C14=", C14)
##Résolution de la matrice:
import numpy as np
a1= np.array([[B11,C11,0,0,0],
             [A12,B12,C12,0,0],
             [0,A13,B13,C13,0],
             [0,0,A14,B14,C14],
             [0,0,0,A15,B15]],dtype=float)
print("a1=", a1)
b1= np.array([0,0,D13,0,0],dtype=float)
print("b1=",b1)
x1=np.linalg.solve(a1,b1)
print("x1=", x1)
## Matrice d'élément n-C4:
##calcule de Aj:
A22=int(V2)-int(U1)
print ("A22= ", A22)
A23=int(V3)-int(U1)
print ("A23= ", A23)
A24=int(V4)+int(F)-int(U1)
print ("A24= ", A24)
A25=int(V5)+int(F)-int(U1)
print ("A25= ", A25)
##calcule de Dj:
D23=-F*z2
print ("D23=", D23)
D21=0
D22=0
D24=0
D25=0
##calcule de Bj:
    ##calcule de Kij:
A2=6.78866
B2=899.617
C2=241.942
P21 = float((10**(A2-(B2/(C2+(T1-32)*(5/9)))))/51.715)
print("P21=", P21)
P22 = float((10 **(A2-(B2/(C2+(T2-32)*(5/9)))))/51.715)
print("P22=", P22)
P23 = float((10**(A2-(B2/(C2+(T3-32)*(5/9)))))/51.715)
print("P23=", P23)
P24 = float((10 **(A2-(B2/(C2+(T4-32)*(5/9)))))/51.715)
print("P24=", P24)
P25 = float((10 **(A2-(B2/(C2+(T5-32)*(5/9)))))/51.715)
print("P25=", P25)
K21 = P21/Pt
print("K21=", K21)
K22 = P22/Pt
print("K22=", K22)
K23 = P23/Pt
print("K23=", K23)
K24 = P24/Pt
print("K24=", K24)
K25 = P25/Pt
print("K25=",K25)
##calcule Bj:
B21=-V2
print("B21=", B21)
B22=-(V3-U1+V2*K22)
print("B22=", B22)
B23=-(V4+F-U1+V3*K23)
print("B23=", B23)
B24=-(V5+F-U1+V4*K24)
print("B24=", B24)
B25=-(F-U1+V5*K25)
print("B25=", B25)
##calcule de Cj:
C21=V2*K22
print("C21=", C21)
C22=V3*K23
print("C22=", C22)
C23=V4*K24
print("C23=", C23)
C24=V5*K25
print("C24=", C24)
##Résolurion de la matrice:
import numpy as np
a2= np.array([[B21,C21,0,0,0],
             [A22,B22,C22,0,0],
             [0,A23,B23,C23,0],
             [0,0,A24,B24,C24],
             [0,0,0,A25,B25]],dtype=float)
print("a2=", a2)
b2= np.array([0,0,D23,0,0],dtype=float)
print("b2=",b2)
x2=np.linalg.solve(a2,b2)
print("x2=", x2)
## Matrice d'élément n-C5:
    ##calcule de Bj:
A32=int(V2)-int(U1)
print ("A32= ", A32)
A33=int(V3)-int(U1)
print ("A33= ", A33)
A34=int(V4)+int(F)-int(U1)
print ("A34= ", A34)
A35=int(V5)+int(F)-int(U1)
print ("A35= ", A35)
##calcule de Cj:
D33=-F*z3
print ("D33=", D33)
D31=0
D32=0
D34=0
D35=0
##calcule de Bj:
    ##calcule de Kij:
A3=6.84471
B3=1060.733
C3=231.541
P31 = float((10**(A3-(B3/(C3+(T1-32)*(5/9)))))/51.715)
print("P31=", P31)
P32 = float((10 **(A3-(B3/(C3+(T2-32)*(5/9)))))/51.715)
print("P32=", P32)
P33 = float((10**(A3-(B3/(C3+(T3-32)*(5/9)))))/51.715)
print("P33=", P33)
P34 = float((10 **(A3-(B3/(C3+(T4-32)*(5/9)))))/51.715)
print("P34=", P34)
P35 = float((10 **(A3-(B3/(C3+(T5-32)*(5/9)))))/51.715)
print("P35=", P35)
K31 = P31/Pt
print("K31=", K31)
K32 = P32/Pt
print("K32=", K32)
K33 = P33/Pt
print("K33=", K33)
K34 = P34/Pt
print("K34=", K34)
K35 = P35/Pt
print("K35=",K35)
##calcule de Bj:
B31=-V2
print("B31=", B31)
B32=-(V3-U1+V2*K32)
print("B32=", B32)
B33=-(V4+F-U1+V3*K33)
print("B33=", B33)
B34=-(V5+F-U1+V4*K34)
print("B34=", B34)
B35=-(F-U1+V5*K35)
print("B35=", B35)
##calcule de Cj:
C31=V2*K32
print("C31=", C31)
C32=V3*K33
print("C32=", C32)
C33=V4*K34
print("C33=", C33)
C34=V5*K35
print("C34=", C34)
##Calcule de a matrice:
import numpy as np
a3= np.array([[B31,C31,0,0,0],
             [A32,B32,C32,0,0],
             [0,A33,B33,C33,0],
             [0,0,A34,B34,C34],
             [0,0,0,A35,B35]],dtype=float)
print("a3=", a3)
b3= np.array([0,0,D33,0,0],dtype=float)
print("b3=",b3)
x3=np.linalg.solve(a3,b3)
print("x3=", x3)
##récupération des solutions se forme d'une matrice:
R= np.array([x1, x2, x3])
print("R =", R)
##calcule de la somme des x dans chaque étage:
E1=R[0,0]+R[1,0]+R[2,0]
print ("E1= ", E1)
E2=R[0,1]+R[1,1]+R[2,1]
print ("E2= ", E2)
E3=R[0,2]+R[1,2]+R[2,2]
print ("E3=" , E3)
E4=R[0,3]+R[1,3]+R[2,3]
print ("E4=" , E4)
E5=R[0,4]+R[1,4]+R[2,4]
print ("E5=" , E5)
## normalisation des x:
N1 = np.array([x1[0]/E1,x1[1]/E2,x1[2]/E3,x1[3]/E4,x1[4]/E5],float)
print("N1 = ",N1)
N2 = np.array([x2[0]/E1, x2[1]/E2,x2[2]/E3, x2[3]/E4, x2[4]/E5], float)
print("N2 = ", N2)
N3 = np.array([x3[0]/E1, x3[1]/E2, x3[2]/E3, x3[3]/E4, x3[4]/E5] , float)
print("N3 = ", N3)
##Récuperer les valeurs se forme d'une matrice:
L= np.array([N1, N2, N3])
print("L = " , L)
##calculer la somme des nouvelles x:
S1 = L[0,0] +L[1,0] +L[2,0]
print("S 1 = ",S1)
S2 = L[0,1] +L[1,1] +L[2,1]
print("S 2 = ",S2)
S3 = L[0,2] +L[1,2] +L[2,2]
print("S 3 = ",S3)
S4 = L[0,3] +L[1,3] +L[2,3]
print("S 4 = ",S4)
S5 = L[0,4] +L[1,4] +L[2,4]
print("S 5 = ",S5)
##Vérification de la somme Kij*Xij=1/
Y1 = K11*L[0,0] + K21*L[1,0] + K31*L[2,0] - 1
print("Y1 = " , Y1)
Y2 = K12*L[0,1] + K22*L[1,1] + K32*L[2,1] - 1
print("Y2 = " , Y2)
Y3 = K13*L[0,2] + K23*L[1,2] + K33*L[2,2] - 1
print("Y3 = " , Y3)
Y4 = K14*L[0,3] + K24*L[1,3] + K34*L[2,3] - 1
print("Y4 = " , Y4)
Y5 = K15*L[0,4] + K25*L[1,4] + K35*L[2,4] - 1
print("Y5 = " , Y5)
#chercher les températures qui vont vérifier la somme Kij*Xij=1
## pour T1:
from scipy.optimize import fsolve
def func1(T1):
    m1 = (L[0,0]((10*(A1-B1/(C1+(T1-32)*5/9)))/5171.5) +
          L[1,0]((10*(A2-B2/(C2+(T1-32)*5/9)))/5171.5) +
          L[2,0]((10*(A3-B3/(C3+(T1-32)*5/9)))/5171.5) -1)
    return m1
root = fsolve(func1, [1])
print("T1 = ",root)
## pour T2:
from scipy.optimize import fsolve
def func1(T2):
    m2 = (L[0,1]((10*(A1-B1/(C1+(T2-32)*5/9)))/5171.5) +
          L[1,1]((10*(A2-B2/(C2+(T2-32)*5/9)))/5171.5) +
          L[2,1]((10*(A3-B3/(C3+(T2-32)*5/9)))/5171.5) -1)
    return m2
root = fsolve(func1, [1])
print("T2 = ",root)
##pour T3:
from scipy.optimize import fsolve
def func1(T3):
    m3 = (L[0,2]((10*(A1-B1/(C1+(T3-32)*5/9)))/5171.5) +
          L[1,2]((10*(A2-B2/(C2+(T3-32)*5/9)))/5171.5) +
          L[2,2]((10*(A3-B3/(C3+(T3-32)*5/9)))/5171.5) -1)
    return m3
root = fsolve(func1, [1])
print("T3 = ",root)
## pour T4:
from scipy.optimize import fsolve
def func1(T4):
    m4 = (L[0,3]((10*(A1-B1/(C1+(T4-32)*5/9)))/5171.5) +
          L[1,3]((10*(A2-B2/(C2+(T4-32)*5/9)))/5171.5) +
          L[2,3]((10*(A3-B3/(C3+(T4-32)*5/9)))/5171.5) -1)
    return m4
root = fsolve(func1, [1])
print("T4 = ",root)
##pour T5:
from scipy.optimize import fsolve
def func1(T5):
    m5 = (L[0,4]((10*(A1-B1/(C1+(T5-32)*5/9)))/5171.5) +
          L[1,4]((10*(A2-B2/(C2+(T5-32)*5/9)))/5171.5) +
          L[2,4]((10*(A3-B3/(C3+(T5-32)*5/9)))/5171.5) -1)
    return m5
root = fsolve(func1, [1])
print("T5 = ",root)
