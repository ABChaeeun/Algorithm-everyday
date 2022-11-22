def solution(brown, yellow):
    # 전체 면적 = brown+yellow의 갯수 = height*width
    s = brown +yellow
    ans = [0,0]
    
    for width in range(s-1,0,-1):
        if s%width :
            continue
        height = s/width;
        y = (width-2)*(height-2)
        b = s-y
        if(y==yellow and b==brown):
            ans[0] = width
            ans[1] = height
            break
    
    return ans