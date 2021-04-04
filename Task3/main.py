from tkinter import *
import re
window = Tk()
window.title('Email Application')
window.geometry('300x300')
def send():

    submit = usernameEntry.get()
    print(submit)
    m = re.match('[^@]+@[^@]+\.[^@]+', submit)
    if m:
        my_string_var.set("VALID")
    else:
        my_string_var.set("INVALID")
    return
my_string_var=StringVar()
Label(window,font=('Calibri',11 ),textvariable = my_string_var).grid(row=0,column=3,sticky=W)
my_string_var.set("Email")
temp_username = StringVar()
usernameEntry = Entry(window, textvariable=temp_username)
usernameEntry.grid(row=0,column=1 , sticky=E)

Button(window,text = "submit" , command=send).grid(row=10,column=1,sticky=E)

window.mainloop()
