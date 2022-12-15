function solution(s){
    var answer = true;
    let p_cnt = 0;
    let y_cnt = 0;
   
    if (s.includes('p') || s.includes('P')) {
        p_cnt = s.match(/p/gi).length
    }
    if (s.includes('y') || s.includes('Y')) {
        y_cnt = s.match(/y/gi).length
    }

    if (p_cnt == y_cnt) {
        answer = true
    } else if (p_cnt != y_cnt) {
        answer = false
    } else {
        answer = true
    }
    
    return answer;
}
