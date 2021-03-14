import sys
sys.stdin = open('BOJ18870.txt')
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
dic = {i:0 for i in arr}

temp = 0
for idx,a in enumerate(sorted(arr)):
    if idx==0:
        dic[a] = temp
        pre = a
    else:
        if pre == a:
            dic[a] = temp
        else:
            temp += 1
            dic[a]=temp
            pre = a
for a in arr:
    print(dic[a],end=' ')