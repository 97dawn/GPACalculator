'''
Created on Jan 15, 2018

@author: Doeun Kim
'''
from tkinter import *


class MyFrame(Frame):
    def __init__(self, master):
        title = Label(font=('arial',30,'bold'), text="GPA Calculator",fg="Steel Blue",bd=10,anchor='w')
        title.grid(row=0, column=0)
        
        gpaLabel = Label(font=('arial',10,'bold'), text="GPA",bd=10,anchor='w')
        gpaLabel.grid(row=1, column=0)
        gpa = Entry();
        gpa.grid(row=1, column=1)
        
        c1 = Label(font=('arial',10,'bold'), text="Course 1",bd=10,anchor='w')
        c1.grid(row=2, column=0)
        c1Credit = Entry()
        c1Credit.grid(row=2,column=1)
        
        c2 = Label(font=('arial',10,'bold'), text="Course 2",bd=10,anchor='w')
        c2.grid(row=3, column=0)
        c2Credit = Entry()
        c2Credit.grid(row=3,column=1)
        
        c3 = Label(font=('arial',10,'bold'), text="Course 3",bd=10,anchor='w')
        c3.grid(row=4, column=0)
        c3Credit = Entry()
        c3Credit.grid(row=4,column=1)
        
        c4 = Label(font=('arial',10,'bold'), text="Course 4",bd=10,anchor='w')
        c4.grid(row=5, column=0)
        c4Credit = Entry()
        c4Credit.grid(row=5,column=1)
        
        c5 = Label(font=('arial',10,'bold'), text="Course 5",bd=10,anchor='w')
        c5.grid(row=6, column=0)
        c5Credit = Entry()
        c5Credit.grid(row=6,column=1)
        
        c6 = Label(font=('arial',10,'bold'), text="Course 6",bd=10,anchor='w')
        c6.grid(row=7, column=0)
        c6Credit = Entry()
        c6Credit.grid(row=7,column=1)
        
        c7 = Label(font=('arial',10,'bold'), text="Course 7",bd=10,anchor='w')
        c7.grid(row=8, column=0)
        c7Credit = Entry()
        c7Credit.grid(row=8,column=1)
        
        calculate = Button(text="Calculate")
        calculate.grid(row=9,column=1,padx=10, pady=10)
 
def main():
    root = Tk()
    root.title('GPA Calculator')
    root.geometry('600x500+100+100')
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()