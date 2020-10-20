# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/13 16:31'
__author__ = 'Philgent'
"""
数字组合
1,2,3,4，能够组成多少个互不相同且无重复数字的三位数
"""

total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in (range(1, 5)):
            if((i!=j) and (j != k) and (k != i)):
                print(i, j, k)
                total+=1
print(total)

print("=========")

#简便方法  用itertools中的 permutations
import itertools
sum2 = 0
a = [1, 2, 3, 4]
for i in itertools.permutations(a, 3):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210

    print(i)  #输出的是元组
    #print(type(i))
    sum2 += 1
print(sum2)