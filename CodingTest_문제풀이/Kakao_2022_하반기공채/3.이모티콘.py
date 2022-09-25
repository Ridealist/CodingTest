from itertools import product

from functools import reduce

def solution(users, emoticons):
    
    discount = [40, 30, 20, 10]
    
    for emo in emoticons:
        product([emo], discount)
    


def makepair(emoticons):
    discount = [40, 30, 20, 10]
    d = {}
    for idx, emo in enumerate(emoticons):
        d[idx] = list(product([emo], discount))

    l = []
    for i in range(len(emoticons)):
        l.append(d[i])
        
    return list(product(*l))

    
print(makepair([7000, 9000]))
    

users = [[40, 10000], [25, 10000]]
emoticons_1 = [7000]
emoticons_2 = [9000]
discount = [40, 30, 20, 10]

# l = [[(0, 0)]*len(emoticons) for _ in range(len(emoticons) * 4)]


# from itertools import product

# discount = [40, 30, 20, 10]

# for emo in emoticons:
    


l1 = list(product(emoticons_1, discount))
l2 = list(product(emoticons_2, discount))

l = list(product(l1, l2))

result = []
for pair in l:
    plus = 0
    total = 0
    # for i in range(len(emoticon)):
        
    # p1,dc1 = pair[0]
    # p2,dc2 = pair[1]
    # plus = 0
    # total = 0
    for user in users:
        s = 0
        dcrate = user[0]
        money = user[1]
        for pairs in l:
            for i in range(len(emoticon)):
                if pairs[i][0] >= dcrate:
                    s += pairs[i][1] * (100-pairs[i][0]) // 100
            if s >= money:
                plus += 1
            if s < money:
                total += s
        # print(p1,dc1, p2, dc2)
        # print(s)
    # print(pair)
    # print([plus, total])
    result.append([plus, total])

# print(result)

result.sort(reverse=True)


print(result)
