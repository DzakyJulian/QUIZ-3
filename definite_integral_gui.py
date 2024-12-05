from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, IntVar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Hanz\Development\Python\Exercise\matdas-py-integral\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# atur window size nya 443x527 dan bg color nya putih
window = Tk()
window.title("Integral Calculator")
window.geometry("443x527")
window.configure(bg = "#FFFFFF")

# inisialisasi variabel untuk batas atas, batas bawah, input, dan hasil
b = IntVar() # batas atas (upper limit)
a = IntVar() # batas bawah (lower limit)
x = IntVar() # input
y = IntVar() # hasil

# atur canvas nya juga pake settingan yang sama kaya settingan window
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 527,
    width = 443,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# 'Hello Integralian' text
canvas.place(x = 0, y = 0)
canvas.create_text(
    23.0,
    22.0,
    anchor="nw",
    text="Hello, Integralian!",
    fill="#000000",
    font=("Consolas Bold", 16 * -1)
)

# 'Integral calculator' text
canvas.create_text(
    23.0,
    48.0,
    anchor="nw",
    text="Integral Calculator",
    fill="#000000",
    font=("Consolas Bold", 24 * -1)
)

# 'Choose one' text
canvas.create_text(
    23.0,
    104.0,
    anchor="nw",
    text="Choose one:",
    fill="#000000",
    font=("Inter", 16 * -1)
)

# 'Result' text
canvas.create_text(
    23.0,
    388.0,
    anchor="nw",
    text="Result: ",
    fill="#000000",
    font=("Inter", 16 * -1)
)
 
 
res_text = ". . ." if y.get() == 0 else y.get() 
# '. . .' text
canvas.create_text(
    206.0,
    450.0,
    anchor="nw",
    text=res_text,
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

# Property tombol 'Indefinite Integral'
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
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
    file=relative_to_assets("button_3.png"))
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
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    49.0,
    248.0,
    image=image_image_1
)

# Property text field untuk batas atas
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
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
entry_bg_2 = canvas.create_image(
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
    file=relative_to_assets("entry_3.png"))
input_angka_bg = canvas.create_image(
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
window.resizable(False, False)
window.mainloop()
