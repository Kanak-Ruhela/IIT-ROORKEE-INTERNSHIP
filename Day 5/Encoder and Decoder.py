def caesar(text, shift, mode):
    if mode == "decode":
        shift = -shift
    result = ""
    for letter in text.lower():
        if letter.isalpha():
            result += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            result += letter  
    return result
secret = caesar("hello world", 3, "encode")
print("Encoded:", secret)
print("Decoded:", caesar(secret, 3, "decode"))

