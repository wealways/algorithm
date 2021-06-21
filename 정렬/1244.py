import sys
sys.stdin = open('swea1244.txt')

def solveR(numL,n):
    global maxVal

    num = int(''.join(numL))

    if n ==K:
        if num > maxVal:
            maxVal = num
    else:
        for i in range(len(numL)-1):
            for j in range(1,len(numL)):
                numL[i],numL[j] = numL[j],numL[i]
                solveR(numL,n+1)
                if maxVal == possible: return
                numL[i],numL[j] = numL[j],numL[i]

T = int(input())
for tc in range(1,T+1):
    l1,l2 = input().split()
    ARR =list(l1)
    K = int(l2)

    possible = int(''.join(sorted(ARR,reverse=True)))
    maxVal = 0
    solveR(ARR,0)

    print('#{} {}'.format(tc,maxVal))