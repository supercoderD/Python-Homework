import tkinter as tk
from tkinter import ttk, messagebox 
class StationeryOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Stationery Order Management App")
        self.stationeryitems = {
            "Notebook": 3,
            "Pencil Pack": 2,
            "Pens": 4,
            "Erasers": 1,
            "Pencil Box": 6,
            "Color Pencils": 5
        }
        self.exchangerate = 94
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(
            frame,
            text="Stationery Order Management",
            font=("Arial", 20, "bold")
        ).grid(
            row=0,
            columnspan=3,
            padx=10,
            pady=10
        )
        self.itemlabels = {}
        self.itemquantities = {}
        for index, (item, price) in enumerate(
            self.stationery_items.items(),
            start=1
        ):
            itemlabel = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
 
            itemlabel.grid(
                row=index,
                column=0,
                padx=10,
                pady=5
            )
 
            self.item_labels[item] = itemlabel
            quantityentry = ttk.Entry(
                frame,
                width=5
            )
            quantityentry.grid(
                row=index,
                column=1,
                padx=10,
                pady=5
            )
            self.itemquantities[item] = quantityentry
        self.currencyvar = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.stationeryitems) + 1,
            column=0,
            padx=10,
            pady=5
        )
        currencydropdown = ttk.Combobox(
            frame,
            textvariable=self.currencyvar,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )
        currencydropdown.grid(
            row=len(self.stationeryitems) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currencydropdown.current(0)
        self.currencyvar.trace(
            "w",
            self.updateitemprices
        )
        orderbutton = ttk.Button(
            frame,
            text="Place Order",
            command=self.placeorder
        )
        orderbutton.grid(
            row=len(self.stationeryitems) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )
    def updateitemprices(self, *args):
        currency = self.currencyvar.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchangerate if currency == "INR" else 1
        for item, label in self.itemlabels.items():
            price = self.stationeryitems[item] * rate
            label.config(
                text=f"{item} ({symbol}{price}):"
            )
    def placeorder(self):
        totalcost = 0
        ordersummary = "Stationery Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchangerate if currency == "INR" else 1
        for item, entry in self.itemquantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.stationeryitems[item] * rate
                cost = quantity * price
                totalcost += cost
 
                if quantity > 0:
                    ordersummary += (
                        f"{item}: {quantity} x "
                        f"{symbol}{price} = {symbol}{cost}\n"
                    )
 
        if totalcost > 0:
            ordersummary += (
                f"\nTotal Cost: {symbol}{totalcost}"
            )
            messagebox.showinfo(
                "Order Placed",
                ordersummary
            )
        else:
            messagebox.showerror(
                "Error",
                "Please order at least one stationery item."
            )
if __name__ == "__main__":
    root = tk.Tk()
    app = StationeryOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()
