def showMatrix(mat):
    "Print out matrix"
    for row in mat:
        print(row)

def zeroMatrix(m,n):
    "Create zero matrix"
    new_mat = []
    for row in range(m):
        zero_row = []
        for col in range(n):
            zero_row.append(0)
        new_mat.append(zero_row)
    return(new_mat)

def zeroV(m):
    z = [0]*m
    return(z)

def trapezoid_rule(h, a, b):
    i = a + h
    sum = 0.
    while(round(i,2) < 1.800000):
        i = round(i,2)
        sum = sum + p4(i)
        i= i+h
    return ((h/2)*(p4(a) + (2 * sum) + p4(b)))

def romberg2(h,a,b):
    s = zeroMatrix(4, 4)
    tmp = .8/h
    for i in range(4):
        s[i][0] = trapezoid_rule((tmp),a,b)
        tmp /= 2
    for i in range(1, 4):
        for j in range(i, 4):
            s[j][i] = s[j][i-1] + ((s[j][i-1] - s[j-1][i-1]) / ((2**(2*i))-1))
    showMatrix(s)
    
h = zeroMatrix(9, 2)
h[0][0] = 1.0
h[1][0] = 1.1
h[2][0] = 1.2
h[3][0] = 1.3
h[4][0] = 1.4 
h[5][0] = 1.5
h[6][0] = 1.6
h[7][0] = 1.7
h[8][0] = 1.8   
h[0][1] = 0.24197072
h[1][1] = 0.21785218
h[2][1] = 0.19418605
h[3][1] = 0.17136859
h[4][1] = 0.14972747
h[5][1] = 0.12951760
h[6][1] = 0.11092083
h[7][1] = 0.09407908
h[8][1] = 0.07895016

def p4(x):
    for i in range(9):
        if(h[i][0] == x):
            return h[i][1]
        
romberg2(1,1.,1.8)

