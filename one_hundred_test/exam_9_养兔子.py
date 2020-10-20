# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/20 15:38'
__author__ = 'Philgent'
"""
有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
问每个月的兔子总数为多少？

可以构建四个数据，其中：
一月兔每个月长大成为二月兔，
二月兔变三月兔，三月兔变成年兔，
成年兔（包括新成熟的三月兔）生等量的一月兔
"""
month = int(input("繁殖几个月？： "))
month_1 = 1
month_2 = 0
month_3 = 0
month_elder = 0

for i in range(month):
    month_1, month_2, month_3, month_elder = month_elder+month_3,month_1,\
                                             month_2, month_elder+month_3
    print("第%d个月共"%(i+1),month_1+month_2+month_3+month_elder, '对兔子')
    print("其中1月兔：",month_1)
    print("其中2月兔：",month_2)
    print("其中3月兔：",month_3)
    print("其中成年兔：",month_elder)


