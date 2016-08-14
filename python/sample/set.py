#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = set('spam')  
y = set(['h','a','m'])  

# 交集 
print x & y 

#并集
print  x | y

# 差集 
print x-y

#转list
print [i for i in y]
