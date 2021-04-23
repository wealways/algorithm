import sys

sys.stdin = open('BOJ14500.txt')

N,M = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dr=[0,0,1,-1]
dc=[1,-1,0,0]

result = 0
maxval = max(map(max, arr))

def dfs(cnt,sumV,r,c):
    global result
    if sumV + (3-cnt) * maxval <=result:
        return
    if cnt ==3:
        result = max(sumV,result)
        return
    else:
        for i in range(4):
            temp_r = r +dr[i]
            temp_c = c +dc[i]
            if 0<= temp_c < N and 0<=temp_r<M and not visit[temp_c][temp_r]:
                if cnt==1:
                    visit[temp_c][temp_r] = 1
                    dfs(cnt + 1, sumV + arr[temp_c][temp_r], r, c)
                    visit[temp_c][temp_r]=0

                visit[temp_c][temp_r]=1
                dfs(cnt+1,sumV+arr[temp_c][temp_r],temp_r,temp_c)
                visit[temp_c][temp_r]=0

visit = [[0] * M for _ in range(N)]
for c in range(N):
    for r in range(M):
        visit[c][r]=1
        dfs(0,arr[c][r],r,c)
        visit[c][r]=0

print(result)
