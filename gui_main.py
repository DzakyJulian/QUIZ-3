from pathlib import Path
from tkinter import *
from sympy import symbols, integrate, sstr
from sympy.parsing.sympy_parser import parse_expr
from sympy.integrals.manualintegrate import integral_steps
# from step_by_step import steps_explanation

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path('./assets')

# Fungsi untuk mengakses asset-asset yang ada
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Fungsi untuk mengupdate hasil setelah mengklik tombol 'Calculate'
def update_result():
    mainFrameCanvas.itemconfig(res_display, text=result.get())

# Fungsi untuk mengubah hasil menjadi lebih rapih
def pretty_integral_result(integration_result: str):
    formatted_result = integration_result.replace('**', '^')
    formatted_result = formatted_result.replace("*", "")
    return formatted_result

# Fungsi untuk membuka jendela baru untuk melihat langkah-langkah integrasi
def show_steps_window():
    newWindow = Toplevel(mainFrame)
    newWindow.title("Step by step")

    # properti text langkah2
    steps_text = Text(newWindow, font="Consolas 12")
    steps_text.insert(INSERT, result_steps.get())
    steps_text.pack()


# Fungsi menghitung integral yang diinput oleh user
def calculate_integral():
    x = symbols('x')
    
    if current_state.get() == "definite":
        parsed_input = parse_expr(q_input.get(), transformations="all")

        integration_result = str(integrate(parsed_input, (x, a.get(), b.get())))
        step_by_step = sstr(integral_steps(parsed_input, x))
        
        result_steps.set(step_by_step)
        result.set(pretty_integral_result(integration_result))
        update_result()
    else:
        parsed_input = parse_expr(q_input.get(), transformations="all")

        integration_result = str(integrate(parsed_input, x))
        step_by_step = sstr(integral_steps(parsed_input, x))
        
        result_steps.set(step_by_step)
        result.set(pretty_integral_result(integration_result) + "+ C")
        update_result()

# Initialize main window
window = Tk()
window.geometry("443x530")
window.title("Integral Calculator")
window.configure(bg="#FFFFFF")

# Initialize variables for the upper limit, lower limit, input, step by step, and result
b = IntVar()  # upper limit
a = IntVar()  # lower limit
x = symbols("x") # x symbol for sympy integration
q_input = StringVar()  # input soal
result_steps = StringVar() # langkah integrasi
result = StringVar()  # hasil

# Frames for pages
mainFrame = Frame(window, bg="#FFFFFF")
mainFrame.place(x=0, y=0, width=443, height=527)

# Initialize current state
current_state = StringVar(mainFrame, "definite")

mainFrameCanvas = Canvas(
    mainFrame,
    bg="#FFFFFF",
    width=443,
    height=527,
)
mainFrameCanvas.place(x=0, y=0)

# 'Hello Integralian' text
mainFrameCanvas.create_text(
    23.0,
    22.0,
    anchor="nw", # text-align
    text="Hello, Integralian!",
    fill="#000000",
    font=("Consolas Bold", 12),
)

# 'Integral calculator' text
mainFrameCanvas.create_text(
    23.0,
    48.0,
    anchor="nw",
    text="Integral Calculator",
    fill="#000000",
    font=("Consolas Bold", 18),
)

# 'Choose one' text
mainFrameCanvas.create_text(
    23.0,
    104.0,
    anchor="nw",
    text="Choose one:",
    fill="#000000",
    font=("Inter", 12)
)

# 'Result' text
mainFrameCanvas.create_text(
    23.0,
    388.0,
    anchor="nw",
    text="Result: ",
    fill="#000000",
    font=("Inter", 12)
)

# '. . .' result text
res_display = mainFrameCanvas.create_text(
    23.0,
    440.0,
    text=result.get(),
    anchor="nw",
    fill="#000000",
    font=("Inter Bold", 18)
)

""" Button and Entries """
# Integral Symbol
integral_symbol_image = PhotoImage(file=relative_to_assets("integrate_symbol.png"))
integral_symbol = mainFrameCanvas.create_image(
    49.0,
    248.0,
    image=integral_symbol_image
)


# Button: Indefinite Integral
indef_integral_button_image = PhotoImage(file=relative_to_assets("indef_integral_button.png"))
indef_integral_button = Button(
    image=indef_integral_button_image,
    borderwidth=0,
    command=lambda: (
        current_state.set("indefinite"),
        upper_limit_entry.place_forget(),
        lower_limit_entry.place_forget(),
        mainFrameCanvas.coords(integral_symbol, 49, 248),
        mainFrameCanvas.coords(integral_symbol, 100, 248),
        mainFrameCanvas.itemconfig(upper_limit_entry_bg, state="hidden"),
        mainFrameCanvas.itemconfig(lower_limit_entry_bg, state="hidden")
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
    image=def_integral_button_image,
    borderwidth=0,
    command=lambda: (
        current_state.set("definite"),
        mainFrameCanvas.coords(integral_symbol, 49, 248),
        mainFrameCanvas.itemconfig(upper_limit_entry_bg, state="normal"),
        mainFrameCanvas.itemconfig(lower_limit_entry_bg, state="normal"),
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
    image=calculate_button_image,
    borderwidth=0,
    command=lambda: calculate_integral(),
    relief="flat"
)
calculate_button.place(
    x=23.0,
    y=322.0,
    width=397.0,
    height=45.0
)

# Upper Limit Entry
upper_limit_entry_image = PhotoImage(file=relative_to_assets("entry_2.png"))
upper_limit_entry_bg = mainFrameCanvas.create_image(
    99.0,
    217.0,
    image=upper_limit_entry_image
)
upper_limit_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    textvariable=b,
    font="Inter, 10"
)
upper_limit_entry.place(
    x = 88.0,
    y = 203.0,
    width=22.0,
    height=28.0
)

# Lower Limit Entry
lower_limit_entry_image = PhotoImage(file=relative_to_assets("entry_2.png"))
lower_limit_entry_bg = mainFrameCanvas.create_image(
    99.0,
    273.0,
    image=lower_limit_entry_image
)
lower_limit_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    textvariable=a,
    font="Inter, 10"
)
lower_limit_entry.place(
    x = 88.0,
    y = 259.0,
    width=22.0,
    height=28.0
)

# Input Entry
num_entry_image = PhotoImage(file=relative_to_assets("entry_1.png"))
num_entry_bg = mainFrameCanvas.create_image(
    282.0,
    251.0,
    image=num_entry_image
)
num_entry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    textvariable=q_input,
    font="Inter, 12"
)
num_entry.place(
    x=160.0,
    y=230.0,
    width=258.0,
    height=42.0
)

# Step by Step Button
show_steps_button = Button(
    text="Show step by step",
    command=lambda: show_steps_window()
)
show_steps_button.place(
    x=23.0,
    y=495.0,
    width=397.0,
    height=25.0
)

# Finalize the window
window.resizable(False, False)
window.mainloop()