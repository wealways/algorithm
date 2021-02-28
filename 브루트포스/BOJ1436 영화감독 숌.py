import sys
sys.stdin = open('BOJ1436.txt','r')

n = int(input())

x = 666

while n:                        # n번만큼 반복
    if '666' in str(x):         # x에 666이 있다면
        n -= 1
    x += 1

print(x - 1)