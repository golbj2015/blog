#!/usr/bin/env python
# -*- coding: utf-8 -*-


names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name


sum = 0
for i in range(10):
	sum+=i 

print "sum:%d" % sum

n = 100
sum2 = 0
while n>0:
	n = n-2
	sum2=sum2+1

print "sum2:%d" %sum2