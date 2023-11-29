import tkinter as tk  # for GUI

# lust if button names and counter for one
elements = ['C', '%', '<x', '/', '7', '8', '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '00', '0', '.', '=']
c = 0


# functions for made button
def button_maker(value):
    global c
    btn_row = tk.Button(master=window, text=value, command=lambda: click(value))
    btn_row.grid(row=(c // 4 + 1), column=c % 4, sticky="nsew")
    c += 1


# functions for processing click events
def click(char):
    if char == 'C':
        # clear all
        display["text"] = ''
    elif char == '%':
        # divide by 100
        display["text"] = display["text"].replace('x', '*')
        if display["text"].isnumeric():
            display["text"] = str(eval(display["text"].lstrip('0')) / 100)
        else:
            display["text"] = 'Invalid Input'

    elif char == '<x':
        # backspace
        display["text"] = display["text"][:-1]
    elif char == '=':
        # result
        try:
            display["text"] = display["text"].replace('x', '*')
            display["text"] = display["text"].lstrip('0')
            # del empty option
            while not display["text"][-1].isnumeric():
                display["text"] = display["text"][:-1]
            display["text"] = str(eval(display["text"]))
            # del .0 ending
            if display["text"].endswith('.0'):
                display["text"] = display["text"][:-2]
            # cut long division part
            if len(display["text"].split('.')[1]) > 3:
                # rounding for 0.001
                display["text"] = display["text"].split('.')[0] + '.' + display["text"].split('.')[1][:4]

        except ZeroDivisionError:
            display["text"] = 'Zero Division Error'
    else:
        display["text"] = display["text"] + char


# create window
window = tk.Tk()

# create table of widgets
# noinspection PyTypeChecker
window.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
# noinspection PyTypeChecker
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

# create button value fot every cell
for element in elements:
    button_maker(element)
# display for calculator
display = tk.Label(master=window, text="")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# click register
window.mainloop()
