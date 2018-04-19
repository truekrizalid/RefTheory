import numpy as np 
def f1(x,y,z):
    return x**2+y**2+z -8
def f2(x,y,z):
    return x+y**2+z**2 -14
def f3(x,y,z):
    return x**2+y+z**2 -12

def f1dx(x,y,z):
    return 1/0.001*(f1(x+0.001,y,z)-f1(x,y,z))
def f1dy(x,y,z):
    return 1/0.001*(f1(x,y+0.001,z)-f1(x,y,z))
def f1dz(x,y,z):
    return 1/0.001*(f1(x,y,z+0.001)-f1(x,y,z))
def f2dx(x,y,z):
    return 1/0.001*(f2(x+0.001,y,z)-f2(x,y,z))
def f2dy(x,y,z):
    return 1/0.001*(f2(x,y+0.001,z)-f2(x,y,z))
def f2dz(x,y,z):
    return 1/0.001*(f2(x,y,z+0.001)-f2(x,y,z))
def f3dx(x,y,z):
    return 1/0.001*(f3(x+0.001,y,z)-f3(x,y,z))
def f3dy(x,y,z):
    return 1/0.001*(f3(x,y+0.001,z)-f3(x,y,z))
def f3dz(x,y,z):
    return 1/0.001*(f3(x,y,z+0.001)-f3(x,y,z))
x = 3
y = 4
z= 10
while abs(f1(x,y,z))< 10**(-6) and abs(f2(x,y,z))<10**(-6) and abs(f3(x,y,z))<10**(-6) == False :
    y1= f1(x,y,z)
    y2 = f2(x,y,z)
    y3 = f3(x,y,z)
    y = np.mat([[y1],[y2],[y3]])
    U = np.mat([[x],[y],[z]])
    J = np.mat([[f1dx(x,y,z),f1dy(x,y,z),f1dz(x,y,z)],[f2dx(x,y,z),f2dy(x,y,z),f2dz(x,y,z)],[f3dx(x,y,z),f3dy(x,y,z),f3dz(x,y,z)]])
    invJ = np.linalg.inv(J)
    U = U - invJ*y
    x,y,z =U[0],U[1],U[2]
    
print x,y,z
