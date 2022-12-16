// 스택 참고

function solution(s) {
    stack = []
    
    let i = 0
    while (true) {
        if (stack[stack.length-1] != s[i])
            stack.push(s[i])
        else
            stack.pop()
        i++
        if (i == s.length) break
    }
    return stack.length == 0 ? 1 : 0;
}
