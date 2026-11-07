from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Reading Schedule Planner")
root.configure(bg="light blue")
root.geometry("500x300")
heading = Label(
    root,
    text="Reading Schedule Planner",
    font=("Arial", 18, "bold"),
    bg="light blue"
)
heading.pack(pady=50) 
instruction = Label(
    root,
    text="Create a simple plan to complete your book.",
    bg="light blue"
)
instruction.pack(pady=10)
def topwin():
    top = Toplevel(root)
    top.title("Create Reading Plan")
    top.configure(bg="light grey")
    top.geometry("500x350+50+50")
    pageslabel = Label(
        top,
        text="Enter total number of pages:",
        bg="light grey"
    )
    pagesentry = Entry(top)
    dailylabel = Label(
        top,
        text="Enter pages you can read each day:",
        bg="light grey"
    )
    dailyentry = Entry(top)
    resultlabel = Label(
        top,
        text="Your Reading Plan",
        font=("Arial", 14, "bold"),
        bg="light grey"
    ) 
    dayslabel = Label(
        top,
        text="Complete reading days:",
        bg="light grey"
    ) 
    remaininglabel = Label(
        top,
        text="Pages remaining:",
        bg="light grey"
    ) 
    daysentry = Entry(top)
    remainingentry = Entry(top)
    def calculateplan():
        try:
            totalpages = int(pagesentry.get())
            pagesperday = int(dailyentry.get())
            if totalpages <= 0 or pagesperday <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter numbers greater than zero."
                )
                return
            complete_days = totalpages // pagesperday
            remaining_pages = totalpages % pagesperday
            daysentry.delete(0, END)
            remainingentry.delete(0, END)
            daysentry.insert(END, str(complete_days))
            remainingentry.insert(END, str(remaining_pages))
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid whole numbers."
            )
    calculatebutton = Button(
        top,
        text="Create Plan",
        command=calculateplan,
        bg="#1261A0",
        fg="white"
    )
    pageslabel.place(x=80, y=40)
    pagesentry.place(x=280, y=40)
    dailylabel.place(x=80, y=90)
    dailyentry.place(x=280, y=90)
    calculatebutton.place(x=205, y=135)
    resultlabel.place(x=175, y=185) 
    dayslabel.place(x=80, y=235)
    daysentry.place(x=280, y=235)
    remaininglabel.place(x=80, y=275)
    remainingentry.place(x=280, y=275)
startbutton = Button(
    root,
    text="Create My Reading Plan",
    command=topwin,
    bg="#1261A0",
    fg="white"
)
startbutton.pack(pady=15)
root.mainloop()
