import sys
sys.stdin = open('BOJ1541.txt')

arr = list(sys.stdin.readline().split('-'))
result = 0
for a in arr[0].split('+'):
    result += int(a)
for a in arr[1:]:
    for i in a.split('+'):
        result -= int(i)
print(result)