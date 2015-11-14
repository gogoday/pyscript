from tkinter import *
import time

def pop():
    def save():
        f = open('./my_work_log.txt', 'a')
        f.write('%-30s%s' % (time.ctime(), t.get('1.0', END)))
        print(t.get('1.0', END))
    root = Tk()
    t = Text(root)
    t.pack()
    Button(root, text='SAVE', command=save).pack(side=RIGHT)
    root.focus_set()
    root.wait_window()
    root.mainloop()
    
while True:
    pop()
    time.sleep(30*60)
    

