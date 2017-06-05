# coding=utf-8
from preprocess import *
from FictionTool import *
from SNA import *
import nltk

if __name__ == '__main__':
    names = get_name_list()
    name_index = dict(zip(names, range(names.__len__())))
    shz = FictionTool('data/水浒传.txt')
    chapters, contents = shz.get_content_list(1, 70)
    print contents[1]
    c1 = nltk.Text(contents[1])
    print c1.findall("毕竟")

