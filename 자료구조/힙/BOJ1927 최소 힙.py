import sys
sys.stdin = open('BOJ1927.txt')
import heapq

heap=[]

for _ in range(int(input())):
    temp = int(sys.stdin.readline())
    if temp==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,temp)
