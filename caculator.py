# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()			
root.title("thanos caculator")
e= Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=15,pady=15)
def button_click(number):
    global f_num
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clea():
    e.delete(0,END)
def button_ad():
    first_number=e.get()
    global f_num
    global math 
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
def button_equa():
    global f_num
    global math 
    second_number=e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0, f_num + int(second_number))
    
    if math=="substraction":
        e.insert(0, f_num - int(second_number))
    
    if math=="division":
        e.insert(0, f_num / int(second_number))
    
    if math=="multiplication":
        e.insert(0, f_num * int(second_number))

def  button_sub():
    first_number=e.get()
    global f_num
    global math 
    math="substraction"
    f_num=int(first_number)
    e.delete(0,END)
def  button_div():
    first_number=e.get()
    global f_num
    global math 
    math="division"
    f_num=int(first_number)
    e.delete(0,END)
def  button_mul():
    first_number=e.get()
    global f_num
    global math 
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)
    


button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_ad = Button(root,text="+",padx=39,pady=25,command=button_ad)
button_equa = Button(root,text="=",padx=95,pady=20,command=button_equa)
button_clea= Button(root,text="SNAP",padx=88,pady=20,command=button_clea)
button_sub = Button(root,text="-",padx=41,pady=20,command=button_sub)
button_mul = Button(root,text="*",padx=39,pady=20,command=button_mul)
button_div = Button(root,text="/",padx=41,pady=20,command=button_div)



button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_clea.grid(row=4,column=1,columnspan=2)
button_ad.grid(row=5,column=0)
button_equa.grid(row=5,column=1,columnspan=2)
button_sub.grid(row=6,column=1)
button_mul.grid(row=6,column=2)
button_div.grid(row=6,column=0)



root.mainloop()
