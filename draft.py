# coding=utf-8
import re

a = '你好'
b = '   你好'


def preProcess(fiction_path):
    f = open(fiction_path)
    line_list = f.readlines()
    for t, line in enumerate(line_list):
        if t == 1000:
            break
        if not line.strip():
            continue
        if line.startswith(' '):
            print line.strip()


if __name__ == '__main__':
    # preProcess('data/水浒传.txt')
    print range(3, 5)
