# !/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2020/11/26 15:13
# @Author : longtao.wu
# @Email: eustancewu@gmail.com
# @File : process.py
# @Software: PyCharm
import re
import matplotlib.pyplot as plt


def process(raw_data):
    with open(raw_data, ) as fhand:
        extract_data = {1: [], 2: [], 3: [], 4: []}
        for line in fhand:
            line = line.strip()
            if 'wr_bytes' in line:
                stuff1 = re.findall(r'\d+', line, re.IGNORECASE)
                extract_data[1].append(float(stuff1[0]))
    return extract_data[1]


def gap_list(extract_data):
    q = []
    for _ in range(len(extract_data) - 1):
        q.append(float((extract_data[_ + 1] - extract_data[_]) / 1048576))
    return q


def plots(extract_data):
    num = len(extract_data)
    x = list(_ * 2 for _ in range(num))
    plt.plot(x, extract_data, color='r', label="ATT-RLSTM")
    plt.show()


if __name__ == '__main__':
    k = process('rawout.data')
    z = gap_list(k)
    plots(z)
