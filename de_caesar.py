#Pembuatan Fungsi Enkripsi CaesarChiper
def dekripsi(teks, p):
    hasil = ""
    # mengurai plain text per huruf
    for i in range(len(teks)):
        char = teks[i]
    # perhatikan perhitungan antara huruf besar dan kecil
        if (char.isupper()):
            hasil += chr((ord(char) - p - 65) % 26 + 65)
        else:
            hasil += chr((ord(char) - p - 97) % 26 + 97)
    print(hasil)
    return hasil
#================================================================

# Program Utama Pemanggil Fungsi
#================================================================

if __name__ == "__main__":
    teks=input("Masukkan Teks yang akan dienkripsi (HANYA HURUF): ")
    penggeser=int(input("Berapa pergeseran Huruf yang akan digunakan:"))
    print("Enkripsi : " + teks)
    print("Shift pattern : " + str(penggeser))
    print("Cipher : " + dekripsi(teks, penggeser))