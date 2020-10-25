def solution(array, commands):
    answer = []
    
    for command in commands:
        start_idx = command[0]-1
        end_idx = command[1]
        idx = command[2]-1
        answer.append(sorted(array[start_idx:end_idx])[idx])
    return answer