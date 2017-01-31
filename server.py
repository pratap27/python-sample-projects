import sys
from socket import *
from tkinter import *
from threading import *
class receive(Thread):
    def __init__(self,s,conn,txtbox):
        Thread.__init__(self)
        self.s=s
        self.conn=conn
        self.txtbox=txtbox
    def run(self):
        while 1:
            data = self.conn.recv(1024)
            if not data : break
            txt = data.decode('UTF-8')
            self.txtbox.configure(state = 'normal')
            self.txtbox.insert(END,'From client : %s\n'%txt)
            self.txtbox.configure(state = 'disabled')

class initi(Thread):
    HOST = 'localhost'
    PORT = 6014
    s = socket(AF_INET,SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)
    print('server is running ......')
    conn,addr = s.accept()
    print('connected by',addr)
    def __init__(self,root):
        Thread.__init__(self)
        self.root = root
        frame= Frame(root)
        frame.grid(row=2,column=3)
        self.mbut = Button(frame,text='quit',command=frame.quit,bg='black',fg='white')
        self.mbut.grid(row=1,column=2)
        self.mbut.config(width=15)
        self.mbut1 =Button(frame,text='send',command=self.send,bg='black',fg='white')
        self.mbut1.grid(row=1,column=1)
        self.mbut1.config(width=15)
        self.entbox = Entry(frame,width=40)
        self.entbox.grid(row=1,column=0)
        self.txtbox = Text(frame,height=20,width=60,wrap=WORD)
        self.txtbox.grid(row=0,columnspan=3)
        self.txtbox.insert(END,'Welcome\n')
        self.txtbox.configure(state='disabled')
    def send(self):
        self.txtbox.configure(state='normal')
        reply = self.entbox.get()
        self.txtbox.insert(END,'To client : %s\n'%reply)
        self.entbox.delete(0,END)
        self.conn.sendall(bytes(reply,'UTF-8'))
        self.txtbox.configure(state='disabled')
    def run(self):
        receive(self.s,self.conn,self.txtbox).start()
obj = Tk()
obj.title('host')
app = initi(obj)
app.start()
obj.mainloop()



