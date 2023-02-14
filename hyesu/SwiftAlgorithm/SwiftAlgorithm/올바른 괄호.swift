//
//  올바른 괄호.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/14.
//

import Foundation

func solution(_ s: String) -> Bool {
    var ans: Bool = true
    var c: Int = 0
    
    for i in s.indices {
        if s[i] == "(" {
            c += 1
        }
        else {
            if c > 0 {
                c -= 1
            }
            else {
                ans = false
                break
            }
        }
    }
    
    if c > 0 {
        ans = false
    }

    return ans
}
