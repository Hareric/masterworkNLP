# coding=utf-8
#        ┏┓　　　┏┓+ +
# 　　　┏┛┻━━━┛┻┓ + +
# 　　　┃　　　　　　　┃ 　
# 　　　┃　　　━　　　┃ ++ + + +
# 　　 ████━████ ┃+
# 　　　┃　　　　　　　┃ +
# 　　　┃　　　┻　　　┃
# 　　　┃　　　　　　　┃ + +
# 　　　┗━┓　　　┏━┛
# 　　　　　┃　　　┃　　　　　　　　　　　
# 　　　　　┃　　　┃ + + + +
# 　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
# 　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
# 　　　　　┃　　　┃
# 　　　　　┃　　　┃　　+　　　　　　　　　
# 　　　　　┃　 　　┗━━━┓ + +
# 　　　　　┃ 　　　　　　　┣┓
# 　　　　　┃ 　　　　　　　┏┛
# 　　　　　┗┓┓┏━┳┓┏┛ + + + +
# 　　　　　　┃┫┫　┃┫┫
# 　　　　　　┗┻┛　┗┻┛+ + + +
"""
Author = Eric_Chan
Create_Time = 2016/05/06
使用igraph包中的BGLL算法对社区进行社区检测
输入用户-用户权值矩阵
输出社区检测结果和社区模块度
"""

import igraph

color_dict = {0: "pink", 1: "green", 2: "purple", 3: "orange", 4: "blue", 5: "yellow", 6: "red", 7: "#8B2500",
              8: "#87CEEB", 9: "#707070",
              10: "#FFF68F", 11: "#FFEFD5", 12: "#FFE4E1", 13: "#FFDEAD", 14: "#FFC1C1", 15: "#FFB90F", 16: "#FFA54F",
              17: "#FF8C00",
              18: "#698B69", 19: "#FF6EB4", 20: "#FF4500", 21: "#FF3030", 22: "#F5DEB3", 23: "#F0FFFF", 24: "#F08080",
              25: "#EED2EE", 26: "#EECFA1",
              27: "#EECBAD", 28: "#EEC900", 29: "#DDA0DD", 30: "#E3E3E3", 31: "#DB7093", 32: "#D8BFD8", 33: "#D2B48C",
              34: "#CDCDB4",
              35: "#CDAD00", 36: "#CD853F", 37: "#CD5555", 38: "#CAE1FF", 39: "#BCEE68", 40: "#A0522D", 41: "#AEEEEE",
              42: "#9AFF9A",
              43: "#B03060", 44: "#8B6508", 45: "#8B475D", 46: "#8B1A1A", 47: "#836FFF", 48: "#7A378B", 49: "#76EEC6",
              50: "black"
              }


class DrawGraph:
    def __init__(self, graph, node_list):
        """
        :param graph: igraph.Graph()
        :param node_list: [.label .value .rank .group, ]
        """
        self.graph = graph
        self.node_list = node_list

    def draw_graph(self, file_name):
        """
        :param file_name:
        :return:
        """
        graph = self.graph
        node_list = self.node_list
        layout = graph.layout_fruchterman_reingold()
        v_size_list = []  # 记录节点大小的列表
        v_color_list = []  # 记录节点颜色的列表
        v_label_list = []  # 记录标签名的列表
        for node in node_list:
            v_size_list.append(300 * node.value + 10)
            v_color_list.append(color_dict[node.group])
            v_label_list.append(node.label.encode('utf-8'))

        p = igraph.Plot()
        p.background = "#f0f0f0"  # 将背景改为白色，默认是灰色网格

        p.add(graph,
              bbox=(50, 50, 550, 550),  # 设置图占窗体的大小，默认是(0,0,600,600)
              layout=layout,  # 图的布局
              vertex_size=v_size_list,  # 点的尺寸
              edge_width=0.5, edge_color="grey",  # 边的宽度和颜色，建议灰色，比较好看
              vertex_label_size=8,  # 点标签的大小
              vertex_label=v_label_list,
              vertex_color=v_color_list, )  # 为每个点着色
        p.save(file_name)  # 将图保存到特定路径，igraph只支持png和pdf
        p.remove(graph)  # 清除图像


class MakeGraph:
    class Node:
        """
        记录每个节点的索引号，对应标签名，中心度值， 中心度值排名， 社区检测后节点所属组别， 是否为topK节点
        """

        def __init__(self):
            self.node_index = int
            self.label = ''
            self.value = int
            self.rank = int
            self.group = int
            self.is_topK = False
            self.influence = float

    def __init__(self, node_links, node_labels_dict):
        self.users_link = node_links  # 节点权值矩阵
        self.user_num = len(node_labels_dict)  # 节点个数
        self.node_list = []  # 保存每个节点属性的列表
        for i in range(self.user_num):
            self.node_list.append(self.Node())
            self.node_list[i].node_index = i
        for k, v in node_labels_dict.items():
            self.node_list[k].label = v
        self.graph = None  # 节点图
        self.divide()

    def __create_graph(self):
        """
        使用igraph构建图
        :return: graph, weights list
        """
        g = igraph.Graph(self.user_num, directed=True)
        weights = []
        edges = []
        for line in self.users_link:
            edges += [(line[0], line[1])]
            weights.append(line[2])
        g.add_edges(edges)
        node_value = g.pagerank(weights=weights)
        for i in range(self.user_num):
            self.node_list[i].value = node_value[i]
        self.graph = g
        return g, weights

    def __calculate_rank(self):
        """
        根据每个节点的pageRank值进行排名并记录
        :return:
        """
        node_values = [node.value for node in self.node_list]  # 提取节点中心度值
        node_values.sort(reverse=True)
        for node in self.node_list:
            node.rank = node_values.index(node.value)

    def __find_topK(self):
        """
        :param node_list: 节点属性列表
        :return: topK个节点属性列表
        """
        node_list = sorted(self.node_list, key=lambda c: c.value, reverse=True)
        topK_list = [node_list[0]]
        self.node_list[node_list[0].node_index].is_topK = True
        value = node_list[0].value
        for node in node_list[1:]:
            if node.value > value * 0.3 and topK_list.__len__() < self.user_num * 0.1:
                self.node_list[node.node_index].is_topK = True
                topK_list.append(node)
                value = node.value
            else:
                break
        return topK_list

    def __calc_influence(self):
        """
        对每个节点的value值进行归一化作为用户影响力评估
        :return:
        """
        max_v = max([n.value for n in self.node_list])
        min_v = min([n.value for n in self.node_list])
        dis = (max_v - min_v) / 5
        for node in self.node_list:
            if node.value < min_v + dis:
                node.influence = 1
            elif node.value < min_v + dis * 2:
                node.influence = 2
            elif node.value < min_v + dis * 3:
                node.influence = 3
            elif node.value < min_v + dis * 4:
                node.influence = 4
            else:
                node.influence = 5

    def divide(self):
        """
        使用igraph包中BGLL算法对已构建好的图进行社区检测
        并为每个节点标明
        :return:
        """
        graph, weights = self.__create_graph()
        self.__calculate_rank()
        # self.__find_topK()
        self.__calc_influence()
        divide_result = graph.community_walktrap(weights=weights, steps=4).as_clustering()
        # divide_result = graph.community_multilevel(weights=weights)
        for index, community in enumerate(divide_result):
            for n in community:
                self.node_list[n].group = index


if __name__ == '__main__':
    labels = dict(load_data('dataSet/label_link.xls', 0))
    links = load_data('dataSet/label_link.xls', 1)
    MG = MakeGraph(links, labels)
    for node in MG.node_list:
        print node.label, node.value, node.rank, node.group
    Weibo_User = Louvain(links)
    print Weibo_User.divide_result
    for com in Weibo_User.divide_result:
        for i in com:
            print labels[i],
        print
    print 'modularity:', Weibo_User.modularity
    print Weibo_User.node_value_dict
