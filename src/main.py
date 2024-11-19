import tkinter
from calc import postfix, calculate

def st(s: str, c: str) -> str:
    return s + c

def on_button_plus():
    global s
    global op
    if s[-1] in op or len(s) > 15:
        s = s[:-1]
    s = st(s, "+")
    label2.config(text=s)

def on_button_minus():
    global s
    global op
    if s[-1] in op or len(s) > 15:
        s = s[:-1]
    s = st(s, "-")
    label2.config(text=s)

def on_button_division():
    global s
    global op
    if s[-1] in op or len(s) > 15:
        s = s[:-1]
    s = st(s, "/")
    label2.config(text=s)

def on_button_mult():
    global s
    global op
    if s[-1] in op or len(s) > 15:
        s = s[:-1]
    s = st(s, "x")
    label2.config(text=s)

def on_button_equal():
    global s
    s = calculate(postfix(s))
    label2.config(text=s)

def on_button_c():
    global s
    s = ""
    label2.config(text=s)

def on_button_nine():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '9')
        label2.config(text=s)

def on_button_eight():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '8')
        label2.config(text=s)

def on_button_seven():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '7')
        label2.config(text=s)

def on_button_six():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '6')
        label2.config(text=s)

def on_button_five():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '5')
        label2.config(text=s)

def on_button_four():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '4')
        label2.config(text=s)

def on_button_three():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '3')
        label2.config(text=s)

def on_button_two():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '2')
        label2.config(text=s)

def on_button_one():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '1')
        label2.config(text=s)

def on_button_zero():
    global s
    if len(s) > 15:
        pass
    else:
        s = st(s, '0')
        label2.config(text=s)

s = ""
op = {'+', '-', '/', 'x'}
window = tkinter.Tk()
window.title("Python Calculator")
window.resizable(False, False)
window.geometry("400x400")

label2 = tkinter.Label(window, text=s, font=('Arial', 20))
label2.pack(padx=30, pady=30)

button_frame = tkinter.Frame(window)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)

button_frame.rowconfigure(0, weight=1)
button_frame.rowconfigure(1, weight=1)
button_frame.rowconfigure(2, weight=1)
button_frame.rowconfigure(3, weight=1)

plus = tkinter.Button(
    button_frame,
    text="+",
    command=on_button_plus
)
plus.grid(row=0, column=3, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

nine = tkinter.Button(
    button_frame,
    text="9",
    command=on_button_nine
)
nine.grid(row=0, column=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

eight = tkinter.Button(
    button_frame,
    text="8",
    command=on_button_eight
)
eight.grid(row=0, column=1, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

seven = tkinter.Button(
    button_frame,
    text="7",
    command=on_button_seven
)
seven.grid(row=0, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

minus = tkinter.Button(
    button_frame,
    text="-",
    command=on_button_minus
)
minus.grid(row=1, column=3, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

six = tkinter.Button(
    button_frame,
    text="6",
    command=on_button_six
)
six.grid(row=1, column=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

five = tkinter.Button(
    button_frame,
    text="5",
    command=on_button_five
)
five.grid(row=1, column=1, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

four = tkinter.Button(
    button_frame,
    text="4",
    command=on_button_four
)
four.grid(row=1, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

division = tkinter.Button(
    button_frame,
    text="/",
    command=on_button_division
)
division.grid(row=2, column=3, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

three = tkinter.Button(
    button_frame,
    text="3",
    command=on_button_three
)
three.grid(row=2, column=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

two = tkinter.Button(
    button_frame,
    text="2",
    command=on_button_two
)
two.grid(row=2, column=1, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

one = tkinter.Button(
    button_frame,
    text="1",
    command=on_button_one
)
one.grid(row=2, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

mult = tkinter.Button(
    button_frame,
    text="x",
    command=on_button_mult
)
mult.grid(row=3, column=3, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

equal = tkinter.Button(
    button_frame,
    text="=",
    command=on_button_equal
)
equal.grid(row=3, column=2, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

c = tkinter.Button(
    button_frame,
    text="C",
    command=on_button_c
)
c.grid(row=3, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

zero = tkinter.Button(
    button_frame,
    text="0",
    command=on_button_zero
)
zero.grid(row=3, column=1, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

button_frame.pack(fill=tkinter.BOTH, expand=True)

window.mainloop()