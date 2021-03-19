import sys
sys.stdin = open('BOJ9461.txt')

for _ in range(int(input())):
    N = int(sys.stdin.readline())
    arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    if N<=10:
        print(arr[N])
    else:
        for n in range(11,N+1):
            arr.append(arr[n-5]+arr[n-1])

        print(arr.pop())


