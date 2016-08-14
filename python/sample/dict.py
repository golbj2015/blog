#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#查看所有的key
print tuple(d.keys())

# update 
d['Adam'] = 67

#判断key是否存在
print 'Thomas' in d        # False
print d.get('Thomas', -1)  # -1

#删除一个key
print d.pop('Bob')         # 75
 
#遍历
for k in d:
	print k,d[k]
