# 캐시


```python
class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.dic = collections.OrderedDict()

    def get(self, key):
        if key not in self.dic:
            return -1
        val = self.dic[key]
        self.dic.move_to_end(key, last=True)
        return val

    def put(self, key, value):
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic) > self.max_size:
            self.dic.popitem(last=False)
```


```python
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

### 출력
lru = LRUCache(3)

print(lru.get(1))
print(lru.put(1, "서울"))
print(lru.put(2, "대구"))
lru.put(3,"부산")
lru.put(4, "전주")
lru.get(3)
print(lru.dic)

###
-1
None
None
{2: '대구', 4: '전주', 3: '부산'}
```