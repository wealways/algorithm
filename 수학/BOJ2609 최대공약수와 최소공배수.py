import sys
sys.stdin = open('BOJ2609.txt','r')

A,B = map(int,input().split())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a = gcd(A,B)
print(a)
print(A*B//a)

