"""
https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""

## sol 1
from functools import reduce


def solution(clothes):
    cloth_cnt = {}
    for cloth, cat in clothes:
        if cat in cloth_cnt:
            cloth_cnt[cat] += 1
        else:
            cloth_cnt[cat] = 1
    print(cloth_cnt)

    if len(cloth_cnt) > 1:
        answer = reduce(lambda x, y: x * (y + 1), cloth_cnt.values(), 1) - 1
    else:
        answer = list(cloth_cnt.values())[0]

    return answer


## sol 2
def makedict(clothes):
    result = {}
    for l in clothes:
        if l[1] in result:
            result[l[1]].append(l[0])
        else:
            result[l[1]] = [l[0]]
    print(result)
    return result


def solution(clothes):
    c_dict = makedict(clothes)
    answer = 1
    for v in c_dict.values():
        answer *= len(v) + 1
    return answer - 1


cloth = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]

makedict(cloth)


users = [
    {"mail": "gregorythomas@gmail.com", "name": "Brett Holland", "sex": "M", "age": 73},
    {
        "mail": "hintoncynthia@hotmail.com",
        "name": "Madison Martinez",
        "sex": "F",
        "age": 29,
    },
    {"mail": "wwagner@gmail.com", "name": "Michael Jenkins", "sex": "M", "age": 51},
    {"mail": "daniel79@gmail.com", "name": "Karen Rodriguez", "sex": "F", "age": 32},
    {"mail": "ujackson@gmail.com", "name": "Amber Rhodes", "sex": "F", "age": 42},
]

from functools import reduce

# 나이 더하기
print(reduce(lambda x, y: x + y["age"], users, 0))

# 이메일 목록 만들기
print(reduce(lambda x, y: x + [y["mail"]], users, []))

# 성별로 분류
def names_by_sex(acc, cur):
    sex = cur["sex"]
    if sex not in acc:
        acc[sex] = [cur["name"]]
    else:
        acc[sex].append(cur["name"])
    return acc


print(reduce(names_by_sex, users, {}))
print(reduce(names_by_sex, users))

"""
이런 현상이 발생하는 이유는 reduce() 함수에 초기값을 넘기지 않으면 두번째 인자로 넘어온 list나 tuple의 첫번째 값이 초기값으로 사용되기 때문입니다. 본 예제에서 사용하고 있는 실습 데이터는 첫번째 값이 유저 정보를 담고 있는 dictionary이므로 이 값에 숫자를 더하거나, 키를 추가하려고 하니 문제가 발생하는 것입니다.
"""
