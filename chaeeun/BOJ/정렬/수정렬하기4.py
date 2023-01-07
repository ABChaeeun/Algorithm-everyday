# merge sort - O(NlogN)

import sys

N = int(sys.stdin.readline().rstrip())
lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))


### divide
# arr에 1개씩 들어있을 때까지 나누고 merge
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    midIdx = len(arr) // 2
    leftArr = arr[:midIdx]
    rightArr = arr[midIdx:]
    leftArr = merge_sort(leftArr)
    rightArr = merge_sort(rightArr)
    return merge(leftArr, rightArr)


### merge
# 분리한 left, right 리스트 중 하나라도 모든 원소들이 비교될때까지 반복하고
  # 각각 첫번째 요소를 비교하며 더 작은 값을 결과 리스트에 저장
# 비교 안된 원소들은 이미 정렬이 된 상황이므로 이어붙여주기
def merge(left, right):
    merged_arr = []
    l = h = 0

    while l < len(left) and h < len(right):
        if (left[l] > right[h]):
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr


merged_lst = merge_sort(lst)
for i in merged_lst:
    print(i)
