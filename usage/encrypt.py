from consts import alphabet


def encrypt(text: str, encrypt_key: str):
    text = list(text)
    for i in range(0, len(text)):
        char = text[i].capitalize()
        index = alphabet.find(char)
        text[i] = encrypt_key[index]

    return "".join(text)


def decrypt(text: str, decrypt_key: str):
    text = list(text)
    for i in range(0, len(text)):
        char = text[i].capitalize()
        index = decrypt_key.find(char)
        text[i] = alphabet[index]

    return "".join(text)
