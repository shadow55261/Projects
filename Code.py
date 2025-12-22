import string
characters=input("Enter the characters to be encrypted:")
number=int(input("Enter the number of encryption steps:"))
def encryption(word,encryption):
    characters=string.ascii_lowercase
    capital_letter=string.ascii_uppercase
    cryptography=""
    for x in word:
        if x in characters:
            location=characters.index(x)
            rest=(location+encryption)%26
            cryptography+=characters[rest]
        elif x in capital_letter:
            location=capital_letter.index(x)
            rest=(location+encryption)%26
            cryptography+=capital_letter[rest]
        else:
            cryptography+=x
    print(f"""
          Encryption🛄
          **************
          {cryptography}
          **************
          """)
encryption(characters, number)
entrance=input("Enter the message to decrypt it:")
negative=int(input("Enter the encryption key"))
def decoding(message,retreat):
    small=string.ascii_lowercase
    captl=string.ascii_uppercase
    uncover_secret=""
    for slicing_letter in message:
        if slicing_letter in small:
            storage=small.index(slicing_letter)
            remaining=(storage-retreat)%26
            uncover_secret+=small[remaining]
        elif slicing_letter in captl:
            storage=captl.index(slicing_letter)
            remaining=(storage-retreat)%26
            uncover_secret+=captl[remaining]
        else:
            uncover_secret+=slicing_letter
    print(f"""
          The encryption has
           been decrypted 🛅
          ****************
          {uncover_secret}
          ****************
          """)
decoding(message=entrance,retreat=negative)