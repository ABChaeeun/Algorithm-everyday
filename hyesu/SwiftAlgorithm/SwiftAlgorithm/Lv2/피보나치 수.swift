//
//  피보나치 수.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/18.
//

func solution(_ n:Int) -> Int {
    var fibo = [0, 1] + [Int](repeating: 0, count: n-1)
    
    for i in 2...n {
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1234567
    }
    
    return fibo[n]
}

print(solution(100))
