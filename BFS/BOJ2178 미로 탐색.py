import sys
from collections import deque
sys.stdin = open('BOJ2178.txt')

dx=[0,0,1,-1]
dy = [1,-1,0,0]

def find():
    global ans
    q= deque()
    q.append((0,0,1))
    arr[0][0]=0
    while q:
        r,c,temp = q.popleft()
        if temp >= ans:
            continue
        if r==R-1 and c==C-1:
            ans = min(ans,temp)
            return
        for i in range(4):
            temp_r,temp_c = r + dx[i],c+dy[i]
            if 0<=temp_r<R and 0<=temp_c<C:
                if arr[temp_r][temp_c] ==1:
                    q.append((temp_r,temp_c,temp+1))
                    arr[temp_r][temp_c]=0



for _ in range(int(input())):
    R,C = map(int,sys.stdin.readline().split())
    arr=[]
    ans = R*C
    for _ in range(R):
        arr.append(list(map(int,sys.stdin.readline().rstrip())))
    find()
    print(ans)
