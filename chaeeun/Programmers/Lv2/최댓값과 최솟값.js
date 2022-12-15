function solution(s) {
    var answer = '';
    
    let s_arr = s.split(' ')
    s_arr = s_arr.map(x => parseInt(x))
    
    answer += Math.min(...s_arr)
    answer += ' '
    answer += Math.max(...s_arr)
    
    return answer;
}
