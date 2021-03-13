import sys
sys.stdin=open('BOJ1931.txt')
time = []

for _ in range(int(input())):
    temp = list(map(int,sys.stdin.readline().split()))
    time.append(temp)

time.sort(key=lambda x:(x[1],x[0]))

cnt = 1
end_time=time[0][1]
for i in range(1,len(time)):
    if time[i][0]>=end_time:
        cnt += 1
        end_time = time[i][1]
print(cnt)


