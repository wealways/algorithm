import sys
sys.stdin = open('BOJ11047.txt')

N, K = map(int,sys.stdin.readline().split())

money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))
money.sort(reverse=True)

idx = 0
cnt = 0
while K>0:
    if money[idx]>K:
        idx += 1
    else:
        temp = K//money[idx]
        cnt += temp
        K -= money[idx] * temp

print(cnt)
