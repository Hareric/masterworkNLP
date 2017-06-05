# coding=utf-8

class CutWord:
    word_set = None

    def __init__(self):
        self.word_set = set(load_file('./data/ChineseDic.txt', charset='GBK'))

    def mm_cut(self, sentence=u'', max_len=6):
        """
        使用正向最大匹配法划分词语
        :param sentence: str 待划分句子
        :param max_len: int 最大词长 默认为6
        :return: str-list 已分词的字符串列表
        """
        sentence = sentence
        cur = 0  # 表示分词的位置
        sen_len = sentence.__len__()  # 句子的长度
        word_list = []  # 划分的结果
        while cur < sen_len:
            l = None
            for l in range(max_len, 0, -1):
                if sentence[cur: cur+l] in self.word_set:
                    break
            word_list.append(sentence[cur: cur+l])
            cur += l
        return word_list

    def rmm_cut(self, sentence=u'', max_len=6):
        """
        使用逆向最大匹配法划分词语
        :param sentence: str 待划分句子
        :param max_len: int 最大词长 默认为6
        :return: str-list 已分词的字符串列表
        """
        sentence = sentence
        sen_len = sentence.__len__()  # 句子的长度
        cur = sen_len  # 表示分词的位置
        word_list = []  # 划分的结果
        while cur > 0:
            l = None
            if max_len > cur:
                max_len = cur
            for l in range(max_len, 0, -1):
                if sentence[cur-l: cur] in self.word_set:
                    break
            word_list.insert(0, sentence[cur-l: cur])
            cur -= l
        return word_list