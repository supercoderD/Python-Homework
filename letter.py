from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("Letter Writing Application")
window.geometry("600x500")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
def openletter():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath: return
    txtedit.delete("1.0", END)
    with open(filepath, "r") as inputfile:
        text = inputfile.read()
        txtedit.insert(END, text)
    window.title(f"Letter Writing Application - {filepath}")
def saveletter():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath: return
    with open(filepath, "w") as outputfile:
        text = txtedit.get("1.0", END)
        outputfile.write(text)
    window.title(f"Letter Writing Application - {filepath}")
txtedit = Text(window)
frbuttons = Frame(window, relief=RAISED, bd=2)
btnopen = Button(frbuttons, text="Open Letter", command=openletter)
btnsave = Button(frbuttons, text="Save Letter As...", command=saveletter)
btnopen.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btnsave.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
frbuttons.grid(row=0, column=0, sticky="ns")
txtedit.grid(row=0, column=1, sticky="nsew")
window.mainloop()
