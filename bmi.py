from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=Tk()

win.title("BMI CALCULATOR")
win.geometry("500x500")
win.resizable(False,False)



def bmi():
    
    if w.get()==0.0 or v.get()==0.0:
        messagebox.showerror('BMI', 'Please select the values')
    else:    
        kg = w.get()
        m =float(v.get()/100)
        bmi = float(kg/(m*m))
        bmi = round(bmi, 1)
    
        bmi_label.config(text="BMI :" + '  ' + str(bmi),font=("Arial Bold",15))
    
        status(bmi)
    
def status(bmi):
    if bmi <= 18.5:
        disp_label.config(text="You are Underweight",bg='pink',font=("Arial Bold",15))
        
    elif (bmi > 18.5) and (bmi <= 24.9):
        disp_label.config(text="You are Normal",bg='green',font=("Arial Bold",15))
       
    elif (bmi > 24.9) and (bmi <= 29.9):
        disp_label.config(text="You are Overweight",bg='orange',font=("Arial Bold",15))
        
    elif (bmi > 29.9):
        disp_label.config(text="You are Obese",bg='red',font=("Arial Bold",15))
            

v=DoubleVar()
w=DoubleVar()


title=Label(win,text='BMI CALCULATOR',font=("Arial Bold",30))
title.pack(padx=50,pady=20)

height=Scale(win,variable=v,length=500,from_=0,to=220,resolution=1,orient=HORIZONTAL,troughcolor='yellow',label='Select Height in cms')
height.pack(padx=20,pady=20)

weight=Scale(win,variable=w,length=500,from_=0,to=200,resolution=0.1,orient=HORIZONTAL,troughcolor='blue',label='Select Weight in kgs')
weight.pack(padx=20,pady=20)

btn1=Button(win,text='CALCULATE BMI', bg='cyan', command=bmi)
btn1.pack(padx=20,pady=20)

bmi_label=Label(win)
bmi_label.pack(padx=50,pady=20)

disp_label=Label(win)
disp_label.pack(padx=50,pady=20)


win.mainloop()
