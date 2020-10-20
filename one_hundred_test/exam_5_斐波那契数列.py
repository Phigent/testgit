# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/20 13:45'
__author__ = 'Philgent'
"""
斐波那契数列（Fibonacci sequence），从1,1开始，
后面每一项等于前面两项之和
"""

#递归实现
def Fib(n):
    return 1 if n <= 2 else Fib(n-1) + Fib(n-2)
print(Fib(int(input("请输入想要打印第几个数"))))


#朴素实现
target = int(input())
res = 0
a, b = 1, 1
for i in range(target-1):
    a,b = b, a+b
    print(a)

print(a)