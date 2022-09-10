from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("CALCULATOR BY UPLAKSH")
size = Font(size=15)


def entries(numbers):
    initial = str(value.get())
    value.delete(0, END)
    value.insert(0, initial + str(numbers))


def val_clear():
    value.delete(0, END)


def add_val():
    initial = float(value.get())
    global f_val
    global action
    action = "addition"
    f_val = initial
    value.delete(0, END)


def diff_val():
    initial = float(value.get())
    global f_val
    global action
    action = "difference"
    f_val = initial
    value.delete(0, END)


def product_val():
    initial = float(value.get())
    global f_val
    global action
    action = "multiplication"
    f_val = initial
    value.delete(0, END)


def divide_val():
    initial = float(value.get())
    global f_val
    global action
    action = "division"
    f_val = initial
    value.delete(0, END)


def percent_val():
    initial = float(value.get())
    global f_val
    global action
    action = "percentage"
    f_val = initial
    value.delete(0, END)


def res_val():
    secondary = float(value.get())
    value.delete(0, END)
    if action == 'addition':
        value.insert(0, str(f_val + secondary))
    elif action == 'difference':
        value.insert(0, str(f_val - secondary))
    elif action == 'multiplication':
        value.insert(0, str(f_val * secondary))
    elif action == 'division':
        value.insert(0, str(f_val / secondary))
    elif action == 'percentage':
        value.insert(0, str((f_val / secondary)*100))


value = Entry(root, width=20)
key1 = Button(root, text="1", padx=25, pady=20, command=lambda: entries(1), borderwidth=5)
key2 = Button(root, text="2", padx=25, pady=20, command=lambda: entries(2), borderwidth=5)
key3 = Button(root, text="3", padx=25, pady=20, command=lambda: entries(3), borderwidth=5)
key4 = Button(root, text="4", padx=25, pady=20, command=lambda: entries(4), borderwidth=5)
key5 = Button(root, text="5", padx=25, pady=20, command=lambda: entries(5), borderwidth=5)
key6 = Button(root, text="6", padx=25, pady=20, command=lambda: entries(6), borderwidth=5)
key7 = Button(root, text="7", padx=25, pady=20, command=lambda: entries(7), borderwidth=5)
key8 = Button(root, text="8", padx=25, pady=20, command=lambda: entries(8), borderwidth=5)
key9 = Button(root, text="9", padx=25, pady=20, command=lambda: entries(9), borderwidth=5)
key0 = Button(root, text="0", padx=25, pady=20, command=lambda: entries(0), borderwidth=5)
decimal = Button(root, text=".", padx=28.45, pady=20, command=lambda: entries('.'), borderwidth=5)
clear = Button(root, text="CLEAR", padx=39, pady=20, command=val_clear, bg='light grey', borderwidth=5)
add = Button(root, text="+", padx=28, pady=20, bg='light grey', command=add_val, borderwidth=5)
diff = Button(root, text="-", padx=32, pady=20, bg='light grey', command=diff_val, borderwidth=5)
product = Button(root, text="*", padx=25, pady=20, bg='light grey', command=product_val, borderwidth=5)
divide = Button(root, text="/", padx=27, pady=20, bg='light grey', command=divide_val, borderwidth=5)
percent = Button(root, text="%", padx=25, pady=20, bg='light grey', command=percent_val, borderwidth=5)
equals = Button(root, text='=', padx=25, pady=67, bg='light grey', command=res_val, borderwidth=5)
value.insert(0, "0")

key1['font'] = size
key2['font'] = size
key3['font'] = size
key4['font'] = size
key5['font'] = size
key6['font'] = size
key7['font'] = size
key8['font'] = size
key9['font'] = size
key0['font'] = size
decimal['font'] = size
clear['font'] = size
add['font'] = size
diff['font'] = size
product['font'] = size
divide['font'] = size
percent['font'] = size
equals['font'] = size
value['font'] = size

value.grid(row=0, column=0, columnspan=5, padx=20, pady=20)
key1.grid(row=1, column=0)
key2.grid(row=1, column=1)
key3.grid(row=1, column=2)
key4.grid(row=2, column=0)
key5.grid(row=2, column=1)
key6.grid(row=2, column=2)
key7.grid(row=3, column=0)
key8.grid(row=3, column=1)
key9.grid(row=3, column=2)
key0.grid(row=4, column=0)
decimal.grid(row=4, column=1)
clear.grid(row=4, column=2, columnspan=2)
add.grid(row=1, column=3)
diff.grid(row=2, column=3)
product.grid(row=1, column=4)
divide.grid(row=2, column=4)
percent.grid(row=3, column=3)
equals.grid(row=3, column=4, rowspan=2)

root.mainloop()
