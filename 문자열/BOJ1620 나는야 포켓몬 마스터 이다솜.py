import sys
sys.stdin = open('BOJ1620.txt')

N,M = map(int,sys.stdin.readline().split())
dogam_arr = []
dogam = {}
for n in range(1,N+1):
    temp = sys.stdin.readline().rstrip()
    dogam_arr.append(temp)
    dogam[temp]=n

for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        print(dogam_arr[int(temp)-1])
    else:
        print(dogam[temp])