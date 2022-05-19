


#import re

count=0
def nq(mat ,r):
    global count
    if(r==8):
        count+=1
        printMat(mat)
        return
    

    for c in range(8):

        if(isSafe(mat,r,c)):
            mat[r][c]='Q'
            nq(mat,r+1)
            mat[r][c]='-'

def isSafe(mat,r,c):

    for i in range(c):
        if(mat[r][i]=='Q'):
            return 0

    for j in range(r):
        if(mat[j][c]=='Q'):
            return 0

    x,y=r,c

    while(x>=0 and y>=0):
        if(mat[x][y]=='Q'):
            return 0
        x=x-1
        y=y-1
    x,y=r,c

    while(x>=0 and y<8):
        if(mat[x][y]=='Q'):
            return 0
        x=x-1
        y=y+1

    return 1

def printMat(mat):

    for i in range(8):
        for j in range(8):

            print(mat[i][j],end=" ")
        print()   
    print('\n\n')

mat=[ ['-' for i in range(8)] for j in range(8)]

nq(mat,0)    

print(count)