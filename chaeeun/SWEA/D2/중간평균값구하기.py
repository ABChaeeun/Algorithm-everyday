# import numpy as np # -> SWEA 에서 컴파일 에러!

T = int(input())

for tc in range(1, T+1):

    lst = list(map(int, input().split()))

    lst.remove(max(lst))
    lst.remove(min(lst))

    ### numpy 이용 ###
    # lst_numpy = np.array(lst)
    # med_mean = np.mean(lst_numpy)
    # med_mean = int(np.round_(med_mean, 0))

    ### 그냥 구하기 ###
    med_mean = sum(lst) / len(lst)
    med_mean = round(med_mean)
    
    
    print('# {} {}'.format(tc, med_mean))

# 평균 구하는 방법
# 1. for 반복문 이용
# 2. sum 함수를 이용
# 3. numpy 모듈 이용
# 4. statiscics 라이브러리 이용