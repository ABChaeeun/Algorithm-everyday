//
//  네트워크.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/15.
//

import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var visited = [Bool](repeating: false, count: n)
    var queue: [Int] = []
    var v = 0
    var answer = 0
    
    for idx in visited.indices {
        if visited[idx] == false {
            answer += 1
            queue.append(idx)
            visited[idx] = true
        }

        while queue.count > 0 {
            v = queue.removeLast()
            for i in 0..<n {
                if computers[v][i] == 1 && visited[i] == false {
                    queue.append(i)
                    visited[i] = true
                }
            }
        }
    }
    
    return answer
}
