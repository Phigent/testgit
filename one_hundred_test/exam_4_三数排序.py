# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/19 15:31'
__author__ = 'Philgent'
'''
 输入三个整数x,y,z，请把这三个数由小到大输出。
'''

raw = []
for i in range(3):
    x = int(input('int{}:'.format(i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)

raw2 = []

for i in range(3):
    x = int(input('int{}:'.format(i)))
    raw2.append(x)
print(sorted(raw2))