//
//  카펫.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/14.
//

import Foundation

func solution(_ brown: Int, _ yellow: Int) -> [Int] {
    var total = brown + yellow
    var b = 0
    
    for i in 3...total/2 {
        if total % i == 0 {
            b = total / i
            if b >= 3 && (2*b + 2*i - 4 == brown) && i >= b {
                return [i, b]
            }
        }
    }
    
    return []
}
