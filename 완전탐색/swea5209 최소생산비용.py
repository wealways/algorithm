import sys
sys.stdin = open('최소생산비용.txt')

def dfs(k,temp):
    global result
    if result <= temp:
        return
    if k==N:

        if result >= temp:
            result = temp
        return
    else:
        for i in range(N):
            if not visit[i]:
                visit[i]=1
                dfs(k+1,temp+data[k][i])
                visit[i]=0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    visit = [0]*N
    result = 999999999999
    temp = 0
    dfs(0,0)
    print('#{} {}'.format(tc,result))