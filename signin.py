from tkinter import *
from tkinter import messagebox
def loginfun():
    if user_entry.get()=='' or pass_entry.get()=='' :
        messagebox.showerror('Error','All Fields are required')
    elif user_entry.get()=='root' and pass_entry.get()=='Tharun@432':
        messagebox.showinfo('login Succesfull')
    else:
        messagebox.showerror('Eroor','Invalid Username or Password')
def func():
    if check.get()==1:
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
        user_entry.insert(END,'root')
        pass_entry.insert(END,'Tharun@432')
    else:
        user_entry.delete(0,END)
        pass_entry.delete(0,END)
root=Tk()
root.title('Signin')
root.geometry('770x650+50+10')
root.config(bg='sienna3')
label=Label(root,text='Customer Login',font=('castellar',28,'bold'),bg='sienna3',fg='white')
label.place(x=180,y=40)
frame=Frame(root,width=580,height=430)
frame.place(x=100,y=110)
img=PhotoImage(file='log.png')
log_img=Label(frame,image=img,bg='white')
log_img.place(x=230,y=5)
user_label=Label(frame,text='Username',font=('arial',22,'bold'),bg='white',fg='black')
user_label.place(x=120,y=150)
user_entry=Entry(frame,font=('times new roman',22,'bold'))
user_entry.place(x=120,y=200)

pass_label=Label(frame,text='Password',font=('arial',22,'bold'),bg='white',fg='black')
pass_label.place(x=120,y=250)
pass_entry=Entry(frame,font=('times new roman',22,'bold'))
pass_entry.place(x=120,y=300)
check=IntVar()
login_button=Button(frame,text="Login",font=('times new roman',17,'bold'),activebackground='black',activeforeground='white',fg='white',bg='black',bd=0,cursor='hand2',command=loginfun)
login_button.place(x=400,y=350)

remember_check=Checkbutton(frame,variable=check,text='Remember me',onvalue=1,offvalue=0,font=('times new roman',16,'bold'),bg='white',activeforeground='sienna3',command=func)
remember_check.place(x=80,y=350)

root.mainloop()