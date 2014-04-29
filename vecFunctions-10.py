"""
vecFunctions.py

This file contains four versions of copyVec() and a test function.
It also contains stubs for three other vector functions

Math 400 2/5/13


"""
#######  START Administrivia 
m400group = 10   # change this to your group number

m400names = ['Bianca Uy', 'Xuanyu Liu', 'Kevin Velasco', 'Danny Wu', 'Allen Yu'] # change this for your names

def printNames():
    print("vecFunctions.py for group %s:"%(m400group)),
    for name in m400names:
        print("%s, "%(name)),
    print

printNames()

#######  END Administrivia
        
def copyVec_1(L):
    "return a copy of L"
    C=[]
    for k in L:
        C.append(k)
    return(C)

def copyVec_2(L):
    "return a copy of L"
    C=[k for k in L]
    return(C)

def copyVec_3(L):
    "return a copy of L"
    C=[]
    for j in range(len(L)):
        C.append(L[j])
    return(C)

def copyVec_4(L):
    "return a copy of L"
    C=[L[j] for j in range(len(L))]
    return(C)


def scalarMult(s,V):
    "return vector sV"
    C = []
    for i in range(len(V)):
        C.append(V[i]*s)
    return(C)    


def addVectors(S,T):
    "return S+T"
    if len(S) != len(T):
        return("Incorect size")
    else:
        C=[]
        for i in range(len(S)):
            C.append(S[i]+T[i])
        return(C)


def dot(S,T):
    "return dot product of two vectors"
    if len(S) != len(T):
        return("Incorect size")
    else:
        tmp=[]
        product=0
        for i in range(len(S)):
            tmp.append(S[i]*T[i])
        for i in range(len(tmp)):
            product += tmp[i]
        return(product)

def testVecFunctions():
    "test the copy functions"
    V=range(10)
    U=[6,7,1,3,-9]
    print("V=%s"%V)
    print("U=%s"%U)
    V_1=copyVec_1(V)
    U_1=copyVec_1(U)
    print("copyVec_1(V)==V is %s"%(V_1==V))
    print("copyVec_1(U)==U is %s"%(U_1==U))
    V_2=copyVec_2(V)
    U_2=copyVec_2(U)
    print("copyVec_2(V)==V is %s"%(V_2==V))
    print("copyVec_2(U)==U is %s"%(U_2==U))
    V_3=copyVec_3(V)
    U_3=copyVec_3(U)
    print("copyVec_3(V)==V is %s"%(V_3==V))
    print("copyVec_3(U)==U is %s"%(U_3==U))
    V_4=copyVec_4(V)
    U_4=copyVec_4(U)
    print("copyVec_4(V)==V is %s"%(V_4==V))
    print("copyVec_4(U)==U is %s"%(U_4==U))

#testVecFunctions()
    
    
