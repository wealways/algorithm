import sys
sys.stdin = open('전기버스.txt')

def chk(k):
    global cnt, result

    if k >= N:
        if result >cnt:
            result = cnt
        return
    if result < cnt:
        return
    start = k
    b = battary[start]
    for i in range(start+b, start, -1):
        cnt += 1
        chk(i)
        cnt -= 1

T = int(input())
for tc in range(1,T+1):
    battary = list(map(int,input().split()))
    N = battary[0]
    cnt = 0
    result = 9999999
    chk(1)
    print('#{} {}'.format(tc,result-1))


