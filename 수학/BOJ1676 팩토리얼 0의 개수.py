import sys
sys.stdin = open('BOJ1676.txt')

from math import factorial

arr = list(str(factorial(int(sys.stdin.readline()))))

arr = arr[::-1]
result = 0
for idx,x in enumerate(arr):
    if idx==0 and x !='0':
        break
    elif x=='0':
        result += 1
    else:
        break
print(result)