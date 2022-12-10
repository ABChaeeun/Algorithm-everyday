
def solution(gems):
    answer = [0,len(gems)]
    size = len(set(gems)) # 보석 종류 갯수
    ruby = {gems[0]:1}
    print(ruby)
    left, right = 0,0
    while left < len(gems) and right < len(gems):
        if len(ruby) == size :#루비만큼 다돌면 확인 
            if right - left <answer[1]- answer[0]:#만약 길이가 짧으면 갱신
                answer = [ left, right ]
            else :
                ruby[gems[left]] -= 1#그개 아니라면 left를 하나씩 전진시켜서 확인
                if ruby[gems[left]] == 0:
                    del ruby[gems[left]]
                left +=1
        else :
            right += 1
            if right == len(gems):
                break
            if gems[right] in ruby:
                ruby[gems[right]] += 1
            else :
                ruby[gems[right]] = 1
    return [answer[0]+1,answer[1]+1]