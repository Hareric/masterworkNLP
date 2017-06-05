# coding=utf-8
from preprocess import *
from FictionTool import *
from SNA import *
from MM import CutWord

if __name__ == '__main__':
    names = get_name_list()
    name_index = dict(zip(names, range(names.__len__())))
    shz = FictionTool('data/水浒传.txt')
    chapters, contents = shz.get_content_list(0, 70)
    mm = CutWord()
    links = []
    for c in contents:
        appear_name = list(set(mm.mm_cut(c)))
        for i in range(len(appear_name)):
            for j in range(i+1, len(appear_name)):
                links.append([name_index[appear_name[i]], name_index[appear_name[j]], 1])
    MG = MakeGraph(links, dict(enumerate(names)))
    DG = DrawGraph(MG.graph, MG.node_list).draw_graph('sdas.png')
    for node in MG.node_list:
        print node.label,  node.group



