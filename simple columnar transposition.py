def simplecypher():
    msg = input("Masukkan teks: ").upper()

    key = input("Maukkan kata kunci: ").upper()
    backup = key

    urut_list = pengurutan(key)

    for i in range(len(key)):
        print(key[i], end=" ")

    print()
    for i in range(len(key)):
        print(str(urut_list[i]), end=" ")

    print()
    print("-------------------------")

    check_text = len(msg) % len(key)

    dummy_char = len(key) - check_text

    if check_text != 0:
        for i in range(dummy_char):
            msg += "."

    jml_baris = int(len(msg) / len(key))

    # print teks
    arr = [[0] * len(key) for i in range(jml_baris)]
    z = 0
    for i in range(jml_baris):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1

    for i in range(jml_baris):
        for j in range(len(key)):
            print(arr[i][j], end=" ")
        print()

    num_loc = urut_number(key, urut_list)

    print(len(backup))
    print(jml_baris)

    # cipher
    cipher_text = ""
    k = 0
    for i in range(len(backup)):
        if k == len(backup):
            break
        else:
            d = int(num_loc[k])  # kolom

        for j in range(jml_baris):
            if arr[j][d] == ".":
                cipher_text += ""
            else:
                cipher_text += arr[j][d]

        k += 1

    print(k)
    cipher_text.replace(".", "")
    print("Hasil Enkripsi :", (cipher_text))
    print("batas")

def deskripsi():
    msg = input("Masukkan hasil Enkripsi : ").upper()
    key = input("Masukkan kunci: ").upper()
    backup = key
    urut_list = pengurutan(key)
    print(urut_list)
    pembulatan = (len(msg) / len(key))
    jml_baris = int(pembulatan)
    if pembulatan>jml_baris:
        jml_baris+=1

    print(jml_baris)

    check_text = len(msg) % len(key)
    print(check_text)
    dummy_char = len(key) - check_text
    if check_text != 0:
        for i in range(dummy_char):
            msg += " "

    num_loc = urut_number(key, urut_list)
    print(num_loc)

    arr = [[0] * len(key) for i in range(jml_baris)]
    print(arr)
    # decipher
    deskripsi = ""
    k = 0
    x = 0


    for i in range(len(backup)):
        d = 0
        if k == len(backup):
            k = 0
        else:
            d: int = int(num_loc[k])
        for j in range(jml_baris):
            arr[j][d] = msg[x]
            x += 1
        if x == len(msg):
            break
        k += 1
    print()

    for i in range(jml_baris):
        for j in range(len(key)):
            deskripsi += str(arr[i][j])

    print("Hasil Deskripsi: " + deskripsi)

def urut_number(key, urut_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if urut_list[j] == i:
                num_loc += str(j)
    return num_loc


def pengurutan(key):
    data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    urut_list = list(range(len(key)))

    init = 0
    for i in range(len(data)):
        for j in range(len(key)):
            if data[i] == key[j]:
                init += 1
                urut_list[j] = init

    return urut_list


if __name__ == "__main__":

    print("PILIH SALAH SATU")
    print("1. Enkripsi")
    print("2. Dekripsi")

    pilihan = int(input("Masukkan pilihan"))
    print(pilihan)
    if pilihan == 1:
        simplecypher()
    else:
        deskripsi()
