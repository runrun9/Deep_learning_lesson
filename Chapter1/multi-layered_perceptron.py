import numpy as np
def AND(x1,x2):
    x = np.array([x1,x2])   #入力
    w = np.array([0.5,0.5]) #重み
    b = -0.7                #バイアス
    if np.sum(x*w) + b > 0:
        return 1
    else:
        return 0

def NAND(x1,x2):
    x = np.array([x1,x2])       #入力
    w = np.array([-0.5,-0.5])   #重み
    b = 0.7                     #バイアス
    if np.sum(x*w) + b > 0:
        return 1
    else:
        return 0

def OR(x1,x2):
    x = np.array([x1,x2])   #入力
    w = np.array([0.5,0.5]) #重み
    b = -0.2               #バイアス
    if np.sum(x*w) + b > 0:
        return 1
    else:
        return 0

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(XOR(1,1))
print(XOR(0,1))
