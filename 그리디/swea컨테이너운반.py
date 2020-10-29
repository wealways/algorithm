import sys
sys.stdin = open('컨테이너운반.txt')

T = int(input())

for tc in range(1,T+1):
    # 컨테이너수, 트럭수
    N,M = map(int,input().split())
    # N개 만큼 컨테이너 무게
    container = list(map(int,input().split()))
    container.sort()
    # M개 만큼 트럭의 적재용량
    truck  = list(map(int,input().split()))
    truck.sort()
    answer = 0
    for t in truck:
        temp = 0
        for c in container:
            if t >= c :
                temp= c
        if temp:
            answer += temp
            container.remove(temp)

    print('#{} {}'.format(tc,answer))
