#!/usr/bin/env python
# coding=utf-8

# 人生苦短，我用Python

# a = [1,2,3]
# b = [1,2,3]
# print id(a),id(b)

# 序列跟顺序相关
# a = [1, 2, 3, 4, 5, 6]
# b = ['a', 'b', 'c', 'd', 'e', 6]
# print 8 in a

# a = [1, 2, 3, 4, 5, 6]
# b = ['a', 'b', 'c', 'd', 'e', 6]
# a = a + b
# print a 

# a = [1, 2, 3, 4, 5, 6]
# print a * 4
# b = ['a', 'b', 'c', 'd', 'e']
# print b * 4

# a = [1, 2, 3, 4, 5, 6]
# print a[-4:]
# print a[1:5]
# print a[:1]
# print a[::2] # 确定每次遍历下标加多少
# print a[0:-1]

# b = a[::-1] # 字符串逆置
# print b

# max min 
# a = [3,123,3124,123,333,12,1]
# b = sorted(a)
# print b

# enumerate
# def Find(input_list, x):
#     for i, item in enumerate(input_list):
#         if item == x:
#             return i
#     return None
# 
# a = [3,123,3124,123,333,12,1]
# print Find(a, 12)

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]
# c = zip(x, y, z)

# key = ('name', 'id', 'score')
# value = ('tangzhong', '1000', '5000')
# dit = {(zip(key, value))}
# print dit

# a = ['n', 'h', 'a']
# a[0] = x
# print a

# x, y = 10, 20
# print 'x = %d, y = %d\n' % (x, y)

# 加上 r 前缀就不会转义

# a = 1
# print str(a), repr(a)
# print type(repr(a))

# a = 'hehe' 
# print str(a), repr(a)

# a = ['aa', 'bb', 'cc']
# print ' '.join(a)

# a = 'aa bb cc'
# print a.split()

# 判断字符串是否以某个特定子串开头或结尾
# a = "hello world"
# print a.startswith('he')
# print a.endswith('ld')

# 去除字符串开头和结尾的空白符(回车，换行，空格，制表符t)
# a = '              haha    wogan    \n'
# print a.strip()

# 字符串居中、左对齐、右对齐
# a = 'hehe'
# print a.center(333)

# 查找子串
# a = 'hello world'
# print a.find('world')

# 字符串替换
# a = 'hello world hehe'
# print a.replace(' ', '%20')

# 判断字符串是否是纯数字 / 纯字母
# a = 'hell'
# print a.isalpha()
# a = '1234'
# print a.isdigit()

# 字符串转换大小写
# a = 'Hello World'
# print a.upper()
# print a.lower()

# 列表的常用操作
# a = [1, 2, 3, 2, 2]
# a.append(3)
# print a
# a.remove(2)
# print a
# del(a[0])
# print a

# a = [1, 2, 3, 2, 2]
# a.extend([3, 4])
# print a

# a = [1, 2]
# a.reverse()
# print a[::-1]
# print a

# 栈操作
# a = []
# a.append(1)
# print a[-1]
# a.pop()

# 队列操作
# a = []
# a.append(1)
# print a[0]
# a.pop(0)

# a = 1
# b = 1
# print id(a), id(b)
# b = 2
# print id(a), id(b)

# a = ([1,2], [3,4])
# print id(a[0][0])
# a[0][0] = 10
# print id(a[0][0])
# print a

# 字符串哈希算法:MD5 

# print hash()

# a = {
#     'a' : 1,
#     'b' : 2,
#     'b' : 3,
# }
# print a.keys()
# print a.items()






















