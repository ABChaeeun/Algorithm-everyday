function solution(s) {
    var answer = 0    
    s = s.split('')
    
    for (let i = 0; i < s.length; i++) {
        var stack = []
        
        s.push(s.shift())        
        for (let j = 0; j < s.length; j++) {
            if (s[j] == '(' || s[j] == '{' || s[j] == '[') {
                stack.push(s[j])
            } else if (s[j] == ')') {
                if (stack[stack.length-1] == '(') stack.pop()
                else stack.push(s[i])
            } else if (s[j] == '}') {
                if (stack[stack.length-1] == '{') stack.pop()
                else stack.push(s[i])
            } else if (s[j] == ']') {
                if (stack[stack.length-1] == '[') stack.pop()
                else stack.push(s[i])
            }
        }
        // console.log(stack)
        if (stack.length == 0) answer++
    }
    return answer
}
