from tkinter import *
import pickle
root=Tk()

#to clear the entry box
def clear():
    cy.set("")
    di.set("")
    hp.set("")
    we.set("")
    ac.set("")
    mo.set("")

#to predict mpg
def calculate_mpg():
    c=cy.get()
    d=di.get()
    h=hp.get()
    w=we.get()
    a=ac.get()
    m=mo.get()
    clear()
    fp=open("model.pkl","rb")
    model=pickle.load(fp)
    mpg=model.predict(np.array([c,d,h,w,a,m]).reshape(1,-1))
    t=Toplevel()
    label=Label(t,text=f"Your Car's \n Predicted Mileage is \n{mpg[0]:.2f} Miles Per Gallon.")
    label.config(bg='black', fg='white', font=('monospace', 25, 'bold'),height=5,width=20)
    label.pack()
    button=Button(t,text="Quit",command=t.destroy)
    button.config(bg='black', fg='red', font=('monospace', 25, 'bold'),height=1,width=20)
    button.pack()
    t.resizable(0,0)
    
    
#variables   
cy=DoubleVar()
di=DoubleVar()
hp=DoubleVar()
we=DoubleVar()
ac=DoubleVar()
mo=DoubleVar()

clear()

#labels
c_label=Label(root,text="Cylinders:")
d_label=Label(root,text="Displacement:")
h_label=Label(root,text="Horsepower:")
w_label=Label(root,text="Weight:")
a_label=Label(root,text="Accleration:")
m_label=Label(root,text="Model Year:")

# entry boxes
c_entry=Entry(root,textvariable=cy)
d_entry=Entry(root,textvariable=di)
h_entry=Entry(root,textvariable=hp)
w_entry=Entry(root,textvariable=we)
a_entry=Entry(root,textvariable=ac)
m_entry=Entry(root,textvariable=mo)

#buttons
button_1=Button(root,text="Get MPG",command=calculate_mpg)
button_2=Button(root,text="Exit",command=root.destroy)

#packing all widgets
c_label.grid(row=1,column=1,)
c_entry.grid(row=1,column=2,)
d_label.grid(row=2,column=1,)
d_entry.grid(row=2,column=2,)
h_label.grid(row=3,column=1,)
h_entry.grid(row=3,column=2,)
w_label.grid(row=4,column=1,)
w_entry.grid(row=4,column=2,)
a_label.grid(row=5,column=1,)
a_entry.grid(row=5,column=2,)
m_label.grid(row=6,column=1,)
m_entry.grid(row=6,column=2,)
button_1.grid(row=7,column=1,columnspan=2,sticky=W+E+N+S)
button_2.grid(row=8,column=1,columnspan=2,sticky=W+E+N+S)

c_entry.focus()

#configurations
c_label.config(bg="black",fg='white', font=('Helvetica', 20, 'italic'))
d_label.config(bg="black",fg='white', font=('Helvetica', 20, 'italic'))
h_label.config(bg="black",fg='white', font=('Helvetica', 20, 'italic'))
w_label.config(bg="black",fg='white', font=('Helvetica', 20, 'italic'))
a_label.config(bg="black",fg='white', font=('Helvetica', 20, 'italic'))
m_label.config(bg="black",fg='white', font=('Helvetica', 20, 'italic'))
c_entry.config(bg='white', fg='black', font=('Helvetica', 20, 'italic'))
d_entry.config(bg='white', fg='black', font=('Helvetica', 20, 'italic'))
h_entry.config(bg='white', fg='black', font=('Helvetica', 20, 'italic'))
w_entry.config(bg='white', fg='black', font=('Helvetica', 20, 'italic'))
a_entry.config(bg='white', fg='black', font=('Helvetica', 20, 'italic'))
m_entry.config(bg='white', fg='black', font=('Helvetica', 20, 'italic'))
button_1.config(bg='black', fg='green', font=('monospace', 25, 'bold'),relief="raised")
button_2.config(bg='black', fg='red', font=('monospace', 25, 'bold'),relief="raised")
root.config(bg="black")
root.title("MPG Prediction")
root.resizable(0,0)

root.mainloop()
