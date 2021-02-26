import sys
sys.stdin = open('BOJ1181.txt','r')

N = int(input())

word_list = []
for n in range(N):
    word = input()
    word_list.append((word,len(word)))

word_list = list(set(word_list))

word_list.sort(key = lambda word:(word[1],word[0]))

for word in word_list:
    print(word[0])
