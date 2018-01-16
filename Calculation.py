'''
Created on Jan 15, 2018

@author: Doeun Kim
'''
from tkinter import *
from tkinter.ttk import Combobox
from Albany import Albany
from Binghamton import Binghamton
from StonyBrook import StonyBrook

class Calculation(Frame):
    
    def clear(self,root):
        list = root.grid_slaves()
        for l in list:
            l.destroy()
            
    def __init__(self,root,uni,num):
        self.clear(root)
        self.courses=num
        gpaLabel = Label(root,font=('arial',10,'bold'), text="GPA",bd=10,anchor='w')
        gpaLabel.grid(row=0, column=0)
        self.gpa = Entry(root,width=10);
        self.gpa.grid(row=0, column=1)
        
        outof = Label(root,font=('arial',10,'bold'), text=" / 4.0",bd=10,anchor='w')
        outof.grid(row=0, column=2)
        
        self.courseCredits = []
        self.courseGrades = []
        for i in range(1,int(num)+1):
            courseLabel = Label(root,font=('arial',10,'bold'), text="Course "+str(i),bd=10,anchor='w')
            courseLabel.grid(row=i, column = 0)
            courseCredit = Entry(root,width=10)
            courseCredit.grid(row=i,column=1)
            self.courseCredits.append(courseCredit)
            creditLabel = Label(root,font=('arial',10,'bold'), text="credits",bd=10,anchor='w')
            creditLabel.grid(row=i, column=2)
            letterGrade = Combobox(root,width=10)
            if uni == 'University at Albany':
                letterGrade['values'] = Albany().getLetterGrades()['LetterGrades']
                self.letterGrades = Albany().getLetterGrades()['LetterGrades']
                self.grades =  Albany().getLetterGrades()['Grades']
            elif uni == 'Binghamton University':
                letterGrade['values'] = Binghamton().getLetterGrades()['LetterGrades']
                self.letterGrades = Binghamton().getLetterGrades()['LetterGrades']
                self.grades =  Binghamton().getLetterGrades()['Grades']
            elif uni == 'Stony Brook University':
                letterGrade['values'] = StonyBrook().getLetterGrades()['LetterGrades']
                self.letterGrades = StonyBrook().getLetterGrades()['LetterGrades']
                self.grades =  StonyBrook().getLetterGrades()['Grades']
            
            letterGrade.grid(row=i, column=3)
            self.courseGrades.append(letterGrade)
            
        calculate = Button(root,text="Calculate", command=self.calculate)
        calculate.grid(row=int(num)+1,column=1,padx=10, pady=10)
    
    def calculate(self):
        self.gpa.delete(0, END)
        gpa=0
        credits=0
        for i in range(len(self.courseCredits)):
            grade = self.courseGrades[i].get() # letter grade
            credit = int(self.courseCredits[i].get())
            credits += credit
            grade = self.grades[self.letterGrades.index(grade)]
            gpa += credit * grade            
        gpa /= credits
        self.gpa.insert(0, round(gpa,2))
            
            