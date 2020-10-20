# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/16 11:23'
__author__ = 'Philgent'

"""
一个整数，它加上100后是一个完全平方数，
再加上168又是一个完全平方数，请问该数是多少？
"""
# 判断是否是完全平方数，最简单的方法是：平方根的值小数为0即可。
n = 0
while (n+1)**2 - n*n <= 168:
    n += 1
print(n+1)
for i in range((n+1)**2):
    if i**0.5 == int(i**0.5) and (i+168)**0.5==int((i+168)**0.5):
        print(i - 100)
