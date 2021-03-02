import sys
sys.stdin = open('BOJ7568.txt')

N = int(input())

mans = []
for _ in range(N):
    mans.append(list(map(int,input().split())))

for i in range(N):
    cnt = 1
    for j in range(N):
        if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1]:
            cnt += 1
    print(cnt,end=' ')
