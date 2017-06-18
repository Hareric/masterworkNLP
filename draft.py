# coding=utf-8
import re

# coding=utf-8
import urllib2
import re
# 6285399016554496258 6282837243963048194
# content = urllib2.urlopen('http://toutiao.com/group/6285399016554496258/comments/?count=901&format=json').read()
# comment = re.findall('"text": "(.*?)",', content)
# f1 = open('data/c2.txt', 'w')
# for j in comment:
#     f1.write(j.decode('unicode-escape').encode('utf-8') + '\n')

import numpy as np
import random
appear_name = '12312123'
for i in range(len(appear_name)):
        for j in range(i+1, len(appear_name)):
            print i,j