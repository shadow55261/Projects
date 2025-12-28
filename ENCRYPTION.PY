# مشروع التشفير و فك التشفير على طريقة إبراهيم عادل
import string 
def encryption(message,numbers):
    letters=string.ascii_lowercase
    thread=string.digits
    decoding=""
    for dismantling in message:
        if dismantling.lower() in letters:
            location = letters.index(dismantling.lower())
            caracter = (location + numbers) %26
            code = letters[caracter]
            if dismantling.isupper():
                code = code.upper()
            decoding += code
        elif dismantling in thread:
            location=thread.index(dismantling)
            caracter=(location + numbers) % 10
            decoding+=thread[caracter]
        else:
            decoding+=dismantling
    print(f""" 
          Cryptography
          **********
          {decoding}
          **********
          """)   
text=input("Enter numbers or a message to encrypt:")
number=int(input("Enter the encryption key:"))   
encryption(message=text , numbers=number)
def code_key(lyrics,key):
    alphabetical=string.ascii_lowercase
    thread=string.digits
    solve=""
    for caesar in lyrics:
        if caesar.lower() in alphabetical:
            element = alphabetical.index(caesar.lower())
            engine = (element - key) %26
            output = alphabetical[engine]
            if caesar.isupper():
                output = output.upper()
            solve += output
        elif caesar in thread:
            element=thread.index(caesar)
            engine=(element - key) % 10
            solve+=thread[engine]
        else:
            solve+=caesar
    print(f"""
          Decoding
          *******
          {solve}
          *******
          """)    
unlocking=input("Enter the encrypted word to decrypt:")
keys=int(input("Enter the decryption key:"))
code_key(unlocking,keys)
