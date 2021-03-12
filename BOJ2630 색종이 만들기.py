import sys
sys.stdin = open('BOJ2630.txt')

N = int(input())
paper = []
result = [0,0]
for _ in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

def check(x,y,n):
    temp = paper[x][y]
    for r in range(x,x+n):
        for c in range(y,y+n):
            if temp !=paper[r][c]:
                check(x,y,n//2)
                check(x,y+n//2,n//2)
                check(x+n//2,y,n//2)
                check(x+n//2,y+n//2,n//2)
                return
    result[temp] += 1
    return

check(0,0,N)
print(result[0])
print(result[1])
