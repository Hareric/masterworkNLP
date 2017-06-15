# coding=utf-8
from preprocess import *
from FictionTool import *
from SNA import *
from MM import CutWord

if __name__ == '__main__':
    names = get_name_list()
    en_names = get_name_list(True)
    print '\n'.join(names)
    name_index = dict(zip(names, range(names.__len__())))
    shz = FictionTool('data/水浒传.txt')
    chapters, contents = shz.get_content_list(0, 30)
    mm = CutWord()
    links = []
    for c in contents:
        appear_name = list(set(mm.mm_cut(c)))
        for i in range(len(appear_name)):
            for j in range(i+1, len(appear_name)):
                links.append([name_index[appear_name[i]], name_index[appear_name[j]], 1])

    MG = MakeGraph(links, dict(enumerate(en_names)))
    sub_node = []
    print MG.divide_result
    for community in MG.divide_result:
        if community.__len__() > 1:
            sub_node += community

    DG = DrawGraph(MG.graph, MG.node_list).draw_graph('data/SNA.png',sub_node)
    # for node in MG.node_list:
    #     print node.label,  node.group



