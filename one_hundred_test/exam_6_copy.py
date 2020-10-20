# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/20 14:48'
__author__ = 'Philgent'
"""
将一个列表的数据复制到另一个列表中。
使用列表[:]，拿不准可以调用copy模块。
"""
import copy
a = [1, 2, 3, 4, ['a', 'b']]

b = a  #赋值
c = a[:]  #浅拷贝
d = copy.copy(a) #浅拷贝
e = copy.deepcopy(a) #深拷贝

a.append(5)
a[4].append('c')

print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)
print("e=", e)