import sys
import heapq

sys.stdin = open('BOJ11279.txt')

heap = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)*-1)
    else:
        heapq.heappush(heap,n*-1)

