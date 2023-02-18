//
//  다음 큰 숫자.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/18.
//

func solution(_ n: Int) -> Int {
    
    var answer: Int = n
    
    while true {
        let nCount = String(n, radix: 2).filter { $0 == "1" }.count
        answer += 1
        if nCount == String(answer, radix: 2).filter({ $0 == "1" }).count {
            return answer
        }
    }
    
    return answer
}
