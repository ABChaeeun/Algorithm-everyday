//
//  K번째수.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/14.
//

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    
    var answer: [Int] = []
    
    var i: Int = 0
    var j: Int = 0
    var k: Int = 0
    
    for idx in commands.indices {
        i = commands[idx][0]
        j = commands[idx][1]
        k = commands[idx][2]
        
        let slicedArray = array[i-1..<j].sorted()
        answer.append(slicedArray[k-1])
    }
    
    return answer
}
