from tkinter import *
from tkinter import ttk
import ttkthemes
window=ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('itft1')
window.geometry('1370x760')
window.config(bg='sienna3')
window.title('Retail system managed by TharunVoora')

mainframe=Frame(window,width=1320,height=690,bg='white')
mainframe.place(x=15,y=15)

titlelabel=Label(mainframe,text='Retail System',font=('arial',40,'bold'),fg='sienna3')
titlelabel.place(x=510,y=10)

timelabel=Label(mainframe,font=('chillar',18,'bold'),text='Time')
timelabel.place(x=1200,y=25)

logoutbutton=ttk.Button(mainframe,text='Log out')
logoutbutton.place(x=15,y=5)

searchbutton=ttk.Button(mainframe,text='Search')
searchbutton.place(x=15,y=45)

customerframe=LabelFrame(mainframe,text='Customer Details',font=('times new roman',20,'bold'),bd=10)
customerframe.place(x=5,y=80)

customernamelabel=Label(customerframe,text='Customer name',font=('times new roman',16,'bold'))
customernamelabel.grid(row=0,column=0)

customernameentry=Entry(customerframe,font=('times new roman',16,'bold'),width=25,bd=5,relief=GROOVE)
customernameentry.grid(row=0,column=1,padx=20)

emaillabel=Label(customerframe,text='Email',font=('times new roman',16,'bold'))
emaillabel.grid(row=0,column=2)
emailentry=Entry(customerframe,font=('times new roman',16,'bold'),width=25,bd=5,relief=GROOVE)
emailentry.grid(row=0,column=3,padx=20)


contactlabel=Label(customerframe,text='Contact',font=('times new roman',16,'bold'))
contactlabel.grid(row=0,column=4)
contactentry=Entry(customerframe,font=('times new roman',16,'bold'),width=23,bd=5,relief=GROOVE)
contactentry.grid(row=0,column=5,padx=18)

leftFrame=LabelFrame(mainframe,text='Products',font=('times new roman',20,'bold'),fg='sienna3',bd=5)
leftFrame.place(x=5,y=160)

selectcategory= Label(leftFrame,text='Select category',font=('times new roman',20,'bold'))
selectcategory.grid(row=0,column=0,sticky=W,pady=5)
selectcategoryentry=ttk.Combobox(leftFrame,font=('times new roman',14,'bold'),state='readonly',width=30)
selectcategoryentry['values']=('Electronics','Fashion','Home & Furniture','Tvs & Applications','Beauty and Personal Care','Sport books and more')
selectcategoryentry.grid(row=1,column=0)
selectcategoryentry.set('Select')

selectsubcategorylabel=Label(leftFrame,text='Sub Category',font=('times new roman',16,'bold'))
selectsubcategorylabel.grid(row=2,column=0,sticky=W,pady=5)
selectsubcategoryentry=ttk.Combobox(leftFrame,font=('times new roman',14,'bold'),state=DISABLED,width=30)
selectsubcategoryentry.grid(row=3,column=0)

productlabel=Label(leftFrame,text='Product',font=('times new roman',16,'bold'))
productlabel.grid(row=4,column=0,sticky=W,pady=5)
productentry=ttk.Combobox(leftFrame,font=('times new roman',14,'bold'),state=DISABLED,width=30)
productentry.grid(row=5,column=0)

quantitylabel=Label(leftFrame,text='Quantity',font=('times new roman',16,'bold'))
quantitylabel.grid(row=6,column=0)
quantityentry=Entry(leftFrame,font=('times new roman',16,'bold'),state=DISABLED,width=30,bd=5,relief=GROOVE)
quantityentry.grid(row=7,column=0,padx=10)


addtocartbutton=ttk.Button(leftFrame,text='Add to Cart')
addtocartbutton.grid(row=8,column=0,sticky=W,padx=30)

removebutton=ttk.Button(leftFrame,text='Remove')
removebutton.place(x=140,y=280)

clearAllbutton=ttk.Button(leftFrame,text='Clear All')
clearAllbutton.place(x=230,y=280)



window.mainloop()