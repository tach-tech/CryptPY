from cryptography.fernet import Fernet
import os

def defkey():
    key = Fernet.generate_key()
    with open("key.txt", 'wb') as file:
        file.write(key)

def crypt(key, path):
    fernet = Fernet(key)
    with open(path, 'rb') as file:
        original = file.read()      
    encrypted = fernet.encrypt(original)
    with open("crypt_file.txt", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(key, path):
    fernet = Fernet(key)    
    with open(path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('crypt_file.txt', 'wb') as dec_file:
        dec_file.write(decrypted)

while True:

    os.system('cls')
    input("{~ CryptPY [Fernet] ~}\n \nPress Any Key ... ")
    os.system('cls')

    choice = input("CryptPY [Fernet]\n \nGet a Key: getkey\nCrypting a file: crypting/crypt\nDecrypting a file: decrypting/decrypt\n \n => ")
    if choice.lower() == "getkey":
        os.system('cls')
        defkey()
        input(f'Your key is on key.txt on CryptPY folder\n \nPress Any Key ...')
        os.system('cls')
    elif choice.lower() in ("crypting", "crypt"):
        os.system('cls')
        filepath = input("CryptPY [Fernet]\n \nComplete file path\n \n => ")
        os.system('cls')
        my_key = str(input("Your Fernet Key\n \n => "))
        os.system('cls')
        crypt(my_key, filepath)
        input("CryptPY [Fernet]\n \nCrypting finish !\n \nPress Any Key ...")
        os.system('cls')
    elif choice.lower() in ("decrypting", "decrypt"):
        os.system('cls')
        filepath = input("CryptPY [Fernet]\n \nComplete file path ?\n \n => ")
        os.system('cls')
        my_key = str(input("Your Fernet Key\n \n => "))
        os.system('cls')
        decrypt(my_key, filepath)
        input("CryptPY [Fernet]\n \nDecrypting finish !\n \nPress Any Key ...")
        os.system('cls')
    elif choice.lower() in ("quit", "exit"):
        os.system('cls')
        input("CryptPY [Fernet]\n \nPress Any Key To Quit...")
        break

        