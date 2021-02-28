import sys
sys.stdin = open('BOJ11050.txt','r')

N,K = map(int,input().split())

if N//2 <K:
    K = N-K

cardinal = 1
ordinal  = 1
for i in range(1,K+1):
    cardinal *= (N-i+1)
    ordinal *= i
print(cardinal//ordinal)