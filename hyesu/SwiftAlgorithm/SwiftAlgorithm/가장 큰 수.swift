//
//  가장 큰 수.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/14.
//

import Foundation

func solution(_ numbers: [Int]) -> String {
    
    let newNumbers = numbers.sorted {
        String($0) + String($1) > String($1) + String($0)
    }
    
    if numbers.last! == 0 {
        return "0"
    }
  
    return newNumbers.map { String($0) }.joined()
}
