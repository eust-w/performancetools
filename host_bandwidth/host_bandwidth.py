# !/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2020/11/26 13:46
# @Author : longtao.wu
# @Email: eustancewu@gmail.com
# @File : host_bandwidth.py
# @Software: PyCharm
import os
import threading
import time


def run_cmd():
    q = os.popen('virsh domblkstat --domain 9f39b7b0ecdd44b6ad07e9abecd8b22a --device vdb')
    with open('rawout_1.data', 'a+') as _h:
        _h.write(str(q.read()))


def main():
    time_start = time.time()
    print 'the 1:', time_start
    for _ in range(200):
        Q = threading.Thread(target=run_cmd)
        print 'start', time.time()
        Q.start()
        print 'sleep', time.time()
        time.sleep(2 - 0.0029)


if __name__ == '__main__':
    main()
