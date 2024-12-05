from pathlib import Path
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path('./assets')

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

""" Window utama """
window = Tk()
window.geometry("443x527")
window.title("Integral Calculator")
window.configure(bg = "#FFFFFF")

# inisialisasi variabel untuk batas atas, batas bawah, input, dan hasil
b = IntVar() # batas atas (upper limit)
a = IntVar() # batas bawah (lower limit)
x = IntVar() # input
y = IntVar() # hasil

""" Membuat frame untuk masing2 halaman """
definiteIntegralPage = Frame(window)
indefiniteIntegralPage = Frame(window)

definiteIntegralPageCanvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 527,
    width = 443,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# 'Hello Integralian' text
definiteIntegralPageCanvas.place(x = 0, y = 0)
definiteIntegralPageCanvas.create_text(
    23.0,
    22.0,
    anchor="nw",
    text="Hello, Integralian!",
    fill="#000000",
    font=("Consolas Bold", 16 * -1)
)

# 'Integral calculator' text
definiteIntegralPageCanvas.create_text(
    23.0,
    48.0,
    anchor="nw",
    text="Integral Calculator",
    fill="#000000",
    font=("Consolas Bold", 24 * -1)
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
 
 
# '. . .' text
res_text = ". . ." if y.get() == 0 else y.get() 
definiteIntegralPageCanvas.create_text(
    206.0,
    450.0,
    anchor="nw",
    text=res_text,
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

# Property tombol 'Indefinite Integral'
button_image_1 = PhotoImage(file=relative_to_assets("indef_integral_button.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: indefiniteIntegralPage.tkraise(),
    relief="flat"
)
button_1.place(
    x=227.0,
    y=131.0,
    width=193.0,
    height=45.0
)

# Property tombol 'Definite Integral'
button_image_2 = PhotoImage(
    file=relative_to_assets("defin_integral_button.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: definiteIntegralPage.tkraise(),
    relief="flat"
)
button_2.place(
    x=23.0,
    y=131.0,
    width=193.0,
    height=45.0
)

#  Property tombol 'Calculate'
button_image_3 = PhotoImage(
    file=relative_to_assets("calculate_button.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(f"upper limit: {b.get()}\nlower limit: {a.get()}\ninput: {x.get()}"),
    relief="flat",
)
button_3.place(
    x=23.0,
    y=322.0,
    width=397.0,
    height=45.0
)

# Property simbol integral '∫'
image_image_1 = PhotoImage(
    file=relative_to_assets("integrate_symbol.png"))
image_1 = definiteIntegralPageCanvas.create_image(
    49.0,
    248.0,
    image=image_image_1
)

# Property text field untuk batas atas
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_1 = definiteIntegralPageCanvas.create_image(
    99.0,
    217.0,
    image=entry_image_1
)
batas_atas = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=b
)
batas_atas.place(
    x=88.0,
    y=202.0,
    width=22.0,
    height=28.0
)

# Property text field untuk batas bawah
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = definiteIntegralPageCanvas.create_image(
    99.0,
    273.0,
    image=entry_image_2
)
batas_bawah = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=a
    
)
batas_bawah.place(
    x=88.0,
    y=258.0,
    width=22.0,
    height=28.0
)

# Property text field untuk angka dari user input
input_angka_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
input_angka_bg = definiteIntegralPageCanvas.create_image(
    282.0,
    251.0,
    image=input_angka_image
)
input_angka = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=x
)
input_angka.place(
    x=148.0,
    y=229.0,
    width=268.0,
    height=42.0
)

definiteIntegralPage.tkraise()
window.resizable(False, False)
window.mainloop()