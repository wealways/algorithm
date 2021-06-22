import sys
import heapq
sys.stdin = open('복습.txt')
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dc = [1,-1,0,0]
dr = [0,0,1,-1]

def visitable(x, y, size, visit):
    return 0 <= x < n and 0 <= y < n and arr[x][y] <= size and not visit[x][y]


def bfs(idx,baby):
    size, eat, answer = 2,0,0
    heap = []
    heapq.heappush(heap,(idx,baby[0],baby[1]))
    visit = [[False]*n for _ in range(n)]

    while heap:
        idx,x,y = heapq.heappop(heap)

        # 물고기 먹을 수 있어?
        if 0<arr[x][y]<size:
            eat += 1
            arr[x][y] = 0
            if eat == size:
                size += 1
                eat = 0
            answer += idx
            idx = 0

            # 방문여부 초기화
            heap = []
            visit = [[False]*n for _ in range(n)]

        for i in range(4):
            next_x, next_y = x+dr[i],y+dc[i]

            if visitable(next_x,next_y,size,visit):
                visit[next_x][next_y] = True
                heapq.heappush(heap,(idx+1,next_x,next_y))
    return answer



for c in range(n):
    for r in range(n):
        if arr[c][r]==9:
            arr[c][r]=0
            print(bfs(0,[c,r]))
            break
