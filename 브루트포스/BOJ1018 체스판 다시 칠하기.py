import sys
sys.stdin = open('BOJ1018.txt','r')

N = int(input())

for tc in range(1,N+1):
    R,C = map(int,input().split())

    pan = []
    for _ in range(R):
        pan.append(list(input()))

    result = []

    for r in range(R-8+1):
        for c in range(C-8+1):
            cnt1 = 0
            cnt2 = 0

            for i in range(8):
                for j in range(8):

                    compareV = pan[r+i][c+j]
                    if (i+j)%2 == 0:
                        if compareV=='W': cnt1 += 1
                        if compareV == 'B' : cnt2 += 1
                    else:
                        if compareV == 'B' : cnt1 += 1
                        if compareV =='W' : cnt2 += 1
            result.append(cnt1)
            result.append(cnt2)
    print(min(result))