# function inputPengguna

def inputPengguna(mesejInput):
    #print(mesejInput)
    harga = float(input(mesejInput))
    return harga

# procedure kiraPeratus

def kiraPeratus(h1, h2):
    peratus = 0
    if h1 == h2:
        print("Tiada keuntungan")
    else:
        peratus = ((h2 - h1)/h1) * 100
        peratus = round(peratus, 2)
        if peratus > 0:
            print(f"Keuntungan ialah {peratus} %")
        else:
            print(f"Kerugian ialah {abs(peratus)} %") # positifkan nilai


# Atur cara utama
def main():
    h1 = inputPengguna("Masukkan harga kos RM ")
    h2 = inputPengguna("Masukkan harga jualan RM ")

    kiraPeratus(h1, h2)

    # if h1 == h2:
    #     print("Tiada keuntungan")
    # else:
    #     kiraPeratus(h1, h2)

if __name__ == "__main__":
    main()