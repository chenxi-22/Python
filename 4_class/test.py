#!/usr/bin/env python
# coding=utf-8

# 人生苦短, 我用Python

# 文件操作
# 垃圾回收, 能够自动回收, 关闭

# print f.__doc__

# f = open("test.txt", 'w | a')

# 每次读一行
# for line in f:
#         print line,

# 一次全部读出来
# lines = f.readlines()
# for line in lines:
#         print line,

# f.write("wogan")
# f.write("wogan")

# f.writelines(['aaa\n', 'afdsaf\n', 'ccc\n'])
# f.writelines(['aaa\n', 'afdsaf\n', 'ccc\n'])
 
# f.close()
# print type(f)

# with 语句和上下文语句

# with open("./test.txt") as f:
#     print f.readlines()

# 文件系统相关操作
# import os.path

# my_path = '/home/kaka/class/Python/class/4_class/test.txt'
 
# print os.path.basename(my_path)
# print os.path.dirname(my_path)
# print os.path.split(my_path)
# print os.path.splitext(my_path)

# import os
# import os.path
# 
# my_path = '/home/kaka/Class'
# for basedir, dirnames, filenames in os.walk(my_path):
#     for filename in filenames:
#         print os.path.join(basedir, filename)

# import os
# import sys
# if len(sys.argv) < 2: 
#     path = '.'
# else:
#     path = sys.argv[1]
# for f in os.listdir(path):
#     print f,

# print 'hello'
# a = [1,2 ,3]
# print a[100]

# 异常处理
# try:
#     a = [1, 2, 3]
#     print a[100]
# except IndexError as e:
#     print type(e)
#     pass
#     print 'hehe'
#     pass 忽略
#     print e

# except 语句需要知道当前处理的异常是哪种类型
# 变量名 e 表示前面抛出异常对象的引用

# try:
#     a = [1, 2, 3]
#     print a[100]
# except Exception as e:
#     print e
#     print type(e)
# print 'hehe'

# try:
#     a = [1, 2, 3]
#     print a[100]
# except Exception as e:
#     print e
#     print type(e)
# finally:
#     print 'wogan' 无论异常是否触发, 都会执行到该逻辑

# 抛出异常
# raise
# def Divede(x, y):
#     if y == 0:
#         return 0, False
#     return x / y, True

# def Divede(x, y):
#     if y == 0:
#         raise Exception('Divide Zero')
#     return x / y
# a = Divede(10, 0)

# while True:
#     print 'hehe'





