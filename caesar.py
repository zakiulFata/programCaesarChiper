def enkripsi(plain_text, shift):
    chipher_text = ""
    for char in plain_text:
        # Huruf besar
        if char.isupper():
            chipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Huruf kecil
        elif char.islower():
            chipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            chipher_text += char
    return chipher_text

def deskripsi(chipher_text, shift):
    plain_text = ""
    for char in chipher_text:
        # Huruf besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Huruf kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def main():
    print("Selamat datang di program enkripsi dan deskripsi text!")
    plain_text = input("Masukkan nilai text asli (plaintext): ")
    shift = int(input("Masukkan nilai pergeseran (1-25): "))

    # Enkripsi
    chipher_text = enkripsi(plain_text, shift)
    print("Data yang dienkripsi:", chipher_text)

    # Deskripsi
    deskripsi_text = deskripsi(chipher_text, shift)
    print("Data yang dideskripsi:", deskripsi_text)

main()