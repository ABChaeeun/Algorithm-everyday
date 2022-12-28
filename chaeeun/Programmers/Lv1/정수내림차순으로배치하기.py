def solution(n):
    answer = ''
    
    str_nums = str(n)
    nums = list(map(int, str_nums))
    nums.sort(reverse=True)
    
    for i in range(len(nums)):
        answer += str(nums[i])  
    
    return int(answer)
