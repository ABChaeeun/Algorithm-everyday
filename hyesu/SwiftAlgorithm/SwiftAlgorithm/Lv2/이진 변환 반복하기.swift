//
//  이진 변환 반복하기.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/17.
//

import Foundation

func solution(_ s:String) -> [Int] {
    var zero: Int = 0
    var count: Int = 0
    var a: String = s
    
    while a != "1" {
        zero += a.filter { $0 == "0" }.count
        a.removeAll { $0 == "0" }
        a = String(a.count, radix: 2)
        
        count += 1
    }
        
    return [count, zero]
}
