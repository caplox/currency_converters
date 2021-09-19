# import modules might have a different directory.
from tkinter import *
from Projects.Other.Finished import btc
import Projects.currency_con.currency_req.cur_rq_v2 as currq

root = Tk()
root.title("Currency Converter")
root.iconbitmap("d:/images/house.ico")

# Exchange rates with USD as base.
BTC = float(btc.f)
EUR = currq.ex_rate_EUR
USD = float(1)
GBP = currq.ex_rate_GBP
SEK = currq.ex_rate_SEK
DKK = currq.ex_rate_DKK

# Answer field at the top of the calculator
e = Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Answer field at the bottom. Enter x much currency you want to convert.
e2 = Entry(root, width=20)
e2.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
e2.insert(0, "Enter your desired amount")


# functions. Make the buttons work
def button_click(cur):
    global conv
    current = e.get()
    e.delete(0, END)
    e.insert(0, cur)
    cur1 = float(cur)
    conv = float(current) / cur1


def button_clear():
    e.delete(0, END)


def button_equal():
    e.delete(0, END)
    e.insert(0, float(amount) * float(conv))


def button_amount():
    global amount
    amount = e2.get()
    e2.delete(0, END)


# creating buttons for currencies

b_BTC = Button(root, text="BTC", padx=10, pady=10, command=lambda: button_click(BTC))
b_EUR = Button(root, text="EUR", padx=10, pady=10, command=lambda: button_click(EUR))
b_USD = Button(root, text="USD", padx=10, pady=10, command=lambda: button_click(USD))

b_GBP = Button(root, text="GBP", padx=10, pady=10, command=lambda: button_click(GBP))
b_SEK = Button(root, text="SEK", padx=10, pady=10, command=lambda: button_click(SEK))
b_DKK = Button(root, text="DKK", padx=10, pady=10, command=lambda: button_click(DKK))

b_NA1 = Button(root, text="N/A", padx=10, pady=10)
b_NA2 = Button(root, text="N/A", padx=10, pady=10)
b_NA3 = Button(root, text="N/A", padx=10, pady=10)

b_equal = Button(root, text="Clear", padx=10, pady=10, command=button_clear)
b_clear = Button(root, text="=", padx=10, pady=10, command=button_equal)
b_amount = Button(root, text="Am.", padx=15, pady=10, command=button_amount)

# Assigning locations to the buttons

b_BTC.grid(row=1, column=0)
b_EUR.grid(row=1, column=1)
b_USD.grid(row=1, column=2)

b_GBP.grid(row=2, column=0)
b_SEK.grid(row=2, column=1)
b_DKK.grid(row=2, column=2)

b_NA1.grid(row=3, column=0)
b_NA2.grid(row=3, column=1)
b_NA3.grid(row=3, column=2)

b_amount.grid(row=4, column=0)
b_equal.grid(row=4, column=1)
b_clear.grid(row=4, column=2)

root.mainloop()
