function solution(n) {
    var answer = 0;
    
    let oneCount = n.toString(2).match(/1/g).length
    
    while (true) {
        n++
        if (oneCount == n.toString(2).match(/1/g).length) {
            return n
        }
    }
    
    // return answer;
}