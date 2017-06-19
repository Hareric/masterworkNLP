# coding=utf-8
from Tkinter import *  # 导入tkinter模块

'''获取路径
import tkFileDialog
filename = tkFileDialog.askdirectory(initialdir='/Users/Har')
print filename
'''

'''

def resize(ev=None):  # scale的回调函数
    labelDisplay.config(font='Helvetica -%d bold' % scale.get())  # 修改labelDisplay的字体大小，当然其他信息也可以改，比如text


root = Tk()  # 产生顶层窗口对象
root.title('水浒传人物分析')  # GUI名字
# root.geometry('250x150+0+0')  # 250x150设置窗口初始大小，如果没有这个设置，窗口会随着组件大小的变化而变化，0+0表示窗口左上角出现在屏幕的位置（）

labelDisplay = Label(root, text='Hello World!', font='Helvetica -12 bold',
                     bg='red')  # 创建一个Label，是要放置在root内的，文本为'Hello World!'，还有字体与背景色
labelDisplay.pack(fill=None, expand=1, ipadx=5,
                  ipady=5)  # 将labelDisplay放置进root，如果没有这句话，则不会显示这个组件。fill, expand, ipadx, ipady的说明在下面

labelDisplay1 = Label(root, text='Hello World!', font='Helvetica -12 bold',
                      bg='green')
labelDisplay1.pack(fill=BOTH, expand=1, padx=5, pady=5)  # padx, pady说明也在下面

scale = Scale(root, from_=10, to=40, orient=HORIZONTAL,
              command=resize)  # orient表示scale的放置方向，默认为vertical竖直的，command就是回调函数，为resize
scale.pack(fill=X, expand=0)

btQuit = Button(root, text='Quit', command=root.quit,  # 回调函数为quit函数，这时Tk类自带的
                fg='blue', bg='yellow',  # fg是前面的字体的颜色，bg是背景的颜色，Label组件也可以这样设置
                activeforeground='white', activebackground='red')  # 按下时的颜色
btQuit.pack(side=LEFT)

print(root.pack_slaves())  # 输出到当前代码处为止，所有在root上pack了的组件

mainloop()  # or root.mainloop()
'''

from Tkinter import *

#
# def change():
#     label.configure(image=bm2)
#
#
# top = Tk()
# bm = PhotoImage(file="/Users/Har/PycharmProjects/masterworkNLP/data/character_relation_1_8.png")
# bm2 = PhotoImage(file="/Users/Har/PycharmProjects/masterworkNLP/data/character_relation_41_48.png")
# label = Label(top, image=bm)
# label.pack()
# button = Button(top, text="change_picture", command=change)
# button.pack()
# top.mainloop()

from Tkinter import *
import PIL.Image
import PIL.ImageTk

root = Toplevel()

im = PIL.Image.open("/Users/Har/PycharmProjects/masterworkNLP/data/character_relation_1_8.png")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()

# root.mainloop()
