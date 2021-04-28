# import sys
# sys.stdin=open('BOJ10026.txt')
#
# N = int(sys.stdin.readline())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# visit = [[0]*N for _ in range(N)]
# dr=[0,0,1,-1]
# dc=[1,-1,0,0]
#
# # [정상, 적록색약]
# result1 = 0
# result2 = 0
#
# def dfs(c,r):
#     visit[c][r] = 1
#     for i in range(4):
#         temp_c,temp_r = c+dc[i], r+dr[i]
#         if 0<=temp_c<N and 0<=temp_r<N and visit[temp_c][temp_r] == 0:
#             if arr[c][r]==arr[temp_c][temp_r]:
#                 dfs(temp_c,temp_r)
#
# for c in range(N):
#     for r in range(N):
#         if visit[c][r]==0:
#             result1 += 1
#             dfs(c,r)
#
# for c in range(N):
#     for r in range(N):
#         if arr[c][r]=='R':
#             arr[c][r]='G'
#
# visit = [[0]*N for _ in range(N)]
# for c in range(N):
#     for r in range(N):
#         if visit[c][r]==0:
#             result2 += 1
#             dfs(c,r)
#
#
#
# print(result1,result2)
import sys
from collections import deque
sys.stdin=open('BOJ10026.txt')
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(c, r):
    q.append([c, r])
    visit[c][r] = 1
    while q:
        c, r = q.popleft()
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < n and 0 <= nr < n:
                if arr[nc][nr] == arr[c][r] and visit[nc][nr] == 0:
                    q.append([nc, nr])
                    visit[nc][nr] = 1

n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
q = deque()

cnt = 0
for c in range(n):
    for r in range(n):
        if visit[c][r] == 0:
            bfs(c, r)
            cnt += 1
print(cnt, end=' ')

for c in range(n):
    for r in range(n):
        if arr[c][r] == 'R':
            arr[c][r] = 'G'
visit = [[0]*n for _ in range(n)]

cnt = 0
for c in range(n):
    for r in range(n):
        if visit[c][r] == 0:
            bfs(c, r)
            cnt += 1
print(cnt)