"""
https://school.programmers.co.kr/learn/courses/30/lessons/92341
"""


def tominute(time: str):
    hour, minute = map(int, time.split(":"))
    return hour*60 + minute

# print(tominute('05:34'))

def duration(records):
    dur_dict = {}
    for rec in records:
        time, num, stat = rec.split(" ")
        if num not in dur_dict:
            dur_dict[num] = 0
        if stat == "IN":
            dur_dict[num] -= tominute(time)
        else:
            dur_dict[num] += tominute(time)
    for key in dur_dict.keys():
        if dur_dict[key] <= 0:
            dur_dict[key] += tominute("23:59")
    return dur_dict

records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees = [180, 5000, 10, 600]

records2 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
fees2 = [120, 0, 60, 591]


records3 = ["00:00 1234 IN"]
fees3 = [1, 461, 1, 10]

print(duration(records3))

def calfee(fees:list, duration:dict):
    base_time, base_fee, per_time, per_fee = fees
    fee_dict = {}
    for car in duration.keys():
        t_minute = duration[car]
        if t_minute <= base_time:
            fee_dict[car] = base_fee
        else:
            if (t_minute - base_time) % per_time == 0:
                t_fee = base_fee + ((t_minute - base_time) // per_time) * per_fee
            else:
                t_fee = base_fee + (((t_minute - base_time) // per_time) + 1) * per_fee
            fee_dict[car] = t_fee
    return fee_dict

def solution(fees, records):
    duration_dict = duration(records)
    fee_dict = calfee(fees, duration_dict)
    
    answer = sorted(fee_dict, key=fee_dict[0])
    return answer


print(calfee(fees2, duration(records2)))


