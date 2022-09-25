Array 단독 보다는
- 백트레킹
- 다이나믹 프로그래밍
과 연결되는 부분 많음 - 난이도 up


0. Index Approach


Array는 Random Access를 지원하는 Data Structure
-> 인덱스를 통해 데이터에 바로 접근 가능


1. Sorting - Array의 기본은


Time Complexity = O(NlogN)

- stable : merge sort
- unstable : quick sort, heap sort

python 기본 sorting은 stable sort

- sort() 메소드는 list에서만 정의
- sorted() 함수는 모든 iterable 사용 가능

```python
>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]

>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
```

2. Searching
- 기본 search - O(N)
- sorted array면, binary search 사용 가능 - O(logN)



3. Binary Search
```python
from typing import List

def search(nums: List[int], target: int):
    left = 0
    right = len(nums)-1

    while left <= right:
        pivot = (left + right)//2
        if nums[pivot] == target:
            print("찾았다!")
            return pivot
        if nums[pivot] > target:
            print("못찾았다. 오른쪽 바운더리 이동")
            right = pivot - 1
        else:
            print("못찾았다. 왼쪽 바운더리 이동")
            left = pivot + 1
    return -1
```

4. Move Zeroes
https://leetcode.com/problems/move-zeroes/

- Array의 기본은 Index를 사용하는 것!
    - Index를 두개 사용하기
    - 2 pointer
- Move Zeroes지만 0이 아닌 숫자를 옮겨라
- 숫자 Copy 후 나머지는 0 오버라이팅 관점

```python
## Swap 관점
from typing import List
def moveZeroes(nums: List[int]):
    zero = 0
    for num in range(len(nums)):
        if nums[num] != 0:
            nums[num], nums[zero] = nums[zero], nums[num]
            zero += 1

## Copy 관점
def moveZeroes(nums: List[int]):
    zero = 0
    for num in range(len(nums)):
        if nums[num] != 0:
            nums[zero] = nums[num]
            zero += 1
    for z in range(zero, len(nums)):
        nums[z] = 0
```

## 투포인터
https://butter-shower.tistory.com/226
```python
n = 5 # 데이터 갯수
m = 5 # 부분합 M
# data = List[int]
data = [1,2,3,4,5]

cnt = 0 # 부분합이 M이 되는 갯수
subs = data[0] # 중간중간 구간합
end = 0

for start in range(n):
    # s = sum(data[start:end+1]) # sum() -> O(k) iterable 돌면서 sum variable에 합치는 것
    while subs < m and end < n:
        print(f"아직... 부분합: {subs}, start={start}, end={end}")
        end += 1
        subs += data[end]
    if subs == m:
        print(f"찾았다, start={start}, end={end}")
        cnt += 1
    subs -= data[start]

print(cnt)
```

5. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/

### Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

- Sliding Window
    - https://youtu.be/uH9VJRIpIDY
    - 이전 결과를 써먹어서 Time Complexity를 줄이는 방법
    - Brute Force O(N**2) or O(N*K) / 슬라이딩으로 O(N) 효율화 가능!
    - 모든 숫자가 양수일때 활용가능
        - 전제조건 잘보기...
    - 주요 유형 : https://itchallenger.tistory.com/178
        - 구간 합
        - Anagram

```python
def pivotIndex(nums: List[int]):
    s = sum(nums)
    lefts = 0
    rights = s
    pastpivotnum = 0

    for i in range(len(nums)-1):
        num = nums[i]
        rights -= num
        lefts += pastpivotnum
        if lefts == rights:
            return i
        pastpivot = num
    return -1
```

6. Sort Colors (Dutch flag problem)
https://leetcode.com/problems/sort-colors/

- 기본 sorting algorithm은 O(NlogN)
    - 어떻게 O(N)으로? / 계수 정렬!
        - in-place swap으로 어떻게?

- 0,1,2로 이루어진 Array / O(N) 시간복잡도 / in-place swap을 통해 정렬하기
- quicksort의 아이디어 적용

**quicksort의 핵심 요소**
- pivot
- partitioning

```python
def sortColors(nums=List[int]):
    idx0 = 0
    idx2 = len(nums)-1
    p = 0

    while p <= idx2:
        if nums[p] == 0:
            nums[idx0], nums[p] = nums[p], nums[idx0]
            idx0 += 1
            p += 1
        elif nums[p] == 2:
            nums[idx2], nums[p] = nums[p], nums[idx2]
            idx2 -= 1
        else: ## nums[p] == 1일때
            p += 1
            ## 조건별로 pointer를 움직이지 않게 하면 코드 중복을 막을 수 있따!!!
            # if nums[p] == 0:
            #     nums[idx0], nums[p] = nums[p], nums[idx0]
            #     idx0 += 1
        # p += 1
    return nums
```