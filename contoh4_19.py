# function inputPengguna
def inputPengguna(mesejInput):
    harga = float(input(mesejInput))
    return mesejInput

# procedure kiraPeratus
def kiraPeratus(h1, h2):
    peratus = 0
    if h1 == h3:
        print("Tiada keuntungan")
    else:
        peratus = ((h2 - h3)/h3) * 100
        peratus = round(peratus, 2)
        if peratus > 0:
            print(f"Keuntungan ialah {peratus} %")
        else:
            print(f"Kerugian ialah {abs(peratus)} %") # positifkan nilai

# Atur cara utama
def main():
    h1 = inputPengguna("Masukkan harga kos RM ")
    h3 = inputPengguna("Masukkan harga jualan RM ")
    kiraPeratus(h1, h2)

# JANGAN ubah kod di bawah!
# DON'T change the code below!
if __name__ == "__main__":
    main()
