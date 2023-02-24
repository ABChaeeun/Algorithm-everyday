//
//  짝지어 제거하기.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/24.
//

import Foundation

func solution(_ s: String) -> Int {
    var stack: [Character] = []
    
    for i in s {
        if let last = stack.last,
           last == i {
            stack.removeLast()
        } else {
            stack.append(i)
        }
    }
    
    if stack.isEmpty {
        return 1
    }
        
    return 0
}

print(solution("baabaa"))

