#Python 学习手册
> by Gol 2016-08-07  bj 
> 

[TOC]

## Python简介

> * Python是著名的“龟叔”Guido van Rossum在1989年圣诞节期间，为了打发无聊的圣诞节而编写的一个编程语言。
> * 龟叔给Python的定位是“优雅”、“明确”、“简单”，所以Python程序看上去总是简单易懂，初学者学Python，不但入门容易，而且将来深入下去，可以编写那些非常非常复杂的程序。
> 

### 适合开发应用:
＊ 网络应用，包括网站、后台服务
＊ 日常需要的小工具，包括系统管理员需要的脚本任务等等
＊ 把其他语言开发的程序再包装起来，方便使用

### Python的缺点:
＊ 缺点就是运行速度慢，和C程序相比非常慢，因为Python是解释型语言
＊ 代码不能加密, 如果要发布你的Python程序，实际上就是发布源代码

![不能加密缺点](http://www.liaoxuefeng.com/files/attachments/0013868176293326466225daa824587bef6bb39c8683c2c000/0)

## 安装Python
>目前，Python有两个版本，一个是2.x版，一个是3.x版，这两个版本是不兼容的，因为现在Python正在朝着3.x版本进化，在进化过程中，大量的针对2.x版本的代码要修改后才能运行，所以，目前有许多第三方库还暂时无法在3.x上使用。

>为了保证你的程序能用到大量的第三方库，我们的教程仍以2.x版本为基础，确切地说，是2.7版本。请确保你的电脑上安装的Python版本是2.7.x，这样，你才能无痛学习这个教程

### 在Mac上安装Python
系统是OS X 10.8或者最新的10.9 Mavericks，恭喜你，系统自带了Python 2.7, 本学习手册中例子使用mac环境验证通过。

>``python -V``

>Python 2.7.10

###  Python 帮助
> * dir 查看方法  dir(os)
> * help 查看帮助 help(os)

## Hello Python
### 执行方式
* 交互方式
> bogon:sample gaolei$ python 
            >>> print "hello world!" 
            hello world! 
            >>>  

* 文件方式1
> bogon:sample gaolei$ python hellopy.py 
hello python!!

* 文件方式2
> hellopy.py 
\#!/usr/bin/env python
print "hello python!!"
chmod +x hellopy.py 
./hellopy.py 

> 用Python开发程序，完全可以一边在文本编辑器里写代码，一边开一个交互式命令窗口，在写代码的过程中，把部分代码粘到命令行去验证，事半功倍！


### 输入和输出
#### 输出
> * print 'hello, world'    # hello, world
> * print 'The quick brown fox', 'jumps over' # The quick brown fox jumps over
> * print 100 + 200  # 300
> * print '100 + 200 =', 100 + 200 # 100+200=300

#### 输入
>\>\>\>name = raw_input("please input name:")
please input name:gol
\>\>\>name
'gol'

### Python解释器
* **CPython**  使用最广的Python解释器,用C语言开发的 ,作为官方版本的解释器
* IPython 基于CPython之上的一个交互式解释器
* PyPy 采用JIT技术，对Python代码进行动态编译 它的目标是执行速度
* Jython 运行在Java平台上的Python解释器，可以直接把Python代码编译成Java字节码执行。
* IronPython 运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码

### Python基础
> * 采用缩进方式 应该始终坚持使用4个空格的缩进
> * 大小写敏感的，如果写错了大小写，程序会报错


```python
    # print absolute value of an integer:
    a = 100
    if a >= 0:
        print a
    else:
        print -a
```

#### 数据类型和变量
> * 整数 1，100，-8080，0,0xff00，0xa5b4c3d2 ， 10 / 3＝3  ，10 % 3＝1
> * 浮点数  1.23 , 1.23e9   10.0 / 3＝3.3333333333333335
> * 字符串 'I\'m \"OK\"!'
> * 布尔值 True、False两种值 布尔值可以用and、or和not运算。
> * 空值 用None表示
> * 变量 赋值时确定类型 
> * 常量 通常用全部大写的变量名表示常量 PI = 3.14159265359 ，但事实上PI仍然是一个变量

#### 字符串和编码
> * 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
> * 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
>![记事本编辑](http://www.liaoxuefeng.com/files/attachments/001387245992536e2ba28125cf04f5c8985dbc94a02245e000/0)
> * 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器
>![浏览网页](http://www.liaoxuefeng.com/files/attachments/001387245979827634fd6204f9346a1ae6358d9ed051666000/0)
> * 指定编码类型 \# -*- coding: utf-8 -*- 并且文件保存为utf-8类型
> *

* 格式化
  常见的占位符有：

    %d  整数
    %f  浮点数
    %s  字符串
    %x  十六进制整数

举例:
```
    >>> '%2d-%02d' % (3, 1)
    ' 3-01'
    >>> '%.2f' % 3.1415926
    '3.14'
```

####使用list和tuple
* list
list是一种有序的集合，可以随时添加和删除其中的元素。

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
>>> len(classmates)
3
>>> classmates[0]
'Michael'
>>> classmates[1]
'Bob'
>>> classmates[2]
'Tracy'
>>> classmates[-1]
'Tracy'
>>> classmates.append('Gol')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Gol']
>>> classmates.insert(1,'Gol')
>>> classmates
['Michael', 'Gol', 'Bob', 'Tracy', 'Gol']
>>> classmates.pop()
'Gol'
>>> classmates
['Michael', 'Gol', 'Bob', 'Tracy']
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah', 'Bob', 'Tracy']
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
>>> s
['python', 'java', ['asp', 'php'], 'scheme']
>>> L = []
>>> L
[]

```

* tuple

> 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

```python
>>> classmates = ('Michael', 'Bob', 'Tracy')
>>> classmates
('Michael', 'Bob', 'Tracy')
>>> classmates[0] = 'Gol'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> 

```

#### 条件判断和循环
* 条件判断
```python
 age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'
```

```
if x:
    print 'True'
```
只要x是非零数值、非空字符串、非空list等

* 循环
```
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
```

#### 使用dict和set
* dict
```python
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

```

* set
要创建一个set，需要提供一个list作为输入集合
```python
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

```

## 参考资料
> * [http://www.liaoxuefeng.com/](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
> 


