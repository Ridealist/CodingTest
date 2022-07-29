d = {"James": [403], "Azad": [404, 101], "Louis": [404], "Andy": [404], "Guard": [101]}


def prior(r_dict, target):
    d = dict()
    for person, values in r_dict.items():
        l = []
        for value in values:
            if value >= target:
                dist = value - target
            else:
                dist = target - value
            l.append(dist)
        dis_num = min(l)
        d[person] = dis_num
    print(d)


prior(d, 403)
