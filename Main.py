'''
Created on Jan 15, 2018

@author: Doeun Kim
'''
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from Calculation import Calculation
 

class MyFrame(Frame):
    
    def submit(self, e):
        uni = self.selectUni.get()
        num = self.numOfCourse.get()
        
        if uni == "" and num != "":
            messagebox.showerror("Error Message", "Please select your school")
        elif uni != "" and num =="" :
            messagebox.showerror("Error Message", "Please type the number of courses you took")
        elif uni == "" and num == "":
            messagebox.showerror("Error Message", "Please select your school and type the number of courses you took")
        else:
            self.master.quit()
            Calculation(uni, num)
       
    def __init__(self,master):
        self.master=master
        # Select campus
        self.selectUniLabel = Label(font=('arial',10,'bold'), text="Select Your School",bd=10)
        self.selectUniLabel.grid(row=0, column = 0)
        self.selectUni = Combobox()
        self.selectUni['values'] = ['Binghamton University','Stony Brook University','University at Albany']
        self.selectUni.grid(row=0, column=1)
        
        # Type the number of courses that the user took
        self.numOfCourseLabel = Label(font=('arial',10,'bold'), text="Number of Courses",bd=10)
        self.numOfCourseLabel.grid(row=1,column=0)
        self.numOfCourse = Entry()
        self.numOfCourse.grid(row=1, column=1)
        
        # Submit button
        self.ok = Button(text="ok", bg='white')
        self.ok.grid(row=2, column=1)
        self.ok.bind("<Button-1>", self.submit)
    
     
 
def main():
    root = Tk()
    root.title('SUNY GPA Calculator')
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()