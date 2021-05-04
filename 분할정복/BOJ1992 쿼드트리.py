import sys
sys.stdin = open('BOJ1992.txt')

N = int(input())

arr=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
result = []

def find(r,c,n):
    if n == 1:
        print(arr[c][r],end="")
        return
    flag=True
    for i in range(c,c+n):
        if not flag:
            break
        for j in range(r,r+n):
            if arr[i][j] != arr[c][r]:
                flag = False
                break

    if flag:
        print(arr[c][r],end="")
    else:
        print('(',end="")
        find(r,c,n//2)
        find(r+n//2,c,n//2)
        find(r,c+n//2,n//2)
        find(r+n//2,c+n//2,n//2)
        print(')',end="")
find(0,0,N)