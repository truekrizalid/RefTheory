import numpy as np 
def f1(x,y,z):
    return x**2+ y**2 + z -8
def f2(x,y,z):
    return x + y**2 + z**2 -14
def f3(x,y,z):
    return x**2 + y + z**2 -12

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

U = np.matrix([[3],[4],[10]])
x=U[0,0]
y=U[1,0]
z=U[2,0]
while (abs(f1(x,y,z))<10**(-4) and abs(f2(x,y,z))<10**(-4) and abs(f3(x,y,z))<10**(-4)) == False :
    J = np.matrix([[f1dx(x,y,z),f1dy(x,y,z),f1dz(x,y,z)],\
                   [f2dx(x,y,z),f2dy(x,y,z),f2dz(x,y,z)],\
                   [f3dx(x,y,z),f3dy(x,y,z),f3dz(x,y,z)]])
    y=np.matrix([[f1(x,y,z)],[f2(x,y,z)],[f3(x,y,z)]])
    print y
    U = U - J**(-1)*y
    print U
    x=U[0,0]
    y=U[1,0]
    z=U[2,0]

