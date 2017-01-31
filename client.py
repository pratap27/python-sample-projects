import sys
from socket import *
from tkinter import *
from threading import *
class receive(Thread):
    def __init__(self,s,txtbox):
        Thread.__init__(self)
        self.s=s
        self.txtbox=txtbox
    def run(self):
        while 1:
            reply = self.s.recv(1024)
            if not reply : break
            txt = reply.decode('UTF-8')
            self.txtbox.configure(state='normal')
            self.txtbox.insert(END,'From server : %s\n'%txt)
            self.txtbox.configure(state='disabled')
class initi(Thread):
    HOST = 'localhost'
    PORT = 6014
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((HOST,PORT))
    def __init__(self,root):
        Thread.__init__(self)
        self.root=root
        frame= Frame(root)
        frame.grid(row=2,column=3)
        self.mbut =Button(frame,text='quit',command=frame.quit,bg='black',fg='white')
        self.mbut.grid(row=1,column=2)
        self.mbut.config(width=15)
        self.mbut1 =Button(frame,text='send',command=self.send,bg='black',fg='white')
        self.mbut1.grid(row=1,column=1)
        self.mbut1.config(width=15)
        self.entbox = Entry(frame,width=40)
        self.entbox.grid(row=1,column=0)
        self.txtbox = Text(frame,height=20,width=60,wrap=WORD)
        self.txtbox.grid(row=0,columnspan=3)
        self.txtbox.insert(END,'welcome\n')
        self.txtbox.configure(state='disabled')
    def send(self):
        self.txtbox.configure(state='normal')
        text = self.entbox.get()
        self.txtbox.insert(END,'To server : %s\n'%text)
        self.entbox.delete(0,END)
        self.s.send(bytes(text,'UTF-8'))
        self.txtbox.configure(state='disabled')
    def run(self):
        receive(self.s,self.txtbox).start()
obj = Tk()
obj.title('client')
app = initi(obj)
app.start()
obj.mainloop()
