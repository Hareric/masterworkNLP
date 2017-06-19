# coding=utf-8
from Tkinter import *
import ttk
import PIL.Image
import PIL.ImageTk
import shutil
from preprocess import *
from FictionTool import *
from SNA import *
from MM import CutWord
import numpy as np
import tkFileDialog

names = get_name_list()
name_index = dict(zip(names, range(names.__len__())))
shz = FictionTool(u'data/水浒传.txt')
def run(start, end, least_edge_value, least_com_num):
    chapters, contents = shz.get_content_list(start, end)
    # print '\n'.join(chapters)
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
    # print MG.divide_result.modularity
    DrawGraph(MG).draw_graph(u'cache/character_relation_%i_%i.png' % (start, end), least_com_num)
    return MG.divide_result.modularity, MG.find_topK()

def analyse(*args):
    start_chapter_value = int(start_chapter.get())
    end_chapter_value = int(end_chapter.get())
    least_com_num_value = int(least_com_num.get())
    least_edge_value_value = int(least_edge_value.get())
    com_modu, top_node = run(start_chapter_value, end_chapter_value, least_edge_value_value, least_com_num_value)
    im = PIL.Image.open(u'cache/character_relation_%i_%i.png' % (start_chapter_value, end_chapter_value))
    global photo
    photo = PIL.ImageTk.PhotoImage(im)
    picture_label.configure(image=photo)
    global name_list, value_list,modu
    for i in range(10):
        try:
            name_list[i].set(top_node[i].label)
            value_list[i].set(top_node[i].value)
        except IndexError:
            for i in range(10)[i:]:
                name_list[i].set("")
                value_list[i].set("")
            break
    modu.set(com_modu)

def save(*args):
    root_path = tkFileDialog.askdirectory(initialdir='D:')
    start_chapter_value = int(start_chapter.get())
    end_chapter_value = int(end_chapter.get())
    shutil.copy(u'cache/character_relation_%i_%i.png' % (start_chapter_value, end_chapter_value),
                root_path + u'/character_relation_%i_%i.png' % (start_chapter_value, end_chapter_value))
    print root_path

root = Tk()
root.title("水浒传人物关系分析")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=5)
mainframe.rowconfigure(0, weight=5)



im = PIL.Image.open(u"cache/white.png")
photo = PIL.ImageTk.PhotoImage(im)
picture_label = Label(mainframe, image=photo)
picture_label.grid(column=1, row=1, rowspan=12, columnspan=8, sticky=W)



start_chapter = StringVar()
end_chapter = StringVar()
least_com_num = StringVar()  # 社区最小个数
least_edge_value = StringVar()  # 小于的边忽略

ttk.Label(mainframe, text="开始章节").grid(column=1, row=13, sticky=(E))  # start chapter
start_entry = ttk.Entry(mainframe, width=10, textvariable=start_chapter)  # 输入框
start_chapter.set('1')
start_entry.grid(column=2, row=13, sticky=(W))
start_entry.focus()

ttk.Label(mainframe, text="结尾章节").grid(column=3, row=13, sticky=E)  # end chapter
end_entry = ttk.Entry(mainframe, width=10, textvariable=end_chapter)  # 输入框
end_chapter.set('10')
end_entry.grid(column=4, row=13, sticky=(W))
end_entry.focus()

ttk.Label(mainframe, text="最小社区").grid(column=1, row=14, sticky=(E))
least_com_num_entry = ttk.Entry(mainframe, width=10, textvariable=least_com_num)
least_com_num.set('2')
least_com_num_entry.grid(column=2, row=14, sticky=(W))
least_com_num_entry.focus()

ttk.Label(mainframe, text="最小边").grid(column=3, row=14, sticky=E)
least_edge_value_entry = ttk.Entry(mainframe, width=10, textvariable=least_edge_value)
least_edge_value.set('1')
least_edge_value_entry.grid(column=4, row=14, sticky=(W))
least_edge_value_entry.focus()

modu = StringVar()
ttk.Label(mainframe, text="社区模块度", font=("Arial, 12")).grid(column=5, row=14, sticky=(E))
ttk.Label(mainframe, textvariable=modu, font=("Arial, 12")).grid(column=6, row=14, sticky=(W))
modu.set('0')

name_list = []
value_list = []
for i in range(10):
    name_list.append(StringVar())
    value_list.append(StringVar())
ttk.Label(mainframe, text="   影响力排名    ", font=("Arial, 18")).grid(column=9, row=1, sticky=(W,E,S), columnspan=2)
ttk.Label(mainframe, text="人物名 PageRank值", font=("Arial, 15")).grid(column=9, row=2, sticky=(W,E,S), columnspan=2)
for i in range(name_list.__len__()):
    ttk.Label(mainframe, textvariable=name_list[i], font=("Arial, 12")).grid(column=9, row=i + 3, sticky=(E))
    ttk.Label(mainframe, textvariable=value_list[i], font=("Arial, 12")).grid(column=10, row=i + 3, sticky=(W))

ttk.Button(mainframe, text="Analyse", command=analyse).grid(column=5, row=15, sticky=W)
ttk.Button(mainframe, text="Save", command=save).grid(column=6, row=15, sticky=W)

# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# root.bind('<Return>', analyse)
root.mainloop()
