#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 计算平均数值
def getAverage(d):
    total = len(d)
    sumValue = 0
    if total == 0:
        return 0

    for k in d:
        sumValue+=d[k]

    return sumValue/total

print "average :%-06.2f"% getAverage(d)

#计算最大 最小数值
def getMaxMin(d):
    max = 0
    min = 0
    for k in d:
        print k

    for k in d:
        #init min value
        if min == 0 :
            min = int(d[k])

        # cal max value
        if max<int(d[k]):
            max = int(d[k])
        #cal min value
        if min>int(d[k]):
            min = int(d[k])
    return max,min


print "max:%d,min:%d" % getMaxMin(d),
