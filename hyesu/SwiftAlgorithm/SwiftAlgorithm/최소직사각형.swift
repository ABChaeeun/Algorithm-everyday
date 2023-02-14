//
//  최소직사각형.swift
//  SwiftAlgorithm
//
//  Created by 김혜수 on 2023/02/14.
//

import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    let small = sizes.map { $0[0] > $0[1] ? $0[1] : $0[0] }
    let big = sizes.map { $0[0] < $0[1] ? $0[1] : $0[0] }
    return big.max()! * small.max()!
}
