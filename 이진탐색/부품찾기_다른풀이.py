#### 집합형 자료형 활용

n = int(input())
## 집합형 자료로 저장
n_set = set(map(int, input().split()))
# n_array.sort()

m = int(input())
m_array = list(map(int, input().split()))

def search_part(n_set, m_array):
    for i in m_array:
        if i in n_set:
            print("yes", end=" ")
        else:
            print("no", end=" ")
            
            
#### 계수정렬 활용

n = int(input())
array = [0] * 10000001

# 부품 번호 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

m = int(input())
m_list = list(map(int, input().split()))


for i in m_list:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")