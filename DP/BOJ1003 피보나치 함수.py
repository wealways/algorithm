import sys
sys.stdin = open('BOJ1003.txt')

def fibo(n):
    global a, b
    if n==0:
        a += 1
        return 0
    elif n==1:
        b += 1
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo2(N):
    for n in range(N+1):
        if n==0:
            arr[0]=0
        elif n==1:
            arr[1]=1
        else:
            arr[n] = arr[n-1] + arr[n-2]

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    a=b=0
    arr=[0]*(N+1)
    # fibo(N)
    # print(a,end=' ')
    # print(b)
    fibo2(N)
    if N ==0:
        print(1,0)
    else:
        print(arr[-2],arr[-1])
    # print(arr[-2],arr[-1])