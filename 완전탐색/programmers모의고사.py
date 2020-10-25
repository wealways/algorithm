def solution(answers):
    answer = []
    a=[1,2,3,4,5] #5
    b=[2,1,2,3,2,4,2,5] #8
    c=[3,3,1,1,2,2,4,4,5,5] #10
    result=[0,0,0]
    
    # 답의 길이만큼 패턴이 순회를 하기 때문에 다음과 같은 구조를 만들었습니다
    for idx,data in enumerate(answers):
        if a[idx%len(a)]==data:
            result[0] += 1
        if b[idx%len(b)]==data:
            result[1] +=1
        if c[idx%len(c)]==data:
            result[2] +=1
            
    for idx,data in enumerate(result):
        if max(result) == data:
            answer.append(idx+1)
    return answer