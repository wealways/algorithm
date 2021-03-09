import sys
sys.stdin = open('BOJ11866.txt')

N,K = map(int,input().split())

arr = [i for i in range(1,N+1)]
visit = [0]*N
v=1
print('<',end='')
while sum(visit)!=N:
    for i in range(N):
        if visit[i] ==0 and v==K:
            if sum(visit)==N-1:
                print(arr[i],end='')
            else:
                print(arr[i],end=', ')
            v= 1
            visit[i]=1
        if visit[i]==0 and v != K:
            v+=1
print('>')