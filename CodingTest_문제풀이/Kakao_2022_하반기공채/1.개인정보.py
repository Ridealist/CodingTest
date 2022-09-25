def transdate(date, month):
    dl = list(map(int, date.split(".")))
    y, m, d = dl
    m += month
    d -= 1

    if d == 0:
        m -= 1
        d = 28

    while m > 12:
        m -= 12
        y += 1
    
    return [y, m ,d]


def caldate(terms, privacies):
    result = []
    t_dict = {}
    for term in terms:
        l = term.split(" ")
        t_dict[l[0]] = int(l[1])
    
    for priv in privacies:
        p = priv.split(" ")
        l = transdate(p[0], t_dict[p[1]])
        result.append(l)
    
    return result

def isexpire(today, priv):
    if today[0] > priv[0]:
        return False
    elif today[0] < priv[0]:
        return True
    else:
        if today[1] > priv[1]:
            return False
        elif today[1] < priv[1]:
            return True
        else:
            if today[2] > priv[2]:
                return False
            else:
                return True


def solution(today, terms, privacies):
    
    trans_today = list(map(int, today.split(".")))
    trans_priv = caldate(terms, privacies)
    # print(trans_today)
    # print(trans_priv)

    result = []

    for i, priv in enumerate(trans_priv):
        if not isexpire(trans_today, priv):
            result.append(i+1)
        
    return result