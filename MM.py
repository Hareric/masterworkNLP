# coding=utf-8
from preprocess import get_name_list

class CutWord:
    word_set = None

    def __init__(self):
        self.word_set = set(get_name_list())

    def mm_cut(self, sentence=u'', max_len=4):
        """
        使用正向最大匹配法划分词语
        :param sentence: str 待划分句子
        :param max_len: int 最大词长 默认为6
        :return: str-list 已分词的字符串列表
        """
        sentence = sentence
        cur = 0  # 表示分词的位置
        sen_len = sentence.__len__()  # 句子的长度
        word_list = []  # 匹配出的词语
        while cur < sen_len:
            l = None
            for l in range(max_len, 0, -1):
                if sentence[cur: cur+l] in self.word_set:
                    break
            if l > 1:
                word_list.append(sentence[cur: cur+l])
            cur += l
        return word_list
