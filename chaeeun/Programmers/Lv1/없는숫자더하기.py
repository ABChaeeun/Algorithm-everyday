all_nums = [0,1,2,3,4,5,6,7,8,9]

def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        if numbers[i] in all_nums:
            all_nums.remove(numbers[i])
            
    for i in all_nums:
        answer += i
    return answer