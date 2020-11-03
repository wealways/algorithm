import sys
sys.stdin = open('5207이진탐색.txt')

def chk(val,idxl,idxr,flag):
    global cnt

    if idxl > idxr:
        return

    m = (idxl+idxr)//2

    if val == narr[m]:
        cnt += 1

    else:
        if narr[m] > val:
            if flag==1: return
            else:
                flag=1
                chk(val,idxl,m-1,flag)
        elif narr[m] < val:
            if flag == -1:return
            else:
                flag = -1
                chk(val,m+1,idxr,flag)
        else:
            return


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    narr = list(map(int,input().split()))
    narr = sorted(narr)
    marr = list(map(int,input().split()))
    cnt = 0
    visit = [0,0]
    flag=0
    for mval in marr:
        chk(mval,0,N-1,flag)
    print('#{} {}'.format(tc,cnt))