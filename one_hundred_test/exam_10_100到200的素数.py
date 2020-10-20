# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/20 16:05'
__author__ = 'Philgent'
"""
用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数
"""
import math
for i in range(100, 200):
    flag = 0
    for j in range(2, round(math.sqrt(i))+1):
        if i % j == 0:
            flag = 1
            break
    if flag:
        continue
    print(i)


print("\nSimplify the code with else\n")

for i in range(100, 200):
    for j in range(2, round(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        print(i)