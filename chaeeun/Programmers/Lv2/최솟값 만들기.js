function solution(A,B){
    var answer = 0;
    // ver1
//     var tmp = [];

//     while (A.length > 0) {
//         let A_index = A.indexOf(Math.min(...A));
//         let B_index = B.indexOf(Math.min(...B));

//         // console.log(B[B_index])
//         answer += A[A_index] * B[B_index]

//         console.log(A, B);
//         console.log(A[A_index], '*', B[B_index])
//         A.splice(A_index, 1);
//         B.splice(B_index, 1);
//         console.log(A, B);
//         console.log();    
//     }
//     tmp.push(answer)
    
    // ver1-2 -> 시간초과
//     while (A.length > 0) {
//         let A_index = A.indexOf(Math.min(...A));
//         let B_index = B.indexOf(Math.max(...B));

//         answer += A[A_index] * B[B_index]
//         A.splice(A_index, 1);
//         B.splice(B_index, 1);
//     }
    
    // ver1-3
    
    // A.sort() // 오름차순 정렬
    // B.sort().reverse() // 내림차순 정렬
    // for (let i=0; i<A.length; i++) {
    //     answer += A[i] * B[i]
    // }
    
    // ver1-4
      A = A.sort((a,b) => a-b) // 오름차순 정렬
      B = B.sort((a,b) => b-a) // 내림차순 정렬
      for (let i=0; i<A.length; i++) {
          answer += A[i] * B[i]
      }
  
    
    
    // ver2
    // console.log(B)
    
    // var arr = []
    // for (let i=0; i<B.length; i++) {
    //     B.push(B.shift())
    //     // console.log(B)
    //     var tmp = 0
    //     for (let j=0; j<A.length; j++) {
    //         tmp += A[j] * B[j]
    //     }
    //     arr.push(tmp)
    // }
    // console.log(arr)
    // answer = Math.min(...arr)
    return answer;
}
