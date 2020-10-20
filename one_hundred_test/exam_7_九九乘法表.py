# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/20 15:01'
__author__ = 'Philgent'
"""
分行与列考虑，共9行9列，i控制行，j控制列。
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%2ld '%(i, j, i*j), end=" ")
    print()