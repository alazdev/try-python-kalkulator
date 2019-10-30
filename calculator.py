def tambah(x, y):
    hasil = x + y
    a = str(x)
    b = str(y)
    c = str(hasil)
    print("\t" + a + " + " + b + " = " + c)
    proses()
def kurang(x, y):
    hasil = x - y
    a = str(x)
    b = str(y)
    c = str(hasil)
    print("\t" + a + " - " + b + " = " + c)
    proses()
def kali(x, y):
    hasil = x * y
    a = str(x)
    b = str(y)
    c = str(hasil)
    print("\t" + a + " * " + b + " = " + c)
    proses()
def bagi(x, y):
    hasil = x / y
    a = str(x)
    b = str(y)
    c = str(hasil)
    print("\t" + a + " / " + b + " = " + c)
    proses()
def proses():
    try:
        print("===================================================")
        pertama = input("Masukkan angka pertama : ")
        kedua = input("Masukkan angka kedua : ")
        per = int(pertama)
        ked = int(kedua)
        ope = input("operasi<+, -, *, /> : ")
        if ope == "+":
            tambah(per, ked)
        elif ope == "-":
            kurang(per, ked)
        elif ope == "*" or ope == "x":
            kali(per, ked)
        elif ope == "/" or ope == ":":
            bagi(per, ked)
        else:
            print("\tMasalah!!!")
            input("<enter>For EXIT")
    except:
        print("Terjadi Masalah!!")
        input("<enter>")
            
proses()