//
//  최솟값 만들기.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/16.
//

func solution(_ A:[Int], _ B:[Int]) -> Int {
    var ans = 0

    let a = A.sorted()
    let b = B.sorted(by: >)
    
    for idx in a.indices {
        ans += a[idx]*b[idx]
    }

    return ans
}
