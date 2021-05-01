import numpy as np

def getLU(arr: np.array, n: int):
    l = np.zeros((n,n))
    r = 0
    pivot_pos=[0,0]
    for i in range(n):
        for j in range(n):
            if i==j:
                l[i][j]=1
                r = arr[i][j]
            elif j>i:
                l[i][j]=0
            else:
                pass

def getU(arr: np.array, n: int):
    l = np.array(arr,copy=True)
    pivot_row=0
    pivot_col=0
    for j in range(n):
        val = l[pivot_row][pivot_col]
        for i in range(n):
            if i>pivot_row: 
                print(val)
                if l[i][j]!= 0:
                    x= l[i][j]/val
                    l[i]=l[i]-x*l[pivot_row]
        pivot_col=pivot_col+1
        pivot_row=pivot_row+1  
    return l
def forSubs():
    pass

def backSub():
    pass

if __name__=="__main__":
    n, m  = input().split()
    n, m = int(n), int(m)
    arr = np.empty((n,n))
    for i in range(n):
        arr[i] = [int(x) for x in input().split()]
    U = getU(arr,n)
    print(U)
