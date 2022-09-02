# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

import random
array = [random.randint(0, 10**5) for _ in range(10**7)]

from time import time


array = [random.randint(0, 10**5) for _ in range(10**7)]
start_time = time()
array.sort()
print("정렬완료!")
print("built-in 정렬 소요시간: ", time() - start_time)


start_time = time()
count = [0] * (max(array)+1)
for i in array:
    count[i] += 1
#print(count)
answer = []
for idx, val in enumerate(count):
    answer.extend([idx]*val)
print("정렬완료!")
print("계수정렬 소요시간: ", time() - start_time)

