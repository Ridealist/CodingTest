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


### 회택풀이
from datetime import datetime, timedelta
from math import ceil
from collections import defaultdict

def solution(fees, records):
    temp_data = defaultdict(list)
    time_records = {}

    end_time = "23:59"

    for record in records:
        time, car_num, in_out = record.split()
        if in_out == "IN":
            temp_data[car_num].append(time)
        else:
            in_time = temp_data[car_num].pop()
            time_records[car_num] = time_records.get(car_num, 0) + get_time_difference(in_time, time)

    for car_num in temp_data.keys():
        if temp_data[car_num]:
            in_time = temp_data[car_num].pop()
            time_records[car_num] = time_records.get(car_num, 0) + get_time_difference(in_time, end_time)

    return [(get_cost(time_records[t], fees)) for t in sorted(time_records)]

def get_time_difference(t1, t2):
    FMT = '%H:%M'
    tdelta = datetime.strptime(t2, FMT) - datetime.strptime(t1, FMT)
    return int(tdelta / timedelta(minutes=1))

def get_cost(time, fees):
    def_time, def_cost, per_time, per_cost = fees
    if time > def_time:
        return def_cost + ((time - def_time - 1) // per_time + 1) * per_cost
    else:
        return def_cost


### 홍동 풀이
function solution(fees, records) {
    const [default_time, default_pay, unit_time, unit_pay] = fees
    const map = new Map()
    records.forEach((item) => {
        let [time, num, type] = item.split(" ")
        const [hour, minute] = time.split(":")
        time = Number(hour) * 60 + Number(minute)
        const recode = map.get(num) || []
        map.set(num, [...recode, time])
    })
    const result = []
    for([key, value] of map) {
        result.push([key, value])
    }
    result.sort((a, b) => a[0] - b[0])
    return result.flatMap(([_, recode]) => {
        if(recode.length % 2 === 1) recode.push(23 * 60 + 59)
        const use_time = []
        while(recode.length !== 0) {
            const a = recode.pop()
            const b = recode.pop()
            const time = a - b
            use_time.push(time)
        }
        const cum_time = use_time.reduce((a ,b) => a + b) - default_time
        if(cum_time <= 0) {
            return default_pay
        } else {
            return Math.ceil(cum_time / unit_time) * unit_pay + default_pay
        }
    })
}