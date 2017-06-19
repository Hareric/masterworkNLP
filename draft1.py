# coding=utf-8
from Tkinter import *
import ttk
import PIL.Image
import PIL.ImageTk


def calculate(*args):
    try:
        value = float(start_chapter.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("水浒传人物关系分析")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=5)
mainframe.rowconfigure(0, weight=5)


im = PIL.Image.open("data/white.png")
photo = PIL.ImageTk.PhotoImage(im)
label = Label(mainframe, image=photo).grid(column=1, row=1, rowspan=3, sticky=W)

start_chapter = StringVar()
end_chapter = StringVar()
meters = StringVar()
ttk.Label(mainframe, text="start chapter").grid(column=2, row=1, sticky=(W,S))
ttk.Label(mainframe, text="end chapter").grid(column=2, row=2, sticky=W)
start_entry = ttk.Entry(mainframe, width=10, textvariable=start_chapter)
start_entry.grid(column=3, row=1, sticky=(W, E,S))
end_entry = ttk.Entry(mainframe, width=10, textvariable=end_chapter)
end_entry.grid(column=3, row=2, sticky=(W, E))
start_entry.focus()
end_entry.focus()

ttk.Button(mainframe, text="Analyse", command=calculate).grid(column=3, row=3, sticky=W)
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
for child in mainframe.winfo_children():child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)
root.mainloop()



