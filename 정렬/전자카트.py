def chk(k):
    if k==N:
				# 문제의 조건을 따르는 과정
        if path[0]==0:
            temp = 0
            for i in range(N):
                temp += data[path[i]][path[i+1]]
            result.append(temp)
    else:
				# 이 부분은 순열을 만드는 과정
        for i in range(N):
            if used[i] == 0:
                path[k]=i
                used[i]=1
                chk(k+1)
                used[i]=0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    path = [0]*(N+1)
    used= [0]*N
    result = []
    chk(0)
    print('#{} {}'.format(tc,min(result)))