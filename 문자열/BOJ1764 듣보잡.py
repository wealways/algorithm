import sys
sys.stdin = open('BOJ1764.txt')

N,M = map(int,sys.stdin.readline().split())
user = {}
for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    user[temp] = 1

result = []
for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    if user.get(temp):
        result.append(temp)

print(len(result))
result = sorted(result)
for r in result:
    print(r)
