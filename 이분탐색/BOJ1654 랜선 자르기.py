import sys
sys.stdin = open('BOJ1654.txt','r')

K,N = map(int,input().split())

string_list = [int(input()) for _ in range(K)]
start, end = 1, max(string_list)

while start <= end:
    mid = (start+end)//2

    temp_N = 0
    for string in string_list:
        temp_N += string//mid

    if temp_N >= N:
        start = mid +1
    else:
        end = mid -1

print(end)
















