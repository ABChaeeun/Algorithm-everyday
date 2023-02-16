//
//  JadenCase 문자열 만들기.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/16.
//

func solution(_ s:String) -> String {
    var isUpper: Bool = true
    var answer: String = ""
    
    for idx in 0..<s.count {
        var stringIdx = s.index(s.startIndex, offsetBy: idx)
        if s[stringIdx] == " " {
            isUpper = true
            answer += " "
        }
        else {
            answer += isUpper ? s[stringIdx].uppercased() : s[stringIdx].lowercased()
            isUpper = false
        }
    }
    
    return answer
}
