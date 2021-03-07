import sys
sys.stdin = open('BOJ9012.txt')

# for _ in range(int(input())):
#     for _ in range(int(input())):
#         ps = list(input())
#         result=[]
#         temp = []
#         for p in ps:
#             if len(result)==0:
#                 result.append(p)
#             else:
#                 if p !=')':
#                     result.append(p)
#                 else:
#                     while True:
#                         t = result.pop()
#                         if t=='(':
#                             temp = []
#                             break
#                         else:
#                             temp.append(t)
#                         if len(result) ==0:
#                             result += temp
#                             break
#         if len(result):
#             print('NO')
#         else:
#             print('YES')

for _ in range(int(input())):
    ps = list(input())
    result=[]
    temp = []
    for p in ps:
        if len(result)==0:
            result.append(p)
        else:
            if p !=')':
                result.append(p)
            else:
                while True:
                    t = result.pop()
                    if t=='(':
                        temp = []
                        break
                    else:
                        temp.append(t)
                    if len(result) ==0:
                        result += temp
                        temp = []
                        break
    if len(result):
        print('NO')
    else:
        print('YES')



