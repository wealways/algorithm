import sys

sys.stdin = open('BOJ1780.txt')

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = [0,0,0]
def check(x,y,n):
    temp = arr[x][y]
    for c in range(x,x+n):
        for r in range(y,y+n):
            if temp != arr[c][r]:
                # 1 번째라인
                check(x,y,n//3)
                check(x, y+n // 3, n // 3)
                check(x, y + (n // 3)*2, (n // 3))
                # 2번째라인
                check(x+ n // 3, y , n // 3)
                check(x + n // 3, y+ n // 3, n // 3)
                check(x + n // 3, y + (n // 3)*2, (n // 3))
                # 3번째라인
                check(x+ (n // 3) * 2, y , (n // 3) )
                check(x + (n // 3) * 2, y+n//3, (n // 3) )
                check(x + (n // 3) * 2, y+ (n // 3) * 2, (n // 3) )
                return
    if temp==-1:
        result[0] +=1
    elif temp==0:
        result[1] +=1
    else:
        result[2] +=1
check(0,0,N)
print(result[0])
print(result[1])
print(result[2])