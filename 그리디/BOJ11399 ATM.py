import sys
sys.stdin = open('BOJ11399.txt')

N = int(sys.stdin.readline())
arr = list(map(int,list(sys.stdin.readline().split())))

arr = sorted(arr)
result = []
for n in range(N):
    if n ==0:
        result.append(arr[0])
    else:
        result.append(result[n-1]+arr[n])
print(sum(result))


# visit = [0]*N
# ans = 1000 * 1000
# def find(v,m):
#     global ans
#     if sum(visit)>=ans:
#         return
#     if v==N:
#         ans = min(ans,sum(visit))
#         return
#     else:
#         for i in range(N):
#             if not visit[i]:
#                 visit[i] = arr[i] + m
#                 find(v+1,m+arr[i])
#                 visit[i] = 0
# find(0,0)
#
# print(ans)