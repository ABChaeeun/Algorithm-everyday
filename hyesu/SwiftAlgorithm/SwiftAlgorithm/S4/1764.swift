//
//  1764.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/15.
//

import Foundation

var nums = readLine()!.split(separator: " ").map { Int($0)! }
let n: Int = nums[0]
let m: Int = nums[1]
var listens: [String] = []
var watchs: [String] = []

for _ in 0..<n {
    listens.append(readLine()!)
}

for _ in 0..<m {
    watchs.append(readLine()!)
}

var ans = Array(Set(listens).intersection(Set(watchs)))
print(ans.count)
ans.sort()
print(ans.joined(separator: "\n"))
