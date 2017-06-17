# coding=utf-8
from preprocess import *
from FictionTool import *
from SNA import *
from MM import CutWord

if __name__ == '__main__':
    names = get_name_list()
    en_names = get_name_list(en=True)
    # print '\n'.join(names)
    name_index = dict(zip(names, range(names.__len__())))
    shz = FictionTool('data/水浒传.txt')
    chapters, contents = shz.get_content_list(10, 20)
    mm = CutWord()
    links = []
    for c in contents:
        for para in c.split('\n'):
            appear_name = list(set(mm.mm_cut(para)))
            for i in range(len(appear_name)):
                for j in range(i+1, len(appear_name)):
                    links.append([name_index[appear_name[i]], name_index[appear_name[j]], 1])

    MG = MakeGraph(links, dict(enumerate(en_names)))

    DG = DrawGraph(MG).draw_graph('data/SNA.png', 1)
    # for node in MG.node_list:
    #     print node.label,  node.group



