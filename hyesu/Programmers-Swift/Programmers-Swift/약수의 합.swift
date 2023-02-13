//
//  main.swift
//  Programmers-Swift
//
//  Created by 김혜수 on 2023/02/13.
//

import Foundation

func solution(_ n:Int) -> Int {
    
    if n == 0 {
        return 0
    }
    
    let array = Array(1...n)
    let newArray = array.filter { (n % $0 == 0) }
    return newArray.reduce(0, +)
}
