from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import *
from tkinter.filedialog import *

t=Tk()
t.title("Address book")

#
my_book= {}

head= Label(t,
            text="My Address Book", width=30)
head.grid(row=0,column=1, pady=10 , columnspan=3)

ope=Button(t,
           text="open",command=open)
ope.grid(row=0, column=3, pady=10,)

L=Listbox(t,
          width=30,height=15)
L.grid(row=2 , column=0, pady=10,columnspan=3, rowspan=5)
#L.bind("<<ListboxSelect>>",display)

nam=Label(t,
          text="Name")
nam.grid(row= 2, column=3, padx=5)

entry_name= Entry(t,
                  )
entry_name.grid(row=2, column=4,padx=5)
#adress, email, mobile birtday Label and Entrybox
edit= Button(t,
             text="Edit")
edit.grid(row=7, column=0,padx=10,pady=10)
delete=Button(t,
              text="Delete")
delete.grid(row=7, column=1, pady=10 , padx=10)

t.mainloop()