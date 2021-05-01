import numpy as np

def getLU(arr: np.array, n: int):
    l = np.zeros((n,n))
    u = np.array(arr,copy=True)
    pivot_row=0
    pivot_col=0
    for j in range(n):
        val = u[pivot_row][pivot_col]
        for i in range(n):
            if i>pivot_row: 
                l[i][j]=u[i][j]/val
                if u[i][j]!= 0:
                    x= u[i][j]/val
                    u[i]=u[i]-x*u[pivot_row]
            else:
                l[i][j]=0
            if i==j:
                l[i][j]=1
        pivot_col=pivot_col+1
        pivot_row=pivot_row+1  
    return l,u

def getEchelon(arr: np.array, size: int):
    pass
def forSubs(l,b,size):
    aug_matrix = np.array(l,copy=True)
    np.hstack((aug_matrix, b.reshape(-1,1)))
    result = getEchelon(aug_matrix,size)
    return result[:,-1]

def backSub(u,y,size):
    pass

if __name__=="__main__":
    n, m  = input().split()
    n, m = int(n), int(m)
    arr = np.empty((n,n))
    for i in range(n):
        arr[i] = [int(x) for x in input().split()]
    l,u = getLU(arr,n)
    for i in range(m):
        b = [int(x) for x in input().split()]
        y = forSubs(l,b,n)
        x = backSub(u,y,n)
        print(*x)
