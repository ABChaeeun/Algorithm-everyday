function solution(brown, yellow) {
    var answer = [];
    
    // 약수들로 접근!
    var arr = []
    for (let i = 1; i <= yellow; i++) {
        if (yellow % i == 0) {
            if (i <= yellow/i) {
                if ((i*2)+((yellow/i)*2)+4 == brown) {
                    answer = [yellow/i+2, i+2]
                }
            } else {
                break
            }
        }
    }
    
    return answer;
}