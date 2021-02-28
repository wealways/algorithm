import sys
sys.stdin = open('BOJ1920.txt','r')

N = int(input())
N_list = list(map(int,input().split()))
N_list = sorted(N_list)
M = int(input())
M_list = list(map(int,input().split()))

#
# def binary_search(v,start,end):
#     if start > end:
#         return 0
#     mid = (start+end)//2
#     if v == N_list[mid]:
#         return 1
#     elif v<N_list[mid]:
#         return binary_search(v,start,mid-1)
#     else:
#         return binary_search(v,mid+1,end)
#
# for m in M_list:
#     print(binary_search(m,0,N-1))

for m in M_list:
    if m in N_list:
        print(1)
    else:
        print(0)