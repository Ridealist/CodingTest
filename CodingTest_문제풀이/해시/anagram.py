"""
- 이론 설명 -
https://shoark7.github.io/programming/algorithm/several-ways-to-solve-anagram-in-python
"""
"""
- 문제 -
https://velog.io/@jiffydev/algo-40
"""


## 1. 정렬 알고리즘

a = input()
b = input()

if sorted(a) == sorted(b):
    print("YES")
else:
    print("NO")

# 시간복잡도 O(NlogN)

#############################

## 2. 글자수 세기

### 2-1. 리스트 자료구조 이용

# 카운터 리스트 만들기

from string import ascii_lowercase as LOWERS

def char_to_index(c):
    if c not in LOWERS or len(c) != 1:
        raise ValueError("Only lower alphabet characters are allowed")
    return ord(c) - ord("a")

def are_anagrams(a, b):
    
    counter = [0] * len(LOWERS)
    
    for i in a:
        idx = char_to_index(i)
        counter[idx] += 1
    
    for j in b:
        idx = char_to_index(j)
        counter[idx] -= 1
    
    return all(n==0 for n in counter)

## 하지만 입력이 정해져있을 때만(입력 가능한 범위가 제한적일 때)
## 사용할 수 있다는 한계점!!!

### 2-2. 딕셔너리 자료 구조 이용

def are_anagram(a, b):
    
    counter = dict()
    
    for c in a:
        counter[c] = counter.get(c, 0) + 1
    
    for c in b:
        counter[c] = counter.get(c, 0) - 1

    return all(counter[i] == 0 for i in counter)

## 공간복잡도 최악에 O(N)

### 2-3. Counter 사용하기

"""
Counter는 collections 내장 모듈에 구현되어 있는 자료구조로,
그 이름에 걸맞게 원소의 빈도수를 세는 데 그 목적이 있다.

>>> from collections import Counter
>>> issubclass(Counter, dict)
True
"""

from collections import Counter

def are_anagram(a, b):
    return Counter(a) == Counter(b)

### 처음부터 끝까지 단어를 세는 작업 -> 시간복잡도: O(N)
### 공간복잡도 -> 최악의 경우 2*O(N)

"""
dictionary.get(keyname, value)

keyname = required.
value = optional. A value to return if the specified key does not exist.
        Default if "None"
"""

"""
딕셔너리가 같을 때
- dic1 == dic2
- dic1 - dic2 == 0
두가지 방법 모두 가능
"""


a = input()
b = input()

# 공간복잡도 good!
dic = dict()

for i in a:
    dic[i] = dic.get(i, 0) + 1

for j in b:
    dic[j] = dic.get(j, 0) - 1

# dict를 그냥 for문 돌리면 key값을 기준으로 돌아감
for i in dic:
    # dic.get(i) != 0
    if dic[i] != 0:
        print("NO")
        break

print("YES")