from sympy import symbols, integrate, sympify

x = symbols("x")
print("---Kalkulator Integral---")
print("Ketik 'Start' untuk memulai program, 'Exit' untuk keluar program.")

home = input("> ").capitalize()

if home == "Start":
    
    while True:

        print("---Kalkulator Integral---")
        print("---Pilih menu---\n1. Integral Tak Tentu\n2. Integral Tentu")

        pilihan = input("> ")

        if pilihan == "1":
            print("Integral Tak Tentu")
            soal = input("Masukkan soal: ")
            soalFix = sympify(soal)
            
            hasil1 = integrate(soalFix, x)
            print(f"Jawaban = {hasil1}")

        elif pilihan == "2":
            print("Integral Tentu")
            soal = input("Masukkan soal: ")
            soalFix = sympify(soal)

            a = float(input("Masukkan batas atas: "))
            b = float(input("Masukkan batas bawah: "))

            hasil2 = integrate(soalFix, (x,a,b))
            print(f"Jawaban = {hasil2}")
        
        elif pilihan == 0:
            print("Thank you, see you again!")
        
        else:
            print("Unknown command! Pilih sesuai menu!")
else:
    print("Thank you, see you again!")
