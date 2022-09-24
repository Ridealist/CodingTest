"""
https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""

## 사이트 참고


## 
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) < cacheSize:
                cache.append(city)
                answer += 5
            else:
                cache.popleft()
                cache.append(city)
                answer += 5
    return answer


## 주선님 풀이
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    ## 빈 캐시 생성해주기!
    for _ in range(cacheSize):
        cache.append(None)
    
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        # pop에서 발생하는 오류를 위해 먼저 append한 후 pop하기
        else:
            cache.append(city)
            cache.popleft()
            answer += 5
    return answer

import collections

## 회택 풀이
# class LRUCache:
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.dic = collections.OrderedDict()
#         self.runtime = 0
    
#     def get(self, key):
#         if key not in self.dic:
#             return -1
#         val = self.dic[key]
#         self.dic.move_to_end(key, last=True)
#         self.runtime += 1
#         return val

#     def put(self, key, value):
#         self.dic[key] = value
#         self.runtime += 5
#         self.dic.move_to_end(key)
#         if len(self.dic) > self.max_size:
#             self.dic.move_to_end(last=False)

class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.dic = dict()
    
    def get(self, key:int):
        if key in self.dic:
            value = self.dic.pop(key)
            self.dic[key] = value # pop 이후 다시 입력하면 가장 뒷 순서로 배치
            return value
        else:
            return -1
    
    def put(self, key:int, value:int):
        self.dic[key] = value
        if len(self.dic) > self.max_size:
            self.dic.pop(list(self.dic.keys())[0])


lru = LRUCache(3)

print(lru.get(1))
print(lru.put(1, "서울"))
print(lru.put(2, "대구"))
lru.put(3,"부산")
lru.put(4, "전주")

lru.get(3)
print(lru.dic)
