from pathlib import Path
from tkinter import *
from sympy import symbols, integrate
from sympy.parsing.sympy_parser import parse_expr

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path('./assets')

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_result():
    definiteIntegralPageCanvas.itemconfig(res_display, text=result.get())

def calculate_integral():
    if current_state.get() == "definite":
        result.set(integrate(parse_expr(q_input.get(), transformations="all"), (x, a.get(), b.get())))
        update_result()
    else:
        result.set(f"{integrate(parse_expr(q_input.get(), transformations="all"), x)} + C")
        update_result()

# Initialize main window
window = Tk()
window.geometry("443x527")
window.title("Integral Calculator")
window.configure(bg="#FFFFFF")

# Initialize variables for the upper limit, lower limit, input, and result
b = IntVar()  # upper limit
a = IntVar()  # lower limit
x = symbols("x") # x symbol for sympy integration
q_input = StringVar()  # input soal
result = StringVar()  # hasil

# Frames for pages
definiteIntegralPage = Frame(window, bg="#FFFFFF")
definiteIntegralPage.place(x=0, y=0, width=443, height=527)

# Initialize current state
current_state = StringVar(definiteIntegralPage, "definite")

""" --------------- Definite Integral Page ----------------------- """
definiteIntegralPageCanvas = Canvas(
    definiteIntegralPage,
    bg="#FFFFFF",
    height=527,
    width=443,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
definiteIntegralPageCanvas.place(x=0, y=0)

# 'Hello Integralian' text
definiteIntegralPageCanvas.create_text(
    23.0,
    22.0,
    anchor="nw",
    text="Hello, Integralian!",
    fill="#000000",
    font=("Consolas Bold", 16 * -1),
)

# 'Integral calculator' text
definiteIntegralPageCanvas.create_text(
    23.0,
    48.0,
    anchor="nw",
    text="Integral Calculator",
    fill="#000000",
    font=("Consolas Bold", 24 * -1),
)

# 'Choose one' text
definiteIntegralPageCanvas.create_text(
    23.0,
    104.0,
    anchor="nw",
    text="Choose one:",
    fill="#000000",
    font=("Inter", 16 * -1)
)

# 'Result' text
definiteIntegralPageCanvas.create_text(
    23.0,
    388.0,
    anchor="nw",
    text="Result: ",
    fill="#000000",
    font=("Inter", 16 * -1)
)

# '. . .' result text
res_display = definiteIntegralPageCanvas.create_text(
    23.0,
    450.0,
    text=result.get(),
    anchor="nw",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

# Button: Indefinite Integral
indef_integral_button_image = PhotoImage(file=relative_to_assets("indef_integral_button.png"))
indef_integral_button = Button(
    master=definiteIntegralPage,
    image=indef_integral_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (
        current_state.set("indefinite"),
        upper_limit_entry.place_forget(),
        lower_limit_entry.place_forget(),
        definiteIntegralPageCanvas.coords(integral_symbol, 49, 248),
        definiteIntegralPageCanvas.coords(integral_symbol, 100, 248),
        definiteIntegralPageCanvas.itemconfig(upper_limit_entry_bg, state="hidden"),
        definiteIntegralPageCanvas.itemconfig(lower_limit_entry_bg, state="hidden")
    ),
    relief="flat"
)
indef_integral_button.place(
    x=227.0,
    y=131.0,
    width=193.0,
    height=45.0
)

# Button: Definite Integral
def_integral_button_image = PhotoImage(file=relative_to_assets("defin_integral_button.png"))
def_integral_button = Button(
    master=definiteIntegralPage,
    image=def_integral_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (
        current_state.set("definite"),
        definiteIntegralPageCanvas.coords(integral_symbol, 49, 248),
        definiteIntegralPageCanvas.itemconfig(upper_limit_entry_bg, state="normal"),
        definiteIntegralPageCanvas.itemconfig(lower_limit_entry_bg, state="normal"),
        upper_limit_entry.place(
            x = 88.0,
            y = 203.0,
            width=22.0,
            height=28.0
        ),
        lower_limit_entry.place(
            x = 88.0,
            y = 259.0,
            width=22.0,
            height=28.0
        ),
    ),
    relief="flat"
)
def_integral_button.place(
    x=23.0,
    y=131.0,
    width=193.0,
    height=45.0
)

# Button: Calculate
calculate_button_image = PhotoImage(file=relative_to_assets("calculate_button.png"))
calculate_button = Button(
    master=definiteIntegralPage,
    image=calculate_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: calculate_integral(),
    relief="flat"
)
calculate_button.place(
    x=23.0,
    y=322.0,
    width=397.0,
    height=45.0
)

# Integral Symbol
integral_symbol_image = PhotoImage(file=relative_to_assets("integrate_symbol.png"))
integral_symbol = definiteIntegralPageCanvas.create_image(
    49.0,
    248.0,
    image=integral_symbol_image
)

# Upper Limit Entry
upper_limit_entry_image = PhotoImage(file=relative_to_assets("entry_2.png"))
upper_limit_entry_bg = definiteIntegralPageCanvas.create_image(
    99.0,
    217.0,
    image=upper_limit_entry_image
)
upper_limit_entry = Entry(
    master=definiteIntegralPage,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=b
)
upper_limit_entry.place(
    x = 88.0,
    y = 203.0,
    width=22.0,
    height=28.0
)

# Lower Limit Entry
lower_limit_entry_image = PhotoImage(file=relative_to_assets("entry_2.png"))
lower_limit_entry_bg = definiteIntegralPageCanvas.create_image(
    99.0,
    273.0,
    image=lower_limit_entry_image
)
lower_limit_entry = Entry(
    master=definiteIntegralPage,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=a
)
lower_limit_entry.place(
    x = 88.0,
    y = 259.0,
    width=22.0,
    height=28.0
)

# Input Entry
num_entry_image = PhotoImage(file=relative_to_assets("entry_1.png"))
num_entry_bg = definiteIntegralPageCanvas.create_image(
    282.0,
    251.0,
    image=num_entry_image
)
num_entry = Entry(
    master=definiteIntegralPage,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=q_input
)
num_entry.place(
    x=160.0,
    y=230.0,
    width=258.0,
    height=42.0
)


# Finalize the window
window.resizable(False, False)
window.mainloop()