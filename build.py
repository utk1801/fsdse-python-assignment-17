import operator


def solution_asc(dic):
    ascDic = sorted(dic.items(),key = operator.itemgetter(0))
    print ascDic
    return ascDic


def solution_desc(dic):
    dscDic = sorted(dic.items(),key = operator.itemgetter(0),reverse = True)
    print dscDic
    return dscDic

solution_asc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
solution_desc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
