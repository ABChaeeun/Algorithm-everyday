def solution(s):
    lists = list(map(int, s.split()))
    answer = str(min(lists)) + " " + str(max(lists))
    return answer 
    