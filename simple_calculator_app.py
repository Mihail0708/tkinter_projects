from tkinter import *

root = Tk()
root.title('Simple Calculator')

entry_widget = Entry(root, width=35, borderwidth=5)
entry_widget.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_equal():
    second_number = entry_widget.get()
    entry_widget.delete(0, END)
    if math == 'addition':
        entry_widget.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        entry_widget.insert(0, f_num - int(second_number))
    elif math == 'division':
        entry_widget.insert(0, f_num / int(second_number))
    elif math == 'multiplication':
        entry_widget.insert(0, f_num * int(second_number))


def button_add():
    first_number = entry_widget.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry_widget.delete(0, END)


def button_clear():
    entry_widget.delete(0, END)


def button_click(number):
    current = entry_widget.get()
    entry_widget.delete(0, END)
    entry_widget.insert(0, current + str(number))


def button_subtract():
    first_number = entry_widget.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry_widget.delete(0, END)


def button_divide():
    first_number = entry_widget.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry_widget.delete(0, END)


def button_multiply():
    first_number = entry_widget.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry_widget.delete(0, END)


button_one = Button(root, text='1', padx=30, pady=20, borderwidth=5, command=lambda: button_click(1))
button_two = Button(root, text='2', padx=30, pady=20, borderwidth=5, command=lambda: button_click(2))
button_three = Button(root, text='3', padx=30, pady=20, borderwidth=5, command=lambda: button_click(3))
button_four = Button(root, text='4', padx=30, pady=20, borderwidth=5, command=lambda: button_click(4))
button_five = Button(root, text='5', padx=30, pady=20, borderwidth=5, command=lambda: button_click(5))
button_six = Button(root, text='6', padx=30, pady=20, borderwidth=5, command=lambda: button_click(6))
button_seven = Button(root, text='7', padx=30, pady=20, borderwidth=5, command=lambda: button_click(7))
button_eight = Button(root, text='8', padx=30, pady=20, borderwidth=5, command=lambda: button_click(8))
button_nine = Button(root, text='9', padx=30, pady=20, borderwidth=5, command=lambda: button_click(9))
button_zero = Button(root, text='0', padx=30, pady=20, borderwidth=5, command=lambda: button_click(0))
button_add = Button(root, text='+', padx=39, pady=20, borderwidth=5, command=button_add)
button_equal = Button(root, text='=', padx=120, pady=20, borderwidth=5, command=button_equal)
button_clear = Button(root, text='C', padx=39, pady=20, borderwidth=5, command=button_clear)
button_subtract = Button(root, text='-', padx=40, pady=20, borderwidth=5, command=button_subtract)
button_multiply = Button(root, text='*', padx=40, pady=20, borderwidth=5, command=button_multiply)
button_divide = Button(root, text='/', padx=40, pady=20, borderwidth=5, command=button_divide)

# put buttons on screen
button_one.grid(row=3, column=0)
button_two.grid(row=3, column=1)
button_three.grid(row=3, column=2)

button_four.grid(row=2, column=0)
button_five.grid(row=2, column=1)
button_six.grid(row=2, column=2)

button_seven.grid(row=1, column=0)
button_eight.grid(row=1, column=1)
button_nine.grid(row=1, column=2)

button_zero.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_clear.grid(row=4, column=2)
button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)
button_equal.grid(row=6, column=0, columnspan=3)


root.mainloop()
