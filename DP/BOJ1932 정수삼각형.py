import sys

sys.stdin = open('BOJ1932.txt')
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]

for n in range(N):
    arr[n] = list(map(int,input().split()))

for i in range(1, N):
    for j in range(0, len(arr[i])):
        if j == 0 :
            arr[i][j] = arr[i-1][j] + arr[i][j]
        elif len(arr[i])-1 == j :
            arr[i][j] = arr[i-1][j-1] + arr[i][j]
        else :
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-1]) + arr[i][j]

print(max(arr[N-1]))