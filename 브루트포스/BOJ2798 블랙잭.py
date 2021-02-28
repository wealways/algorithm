import sys
sys.stdin = open('BOJ2798.txt','r')

def find(v,sumV):
    global result
    if v==3:
        if sumV <=M:
            result = max(sumV,result)
        return
    if sumV > M:
        return
    for card in card_list:
        if card not in visit:
            visit.append(card)
            find(v+1,sumV+card)
            visit.pop()


T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    card_list = list(map(int,input().split()))
    visit=[]
    result = 0
    find(0,0)
    print(result)