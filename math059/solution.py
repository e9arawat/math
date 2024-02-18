"""
XOR Decryption
"""


def answer():
    """
    XOR Decryption
    """
    with open("0059_cipher.txt", "r", encoding="UTF-8") as f:
        data = [int(num) for num in f.read().split(",")]

    password_length = 3
    decoded_password = []

    for p in range(password_length):
        for ch in range(ord("a"), ord("z") + 1):

            dec = []
            for i in range(p, len(data), password_length):
                dec.append(chr(data[i] ^ ch))

            count = sum(1 for char in dec if not char.isalpha() and char != " ")

            if count / len(dec) < 0.1:
                decoded_password.append(ch)
                break

    decrypted = []
    for index, x in enumerate(data):
        decrypted.append(x ^ decoded_password[index % password_length])

    return sum(decrypted)


if __name__ == "__main__":
    print(answer())
