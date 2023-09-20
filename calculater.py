
from tkinter import *
mw=Tk()
mw.title('calculater')
def clear():
    db.delete(0,END)
def btn_clk(num):
    cur_num=db.get()
    clear()
    # db.delete(0,END)
    f_num=cur_num+num
    db.insert(0,f_num)
    
first_num=0
math=''
math_sign=''
ms_list=['+','-','*','/']
def calc(math_type,ms):
    global first_num,math,math_sign
    math_sign=ms
    math=math_type
    first_num=db.get()
    for x in ms_list:
        if x in first_num:
            first_num=first_num.replace(x,'')
    clear()
    db.insert(0,first_num+math_sign)
    
def equal():
    result=''
    global first_num
    second_num=db.get().replace(str(first_num)+math_sign,'')
    clear()
    if math=='add':
        result=int(first_num)+int(second_num)
    elif math=='sup':
        result=int(first_num)-int(second_num)
    elif math=='mul':
        result=int(first_num)*int(second_num)
    elif math=='div':
        result=int(first_num)/int(second_num)
        result=round(result,4)
    db.insert(0,result)


db=Entry(mw,width=14,font=('arial',28),justify=RIGHT)
b0=Button(mw,text='0',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('0'))
b1=Button(mw,text='1',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('1'))
b2=Button(mw,text='2',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('2'))
b3=Button(mw,text='3',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('3'))
b4=Button(mw,text='4',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('4'))
b5=Button(mw,text='5',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('5'))
b6=Button(mw,text='6',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('6'))
b7=Button(mw,text='7',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('7'))
b8=Button(mw,text='8',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('8'))
b9=Button(mw,text='9',padx=36,pady=10,font=('arial',14),command=lambda:btn_clk('9'))
cb=Button(mw,text='clear',padx=74,pady=10,font=('arial',14),command=clear)
bdiv=Button(mw,text='/',padx=36,pady=10,font=('arial',14),command=lambda:calc('div','/'))
bmul=Button(mw,text='*',padx=36,pady=10,font=('arial',14),command=lambda:calc('mul','*'))
badd=Button(mw,text='+',padx=36,pady=10,font=('arial',14),command=lambda:calc('add','+'))
bsup=Button(mw,text='-',padx=36,pady=10,font=('arial',14),command=lambda:calc('sup','-'))
be=Button(mw,text='=',padx=36,pady=40,font=('arial',14),command=equal)



b1.grid(row=3,column=0,padx=2,pady=2)
b2.grid(row=3,column=1,padx=2,pady=2)
b3.grid(row=3,column=2,padx=2,pady=2)

b4.grid(row=2,column=0,padx=2,pady=2)
b5.grid(row=2,column=1,padx=2,pady=2)
b6.grid(row=2,column=2,padx=2,pady=2)

b7.grid(row=1,column=0,padx=2,pady=2)
b8.grid(row=1,column=1,padx=2,pady=2)
b9.grid(row=1,column=2,padx=2,pady=2)

b0.grid(row=4,column=0,padx=2,pady=2)
cb.grid(row=4,column=1,padx=2,pady=2,columnspan=2)
bdiv.grid(row=5,column=0,padx=2,pady=2)
bmul.grid(row=5,column=1,padx=2,pady=2)
badd.grid(row=6,column=0,padx=2,pady=2)
bsup.grid(row=6,column=1,padx=2,pady=2)
be.grid(row=5,column=2,padx=2,pady=2,rowspan=2)

db.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
mw.mainloop()
