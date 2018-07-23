# coding=utf-8
# 人生苦短，我用Python

# 引用
# 这里的变量 a b c 等类似于标签

# a = 10
# b = a
# x = 10
# print id(a), id(b), id(10), id(x)
# b = 20
# print id(b)

# if 语句
# 如:  if expression:
#           do_something1
#      else: 
#           do_something2

# 如:  if expression:
#           do_something1
#      elif: 
#           do_something2
#      else: 
#           do_something3

# a = 10
# b = 5
# if a > b:
#     print a
# else:
#     print b

# while 循环
# 如: while expression:
#         do_something  

# counter = 0
# while counter < 3:
#     print 'loop %d' % counter
#     counter += 1
    
# for 循环
# 如: for c in a:
#           do_something
# for i in range(a, b):
#       do_something

# mystr = 'abcd'
# for c in mystr:
#     print c

# num = [1, 2, 3, 4]
# for i in num:
#     print i

# a = {
#      'key1':'value1', 
#      'key2':'value2',
#      'key3':'value3'
# }
# for key in a:
#     print key, a[key]

# for i in range(0, 10): # 前闭后开
#     print i

# break 和 continue
# for num in range(1, 100): # for 内部定义的变量
#      if num % 3 == 0:     #     在循环外也可以访问
#         break
# print num

# 找 1-99 中所有 3 的倍数
# for i in range(1, 100):
#     if i % 3 != 0:
#         continue
#         print i

# 空语句 pass 类似于 ;
# x = 10
# if x % 2 != 0:
#     pass
# else:
#     print 'x is prime'

# 列表解析
# a = []
# for x in range(0, 4):
#     a.append(x ** 2)
# print a

# a = [x ** 2 for x in range(1, 100) if x % 2 == 1]
# print a

# a = [x for x in range(1900, 2000) if x % 400 == 0 or x % 4 == 0 and x % 100 != 0]
# print a

# 函数 
# 如: def Add(x, y)
#         return x + y

# def Add(x, y):
#     return x + y
 
# a = int (raw_input())
# b = int (raw_input())
# c = Add(int (a), int (b))
# print c

# def Func():
#     print 'aaa'
# 
# def Func(x):
#     print x
# 
# a = 'a'
# Func(a)

# Python 不支持重载
# 如果定义了同名的函数，无论参数列表如何，后定义的函数会覆盖前面的

# def Func():
#     print "nihao!"
# print type(Func)

# def Func(debug = True):
#     if debug:
#         print 'in debug'
#     else:
#         print True
# Func()
# Func(False)

# def GetPoint(): # type tupel 元组
#     x = 1
#     y = 20
#     return x, y
# print type(GetPoint)
# a, b = GetPoint()
# print a, b
# 
# _, b = GetPoint()
# print b

# 文件操作

# 文件对象可以使用 for 循环遍历
# 凡是能够用 for 遍历的对象，称作可迭代对象
# f = open('test.txt', 'r')
# for line in f:
#     print line[:-1]
# f.close()

# 字典的键值对: 键对应单词，值对应单词出现的次数
# f = open('test.txt', 'r')

# f = raw_input()
# data = {}
# for word in f:
#     if word in data:
#         data[word] += 1
#     else:
#         data[word] = 1
# print data

# 导入
# 会生成一个 *.pyc 文件
# import add
# print add.Add(10, 30)

# 查找 import 由这个顺序来查找 优先查找当前目录
# import sys
# print sys.path 

# import string
# a = string.atoi("1234567")
# b = str.count('o')
# print b
# str = 'hello world!'
# print str[::-1]
# tmp = "hello".join("world!")
# print tmp

# print "*************************************"
# print "****1.game                2. exit****"
# print "*************************************"
# input = raw_input("#")
# if input == '1':
#     print "game"
# else:
#     exit(0)
# print 'haha'

# import time
# 
# i = 0
# while 1:
#     print range(0, 10)
#     time.sleep(1)
#     i += 1
#     if i >= 10:
#         break

# 访问函数的文档字符串
# def Add(x, y):
#     '文档字符串'
#     return x + y
# ret = Add(1, 2)
# print Add.__doc__
# print ret
# help(Add)







