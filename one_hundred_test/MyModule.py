def mymain():
    print('Doing something in module', __name__)

if __name__ == '__main__':
    print('Executed from command line')
    mymain()