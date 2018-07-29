#!/usr/bin/env python
# coding=utf-8

# a = 12
# print id(a)

# a = 2
# b = 2
# print id(a) 
# print id(b) 

# b = type(1)
# print type(id(b))
# b = NULL
# print b

# print type(None)

# a = ''
# if a :
#     print '1'
# else:
#     print '2'

# 比较的过程: 值 身份 类型

# a = 60
# b = 200
# print a is b
# print type(a) == type(a)
# print a < b

# a = []
# print isinstance(a, list)
 
# a = 100
# print isinstance(a, type(100))

# abs 求绝对值
# divmod 返回一个元组，同时保存商与余数

# a = 10
# b = 3 
# r1, r2 = divmod(a, b)
# print r1, r2
# r1 = a / b
# r2 = a % b

# round 对浮点数进行四舍五入
# pi = 3.1415926
# print round(pi, 2)

# import math
# print round(math.pi, 4)

# oct hex 进制转换

# 条件和循环
# smaller = x if x < y else y 类似于三目运算符

# def Hello():
#     print 'hehe'
# 
# Hello()

# def Func1():
#     def Func2():
#         print "hehe"
#     return Func2
# 
# ret = Func1()
# Func1()
# ret()

# def Hello(x):
#     print x
# 
# Hello("wogan")
# Hello(100)
# Hello({'a' : 1, 'b' : 2})

# def Add(x, y):
#     return x + y
# 
# print (10 + 5)
# print ("wo" + "ri")

# def Hello(x = 10):
#     print x
# 
# Hello(1)
# Hello("wonong")

# def PrintPoint(x = 0, y = 0, z = 0):
#     print x, y, z
 
# PrintPoint()
# PrintPoint(10)
# PrintPoint(10, 20)
# PrintPoint(10, 20, 30)

# 关键字参数
# PrintPoint(x = 10, z = 20)

# arr = [9, 5, 2, 7]
# print arr
# print sorted(arr, reverse = True)
# print sorted(arr)

# def Cmp(x, y):
#     if abs(x) < abs (y):
#         return -1
#     elif abs(x) > abs(y):
#         return 1
#     else:
#         return 0
# 
# a = [-9, 5, 2 ,7]
# print sorted(a, cmp = Cmp)

# CRITICL
# ERROR
# WARNING
# INFO
# NOTICE

# def Log(prefix, *data): # * 代表 data 为一个元组(参数组)
 
#     print prefix + '\t'.join(data)
# Log("[Notice]\t","id = 10", "name = tz", "score = 10")

# ** 代表字典
# def Log(prefix, **data):
#     print prefix + '\t'.join(data.values())
# 
# Log("[Notice]\t",id = "10", name = "tz", score = "10")

# def Func():
#     print '1'
# 
# def Func():
#     print '2'
# 
# Func()



















