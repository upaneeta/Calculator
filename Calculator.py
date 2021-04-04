from tkinter import *
from tkinter import messagebox
# Making the window
root=Tk()
root.title("CALCULATOR")
root.geometry("300x350+530+170")
root.resizable(0,0)

val = ""
num_1st = 0
sign = "" 

# Functions to be used when the numbers are clicked
def button_0_clicked():
     global val
     val=val+"0"
     show_data.set(val)

def button_1_clicked():
     global val
     val=val+"1"
     show_data.set(val)

def button_2_clicked():
     global val
     val=val+"2"
     show_data.set(val)

def button_3_clicked():
     global val
     val=val+"3"
     show_data.set(val)

def button_4_clicked():
     global val
     val=val+"4"
     show_data.set(val)

def button_5_clicked():
     global val
     val=val+"5"
     show_data.set(val)

def button_6_clicked():
     global val
     val=val+"6"
     show_data.set(val)

def button_7_clicked():
     global val
     val=val+"7"
     show_data.set(val)

def button_8_clicked():
     global val
     val=val+"8"
     show_data.set(val)

def button_9_clicked():
     global val
     val=val+"9"
     show_data.set(val)


# Functions to be used when the operators are clicked
def button_add_clicked():
     global num_1st,val,sign
     try:
          num_1st=int(val)
     except:
          num_1st=0
     val = val + "+"
     sign="+"
     show_data.set(val)

def button_sub_clicked():
     global num_1st,val,sign
     try:
          num_1st=int(val)
     except:
          num_1st=0
     val = val + "-"
     sign="-"
     show_data.set(val)

def button_mult_clicked():
     global num_1st,val,sign
     num_1st=int(val)
     val = val + "*"
     sign="*"
     show_data.set(val)

def button_div_clicked():
     global num_1st,val,sign
     num_1st=int(val)
     val = val + "/"
     sign="/"
     show_data.set(val)

# Function for clearing the screen
def button_C_clicked():
     global val
     val=" "
     show_data.set(val)

def button_equal_clicked():
     global num_1st,sign,val
     val2 = val
     if sign=="+":
          num_2nd=int(val.split("+")[1])
          res=num_1st+num_2nd
          val=str(res)
          show_data.set(val)
     if sign=="-":
          num_2nd=int(val.split("-")[1])
          res=num_1st-num_2nd
          val=str(res)
          show_data.set(val)
     if sign=="*":
          num_2nd=int(val.split("*")[1])
          res=num_1st*num_2nd
          val=str(res)
          show_data.set(val)
     if sign=="/":
          num_2nd=int(val.split("/")[1])
          if num_2nd == 0:
               messagebox.showerror("Error", "Oops! Can't divide by zero")
               num_1st = ""
               val = ""
               show_data.set(val)
          else:
               res=num_1st/num_2nd
               val=str(res)
               show_data.set(val)







# Making the screen to see the proceedings
show_data=StringVar()
label=Label(root,bg="black",fg="white",borderwidth=4,relief='raised',text="label ",font=("arial","25"),anchor=SE,textvariable=show_data)
label.pack(expand=True,fill="both")

# Making the frames
button_row_1=Frame(root,bg='black')
button_row_1.pack(expand=True,fill="both")

button_row_2=Frame(root,bg='black')
button_row_2.pack(expand=True,fill="both")

button_row_3=Frame(root,bg='black')
button_row_3.pack(expand=True,fill="both")

button_row_4=Frame(root,bg='black')
button_row_4.pack(expand=True,fill="both")

# Making the buttons
button_1=Button(button_row_1,text="1",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_1_clicked)
button_1.pack(side='left',expand=True,fill='both')

button_2=Button(button_row_1,text="2",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_2_clicked)
button_2.pack(side='left',expand=True,fill='both')

button_3=Button(button_row_1,text="3",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_3_clicked)
button_3.pack(side='left',expand=True,fill='both')

button_add=Button(button_row_1,text="+",bg="black",fg='deep pink',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_add_clicked)
button_add.pack(side='left',expand=True,fill='both')


button_4=Button(button_row_2,text="4",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_4_clicked)
button_4.pack(side='left',expand=True,fill='both')

button_5=Button(button_row_2,text="5",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_5_clicked)
button_5.pack(side='left',expand=True,fill='both')

button_6=Button(button_row_2,text="6",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_6_clicked)
button_6.pack(side='left',expand=True,fill='both')

button_subtract=Button(button_row_2,text="- ",bg="black",fg='deep pink',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_sub_clicked)
button_subtract.pack(side='left',expand=True,fill='both')


button_7=Button(button_row_3,text="7",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_7_clicked)
button_7.pack(side='left',expand=True,fill='both')

button_8=Button(button_row_3,text="8",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_8_clicked)
button_8.pack(side='left',expand=True,fill='both')

button_9=Button(button_row_3,text="9",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_9_clicked)
button_9.pack(side='left',expand=True,fill='both')

button_multiply=Button(button_row_3,text="*",bg="black",fg='deep pink',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_mult_clicked)
button_multiply.pack(side='left',expand=True,fill='both')


button_C=Button(button_row_4,text="C",bg="black",fg='deep pink',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_C_clicked)
button_C.pack(side='left',expand=True,fill='both')

button_0=Button(button_row_4,text="0",bg="black",fg='white',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_0_clicked)
button_0.pack(side='left',expand=True,fill='both')

button_equal=Button(button_row_4,text="=",bg="black",fg='deep pink',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_equal_clicked)
button_equal.pack(side='left',expand=True,fill='both')

button_divide=Button(button_row_4,text="/",bg="black",fg='deep pink',font=('tahoma','19'),relief = GROOVE,border = 0,command=button_div_clicked)
button_divide.pack(side='left',expand=True,fill='both')




















































button2=Button(root,text="2")

button3=Button(root,text="3")

button_divide=Button(root,text="/")

button4=Button(root,text="4")

button5=Button(root,text="5")

button6=Button(root,text="6")

button_multiply=Button(root,text="*")

button7=Button(root,text="7")

button8=Button(root,text="8")

button9=Button(root,text="9")

button_subtract=Button(root,text="-")

root.mainloop()
