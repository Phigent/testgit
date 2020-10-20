# coding = utf-8
# version:python3.8.4
# Tools:Pycharm 2020
__date__ = '2020/10/20 15:04'
__author__ = 'Philgent'
import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)

for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)