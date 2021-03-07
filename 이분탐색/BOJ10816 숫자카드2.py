import sys
sys.stdin = open('BOJ10816.txt')

def binary_search(arr,v,start,end):
    if start>end:
        return 0
    mid = (start+end)//2
    if arr[mid]==v:
        return 1
    elif v<arr[mid]:
        return binary_search(arr,v,start,mid-1)
    else:
        return binary_search(arr,v,mid+1,end)


N = int(input())
cards = list(map(int,input().split()))
M = int(input())
numbers = list(map(int,input().split()))
dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in numbers:
    if i in dic:
        print(dic[i] , end = " ")
    else:
        print(0, end=" ")

result = {}
for number in numbers:
    result[number]=0

numbers = sorted(numbers)



for card in cards:
    if binary_search(numbers,card,0,M-1):
        result[card] += 1

print(' '.join(str(v) for v in result.values()))
