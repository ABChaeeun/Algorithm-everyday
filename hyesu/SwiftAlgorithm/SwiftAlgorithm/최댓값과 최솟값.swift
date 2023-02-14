//
//  최댓값과 최솟값.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/14.
//

import Foundation

func solution(_ s:String) -> String {
    let data = s.components(separatedBy: " ").map{Int($0)!}
    return String(data.min()!) + " " + String(data.max()!)
}
