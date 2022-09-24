# 캐시

## 캐시가 사용되는 경우

### 1. 웹 서비스
- 데이터를 저장소에서 꺼내올 때 많은 부하(시간+돈) 소요
- 캐시 서버를 두어서 요청이 메인 서버로 몰리지 않도록 처리
    - 자주 요청하는 데이터는 캐시 서버에서 바로 전달
    - 캐시 서버 없는 것만 메인 서버에서

### 2. CPU
- 데이터 읽을 때 L1, L2, L3 cache에 저장된 데이터 유무 확인
    - 없는 경우에만 Memory나 Disk에 접근
    - 가져온 데이터는 다시 캐시에 넣어둠

### 3. DB
- DB에 데이터 요청 들어오면 버퍼 캐시(임시저장소 역할)에서 요청 데이터 있는지 확인
- 버퍼 캐시에 없으면 디스크에서 찾음
    - 대부분은 버퍼 캐시에서 해결

### 4. Redis
- DB 버퍼 캐시로 해결이 되지 않을 때 외부 캐시 서버로 활용
    - DB 내부 버퍼 캐시를 확장해 외부에 두는 것
    - key-value 형태로 데이터 저장
    - 그 자체로 NoSQl DBMS(비 관계형 데이터 베이스 관리 시스템)

## LRU Cache
- LRU(Last Recently Used) 캐시 데이터 저장 및 수정 알고리즘 중 하나
- 제한된 용량의 cache에 데이터 올리고, 용량이 다 차면 가장 오랬동안 사용하지 않은 값부터 버림
- DB 버퍼 캐시, redis도 이 방식 지원
- FIFO보다 효율적


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
- Ordered Dict 활용
    - OrderedDict.move_to_end(key=, last=) 메소드
    - OrderedDict.popitem(last=) 메소드


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
            self.dic.pop(list(self.dic.keys())[0]) # 가장 먼저 나온 (쓴 지 오래된) 값을 지우기

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

- __python 3.7 버젼 이후부턴 dictionary가 입력 순서를 보장__
- 일반 dict 사용해도 OrderedDict처럼 활용 가능!

<br>

---


### 참조 사이트
- https://moons08.github.io/programming/cache_LRU/

### 상세 설명?
- https://www.interviewcake.com/concept/java/lru-cache

### 다른 방법?
- https://moons08.github.io/programming/OS_virtual_memory/#page-replacement-algorithms