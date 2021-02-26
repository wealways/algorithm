import sys
sys.stdin = open('BOJ1259.txt','r')

while True:
    N = int(input())
    if N==0: break

    temp = list(str(N))
    temp_len = len(temp)
    flag = 0
    for n in range(temp_len//2):
        if temp[n]!=temp[temp_len-n-1]:
            flag = 1
            break
    if flag==0:
        print('yes')
    else:
        print('no')

