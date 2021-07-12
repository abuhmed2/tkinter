from tkinter import *
window = Tk()
two = Tk()
window.title('user information')
two.title('profile')
two.geometry('400x350')
window.geometry('500x350')
def myfunction():
    m = a.get()
    L = Label(two,text=m).pack()
    v = b.get()
    L = Label(two, text=v).pack()
    h = c.get()
    L = Label(two, text=h).pack()
    g = d.get()
    L = Label(two, text=g).pack()
    k = e.get()
    L = Label(two, text=k).pack()
def myfunctionn():
    bi = Label(text='please fill in all information').place(x=50,y=150)


def myfunctionnn():
  uy = Label(text='all our rights are reserved').place(x=50,y=190)

lbl1 = Label(text='Enter your name .. ')
lbl2 = Label(text='Enter your surname ..')
lbl3 = Label(text='Enter your age .. ')
lbl4 = Label(text='Enter your country .. ')
lbl5 = Label(text='Enter your job .. ')
lbl6 = Label(two,text='YOUR PROFILE')


lbl7 = Label(two,text='your name : ')
lbl8 = Label(two,text='your surname :')
lbl9 = Label(two,text='your age :')
lbl10 = Label(two,text='your country :')
lbl11 = Label(two,text='your job :')

lbl12 = Label(two,text='YOUR PROFILE')



btn = Button(text='login',command=myfunction,cursor='circle',width=4,height=2,fg='blue',bd=40)
bttn = Button(text='bilgi',bitmap='question',command=myfunctionn)
btttn = Button(text='bilgilendrme', bitmap='warning',command=myfunctionnn)

a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()
e = StringVar()

text = Entry(textvariable=a)
text1 = Entry(textvariable=b)
text2 = Entry(textvariable=c)
text3 = Entry(textvariable=d)
text4 = Entry(textvariable=e)
text.pack()
text1.pack()
text2.pack()
text3.pack()
text4.pack()

btn.place(x=235,y=150)
lbl1.place(x=20,y=5)
lbl2.place(x=20,y=35)
lbl3.place(x=20,y=60)
lbl4.place(x=20,y=85)
lbl5.place(x=20,y=110)

lbl7.place(x=20,y=25)
lbl8.place(x=20,y=50)
lbl9.place(x=20,y=75)
lbl10.place(x=20,y=95)
lbl11.place(x=20,y=120)
lbl6.pack()

bttn.place(x=20,y=150)
btttn.place(x=20,y=190)


window.mainloop()