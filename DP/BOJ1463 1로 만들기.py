import sys
sys.stdin = open('BOJ1463.txt')

# def find(cnt,k):
#     global ans
#     if ans<=k:
#         return
#     if k==1:
#         ans = min(ans,cnt)
#         return
#     else:
#         for i in range(3):
#             if i==0 and k % 3 ==0:
#                 find(cnt+1,int(k//3))
#             elif i==1 and k % 2 ==0:
#                 find(cnt+1, int(k//2))
#             else:
#                 find(cnt+1, k-1)


for _ in range(int(input())):
    N = int(input())
    # ans = 999999999999
    # find(0,N)
    # print(ans)
    dp = [0 for _ in range(N+1)]

    for i in range(1,N+1):
        if i==1:
            dp[i]=0
        else:
            dp[i] = dp[i-1]+1
            if i%3 ==0:
                dp[i] = min(dp[i],dp[i//3]+1)
            if i% 2 ==0:
                dp[i] = min(dp[i],dp[i//2]+1)

    print(dp[N])