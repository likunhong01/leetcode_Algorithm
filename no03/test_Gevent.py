# coding=utf-8
# Version:python3.7.0
# Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


# import gevent
# gevent.greenlet()

def jump_range(up_to):
    step = 0
    while step < up_to:
        jump = yield step
        print("jump", jump)
        if jump is None:
            jump = 1
            step += jump
        print("step", step)


if __name__ == '__main__':
    iterator = jump_range(10)
    print(next(iterator))  # 0
    print(iterator.send(4))  # jump4; step4; 4
    print('---')
    print(next(iterator))  # jump None; step5; 5
    print(iterator.send(-1))  # jump -1; step4; 4
