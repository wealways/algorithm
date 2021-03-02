# import sys
# sys.stdin = open('BOJ2164.txt')

N = int(input())
cnt = 1
while True:
    if N<= 2**cnt:
        break
    cnt += 1

if N ==1:
    print(1)
elif N==2:
    print(2)
else:
    print(2**cnt - 2*(2**cnt-N))

# print(2*(N-2**(cnt-1)))



    # cards = [i for i in range(1,N+1)]
    #
    # cnt = 1
    # while True:
    #     if len(cards)==1:
    #         break
    #     temp = cards.pop(0)
    #     if cnt % 2==0:
    #         cards.append(temp)
    #     cnt += 1
    #
    # print(cards[0])


# 1 2 2 4 2 4 6 8 2 4