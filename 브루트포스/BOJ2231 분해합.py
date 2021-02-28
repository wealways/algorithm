# import sys
# sys.stdin = open('BOJ2231.txt','r')

# N = int(input())
#
# for n in range(1,N+1):
#     temp = n
#     result = n
#
#     while temp != 0:
#         result += temp%10
#         temp =  temp//10
#
#     if result ==N:
#         break
#     if n == N and result !=N :
#         n = 0
#
# print(n)

N = input()
len_n = len(N)
temp = int(N)-8*len_n
temp = 1 if temp <1 else temp

for n in range(temp,int(N)+1):
    result = int(n)
    result += sum(map(int,str(n)))

    if (result == int(N)):
        print(n)
        break
    if n==int(N) and result!=int(N):
        print(0)


