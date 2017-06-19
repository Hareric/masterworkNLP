# coding=utf-8
from preprocess import *
from FictionTool import *
from SNA import *
from MM import CutWord
import numpy as np

if __name__ == '__main__':
    names = get_name_list()
    en_names = get_name_list(en=True)
    name_index = dict(zip(names, range(names.__len__())))
    shz = FictionTool(u'data/水浒传.txt')
    modu_list = []
    def run(start, end,least_edge_value, least_com_num):
        chapters, contents = shz.get_content_list(start, end)
        print '\n'.join(chapters)
        mm = CutWord()
        matrix = np.zeros((names.__len__(), names.__len__()))
        links = []
        for c in contents:
            for para in c.split('\n'):
                appear_name = list(set(mm.mm_cut(para)))
                for i in range(len(appear_name)):
                    for j in range(i+1, len(appear_name)):
                        links.append([name_index[appear_name[i]], name_index[appear_name[j]], 1])
                        matrix[name_index[appear_name[i]], name_index[appear_name[j]]] += 1
        MG = MakeGraph(matrix, dict(enumerate(names)), least_edge_value)
        print MG.divide_result.modularity
        modu_list.append(MG.divide_result.modularity)
        for n in MG.find_topK():
            print n.label,n.rank, n.value
        DG = DrawGraph(MG).draw_graph(u'cache/character_relation_%i_%i.png' % (start, end), least_com_num)

    # t = 8
    # n = 120 / t
    # for i in range(n):
    #     run(i*t+1, (i+1) * t)
    # print "avg modularity: ", sum(modu_list)/n
    run(1,30,5,3)



