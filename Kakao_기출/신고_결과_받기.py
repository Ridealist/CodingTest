"""https://programmers.co.kr/learn/courses/30/lessons/92334"""


def solution(id_list, report, k):
    blame_pair = {[]: x for x in id_list}
    blame_count = {0: x for x in id_list}

    report = set(report)
    for r in report:
        blame_count[r.split(" ")[1]] += 1
        blame_pair[r.split(" ")[0]].append(r.split(" ")[1])

    answer = []
    for id in id_list:
        cnt = 0
        for name in blame_pair[id]:
            if blame_count[name] >= k:
                cnt += 1
        answer.append(cnt)

    return answer


def solution(id_list, report, k):

    answer = [0] * len(id_list)
    blame_cnt = {x: 0 for x in id_list}

    report = set(report)

    for r in report:
        blame_cnt[r.spilt(" ")[1]] += 1

    for r in report:
        if blame_cnt[r.split(" ")[1]] >= k:
            answer[id_list.index(r.split(" ")[0])] += 1

    return answer


def solution(id_list, report, k):
    report = set(report)

    blame_cnt_set = {}
    report_set = {}
    for r in report:
        rep_l = r.split(" ")
        er = rep_l[0]
        ed = rep_l[1]
        try:
            blame_cnt_set[ed] += 1
        except:
            blame_cnt_set[ed] = 1
        try:
            report_set[er].append(ed)
        except:
            report_set[er] = [ed]

    answer = []
    for id in id_list:
        cnt = 0
        try:
            for rep in report_set[id]:
                if blame_cnt_set[rep] >= k:
                    cnt += 1
        except:
            cnt = 0
        answer.append(cnt)

    # print(blame_cnt_set)
    # print(report_set)

    return answer
