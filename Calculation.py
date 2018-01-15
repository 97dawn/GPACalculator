'''
Created on Jan 15, 2018

@author: Doeun Kim
'''
from tkinter import *
from tkinter.ttk import Combobox

class Calculation:
      
    def construct(self,num):
        gpaLabel = Label(font=('arial',10,'bold'), text="GPA",bd=10,anchor='w')
        gpaLabel.grid(row=0, column=0)
        gpa = Entry(width=10);
        gpa.grid(row=0, column=1)
        
        
        
        outof = Label(font=('arial',10,'bold'), text=" / 4.0",bd=10,anchor='w')
        outof.grid(row=0, column=2)
        
        c1 = Label(font=('arial',10,'bold'), text="Course 1",bd=10,anchor='w')
        c1.grid(row=1, column=0)
        c1Credit = Entry(width=10)
        c1Credit.grid(row=1,column=1)
        
        c2 = Label(font=('arial',10,'bold'), text="Course 2",bd=10,anchor='w')
        c2.grid(row=2, column=0)
        c2Credit = Entry(width=10)
        c2Credit.grid(row=2,column=1)
        
        c3 = Label(font=('arial',10,'bold'), text="Course 3",bd=10,anchor='w')
        c3.grid(row=3, column=0)
        c3Credit = Entry(width=10)
        c3Credit.grid(row=3,column=1)
        
        c4 = Label(font=('arial',10,'bold'), text="Course 4",bd=10,anchor='w')
        c4.grid(row=4, column=0)
        c4Credit = Entry(width=10)
        c4Credit.grid(row=4,column=1)
        
        c5 = Label(font=('arial',10,'bold'), text="Course 5",bd=10,anchor='w')
        c5.grid(row=5, column=0)
        c5Credit = Entry(width=10)
        c5Credit.grid(row=5,column=1)
        
        c6 = Label(font=('arial',10,'bold'), text="Course 6",bd=10,anchor='w')
        c6.grid(row=6, column=0)
        c6Credit = Entry(width=10)
        c6Credit.grid(row=6,column=1)
        
        c7 = Label(font=('arial',10,'bold'), text="Course 7",bd=10,anchor='w')
        c7.grid(row=7, column=0)
        c7Credit = Entry(width=10)
        c7Credit.grid(row=7,column=1)
        
        for i in range(1,8):
            creditLabel = Label(font=('arial',10,'bold'), text="credits",bd=10,anchor='w')
            creditLabel.grid(row=i, column=2)
            letterGrade = Combobox(width=10)
            letterGrade['values']=['A','A-','B+','B','B-','C+','C','C-','D+','D','F']
            letterGrade.grid(row=i, column=3)
        calculate = Button(text="Calculate")
        calculate.grid(row=9,column=1,padx=10, pady=10)
        
    def __init__(self,uni,num):
        self.construct(num)
      