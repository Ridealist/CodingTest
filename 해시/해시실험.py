from time import time

num_list = [i for i in range(1, 10 ** 7)]
num_set = set(i for i in range(1, 10 ** 7))

target = 5000000

start_time = time()
if target in num_list:
    print("List에서 찾았다!", end=" ")
    total_time = time() - start_time
    print("List 찾기 걸린시간: {:.25f}".format(total_time))

start_time = time()
if target in num_set:
    print("Set에서 찾았다!", end=" ")
    total_time = time() - start_time
    print("Set 찾기 걸린시간: {:.25f}".format(total_time))