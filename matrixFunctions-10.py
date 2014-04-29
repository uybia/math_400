"""
matrixFunctions.py

2/5/13  bic
2/7/13  bic revised to fix zeroMatrix bug.  Many thanks to David Russell
2/8/13  bic removed old zeroMatrix

This is a skeleton for the matrix part of first Math 400 assignment

"""

#######  START Administrivia 
m400group = 10   # change this to your group number

m400names = ['Bianca Uy', 'Xuanyu Liu', 'Kevin Velasco', 'Danny Wu', 'Allen Yu'] # change this for your names

def printNames():
    print("matrixFunctions.py for group %s:"%(m400group)),
    for name in m400names:
        print("%s, "%(name)),
    print

printNames()

#######  END Administrivia

def showMatrix(mat):
    "Print out matrix"
    for row in mat:
        print(row)

## revised 2/7/13
def zeroMatrix(m,n):
    "Create zero matrix"
    new_mat = []
    for row in range(m):
        zero_row = []
        for col in range(n):
            zero_row.append(0)
        new_mat.append(zero_row)
    return(new_mat)


def rows(mat):
    "return number of rows"
    return(len(mat))

def cols(mat):
    "return number of cols"
    return(len(mat[0]))
 
def transpose(mat):
    "return transpose of mat"
    # finish this
    new_mat = zeroMatrix(cols(mat),rows(mat))
    for i in range(cols(mat)):
        for k in range(rows(mat)):
            new_mat[i][k] = mat[k][i]
    return(new_mat)

def getCol(mat, col):
    "return column col from matrix mat"
    # finish this
    col_mat = []
    for i in range (rows(mat)):
        col_mat.append(mat[i][col])
    return (col_mat)   

def getRow(mat, row):
    "return row row from matrix mat"
    # finish this
    return (mat[row]);


def scalarMultMatrix(a,mat):
    "multiply a scalar times a matrix"
    # finish this
    new_mat = []
    for row in range(rows(mat)):
        tmp = []
        for col in range(cols(mat)):
            tmp.append(a * mat[row][col])
        new_mat.append(tmp)     
    return(new_mat)


def addMatrices(A,B):
    "add two matrices"
    # finish this
    new_mat = []
    for row in range(rows(A)):
        tmp = []
        for col in range(cols(A)):
            tmp.append(A[row][col] + B[row][col])
        new_mat.append(tmp)
    return(new_mat)


def multiplyMat(mat1,mat2):
    "multiply two matrices"
    # finish this
    prod = []
    if cols(mat1) != rows(mat2):
        print("Cannot multiply the matrix")
        return
    for i in range(rows(mat1)):
        tmp = []
        for j in range(cols(mat2)):
            mat_sum = 0
            for k in range(rows(mat2)):
                mat_sum += mat1[i][k] * mat2[k][j]
            tmp.append(mat_sum)
        prod.append(tmp)
    return(prod)

A= [[4,-2,1,11],
    [-2,4,-2,-16],
    [1,-2,4,17]]

Ae= [[4,-2,1],
    [-2,4,-2],
    [1,-2,4]]

B=[[11,-16,17]]
C=[[2,3,5]]

print("running matrixFunction.py file")

