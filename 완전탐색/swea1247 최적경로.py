import sys
sys.stdin = open('swea1247 최적경로.txt')

def dfs(xy:tuple,k,temp):
    global result
    if result <= temp:
        return
    if k == N:
        temp += abs(xy[0]-data[2])+abs(xy[1]-data[3])
        result = min(result, temp)
        return
    else:
        for i,m in enumerate(mapping):
            if not visit[i]:
                visit[i]=1
                x = xy[0]
                y = xy[1]
                mx = m[0]
                my = m[1]
                dfs(m,k+1,temp+abs(x-mx)+abs(y-my))
                visit[i]=0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    mapping = []
    for i in range(2, N+2):
        mapping.append((data[2*i], data[2*i+1]))

    visit = [0]*N
    result = 9999999999
    dfs((data[0], data[1]), 0, 0)
    print('#{} {}'.format(tc,result))