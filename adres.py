from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import *
from tkinter.filedialog import *

t=Tk()
t.title("Address book")

#
my_book= {}

def clear():
    entry_name.delete(0,END)
    entry_adres.delete(0,END)
    entry_bday.delete(0,END)
    entry_email.delete(0,END)
    entry_mobile.delete(0,END)

def update():
    key=entry_name.get()
    if key=="":
        messagebox.showinfo("Error", "The Name Entrybox Can Not Be Empty")
    else:
        if key not in my_book.keys():
            L.insert(END,key)
        my_book[key]= (entry_adres.get(), entry_bday.get(), entry_email.get(), entry_mobile.get())
        clear()

def edit():
    clear()
    index=L.curselection()
    if index:
        entry_name.insert(0,L.get(index))
        details=my_book[entry_name.get()]
        entry_adres.insert(0,details[0])
        entry_bday.insert(0,details[1])
        entry_email.insert(0,details[2])
        entry_mobile.insert(0,details[3])
    else:
        messagebox.showinfo("Error","Select a name.")

def delete():
    index=L.curselection()
    if index:
        del my_book[L.get(index)]
        L.delete(index)
        clear()
    else:
        messagebox.showinfo("Error", "Select a name")




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
          text="Name:")
nam.grid(row= 2, column=3, padx=5)

entry_name= Entry(t,
                  )
entry_name.grid(row=2, column=4,padx=5)
#email, mobile birtday Label and Entrybox

adres=Label(t,
          text="Adress:")
adres.grid(row= 3, column=3, padx=5)

entry_adres= Entry(t,
                  )
entry_adres.grid(row=3, column=4,padx=5)

mobile=Label(t,
          text="Mobile:")
mobile.grid(row= 4, column=3, padx=5)

entry_mobile= Entry(t,
                  )
entry_mobile.grid(row=4, column=4,padx=5)

email=Label(t,
          text="E-mail:")
email.grid(row= 5, column=3, padx=5)

entry_email= Entry(t,
                  )
entry_email.grid(row=5, column=4,padx=5)

bday=Label(t,
          text="Birthday:")
bday.grid(row= 6, column=3, padx=5)

entry_bday= Entry(t,
                  )
entry_bday.grid(row=6, column=4,padx=5)



edi= Button(t,
             text="Edit", command=edit)
edi.grid(row=7, column=0,padx=10,pady=10)
delet=Button(t,
              text="Delete",command=delete)
delet.grid(row=7, column=1, pady=10 , padx=10)

upad= Button(t,
             text="Update/Add",command=update)
upad.grid(row=7, column=4,padx=10,pady=10)

save= Button(t,
             text="Save", width=20)
save.grid(row=8, column=3)

t.mainloop()
