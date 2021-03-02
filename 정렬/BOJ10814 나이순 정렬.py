import sys
sys.stdin = open('BOJ10814.txt')

N = int(input())

lines = [[] for _ in range(200)]
for _ in range(N):
    age, name = input().split()
    lines[int(age)-1].append(name)

for idx,line in enumerate(lines):
    if len(line):
        for l in line:
            print('{} {}'.format(idx+1,l))