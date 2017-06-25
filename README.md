# 基于社区检测的名著分析---以《水浒传》为例


## 代码说明
- **preprocess.py**  包含一些用来预处理的函数
- **FictionTool.py** 对《水浒传》文档进行处理 及提供一些后期处理的函数
- **MM.py**  最大正向正则匹配算法 用来匹配人物名
- **SNA.py**  社区检测算法及绘图
- **character_relation.py**  分析人物关系
- **main_gui.py**  提供gui界面

## 开源包
- **numpy**  提供矩阵运算
- **Pillow**  解析png图片格式
- **pycairo**  绘图工具包
- **python_igraph**  提供社区检测算法

[开源包下载地址（windows）][1]

## 运行说明
配置好开源包后 直接运行main_gui.py

## 效果图
### 整体效果图
   ![Heroes of the Marshes][2]
   ![Heroes of the Marshes][3]
   ![Heroes of the Marshes][4]
　　主体部分为社区检测效果图，同一个颜色的节点为归为同一个社区，颜色的深浅及节点的大小表示出该节点表示的人物的影响力。
右边部分显示出PageRank值最大的前几名人物。

　　下半部分为参数交互框，可以选择需要分析的章节的片段，其中“最小社区”值得是需要图示显示最小的社区，其中社区节点数小于2的默认不显示。“最小边”可用来忽略节点之间的关联值的大小，小于该值的边则忽略。

### 社区检测效果及剧情分析
#### a
   ![Heroes of the Marshes][5]
   ![Heroes of the Marshes][6]
   ![Heroes of the Marshes][7]
　　上三图为分别对章节1-10，章节1-15，章节1-30的人物进行社区检测，可以发现《水浒传》中的主要人物从一开始逐渐登场，拥有独自的故事，到后来人物与人物之间进行互动，到后期逐渐走向联合为108好汉大聚合（第70章）做了铺垫。
　　
　　《水浒传》人物——及时雨宋江，作为梁山未来的首领，其人物影响力也在节点的PageRank值中有所体现。
#### b
   ![Heroes of the Marshes][8]
　　上图为对章节15~30分析，可获得其人物社区图。
  
　　其中朱仝与雷横为同一社区，在《水浒传》中同为郓城县都头。

　　鲁智深、杨志、曹正为同一社区，在《水浒传》均来自二龙山的好汉。

　　阮小二、阮小七、阮小五为同一社区，在《水浒传》为阮氏三兄弟。

　　综上，社区检测效果基本符合原著。
#### c	
   ![Heroes of the Marshes][9]
　　上图为对章节82-100进行分析，其中第82章为梁山好汉招安剧情，后续剧情为征辽,平灭田虎,王庆，作为梁山第二把交椅卢俊义的人物影响力也可以逐渐看出。




  [1]: www.lfd.uci.edu/~gohlke/pythonlibs
  [2]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%281%29.jpg
  [3]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%282%29.jpg
  [4]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%283%29.jpg
  [5]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%284%29.jpg
  [6]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%285%29.jpg
  [7]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%286%29.jpg
  [8]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%287%29.jpg
  [9]: http://oevwfwaro.bkt.clouddn.com/Heroes%20of%20the%20Marshes%20%288%29.jpg
