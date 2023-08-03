from tkinter import *
from tkcalendar import *

apple = Tk()


def choice_date():
    present_date = display_cal.get_date()
    user_date = Label(text=present_date)
    user_date.pack(padx=2, pady=2)


display_cal = Calendar(apple, setmode="day", date_pattern='dd/mm/yyyy')
display_cal.pack(padx=15, pady=15)

# photo = PhotoImage(file=r"file:///D:/MASAI%20CAP04/Project/5993123.png")
open_cal = Button(apple, text="SELECT DATE", bg="black", fg="white", command=choice_date)
open_cal.pack(padx=15, pady=15)

apple.geometry('400x400')
apple.title("GUI Calendar")
apple.configure(bg="red")
apple.mainloop()
