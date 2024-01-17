from cryptography.fernet import Fernet
from pystyle import *
import time
import os
from w_log import wlog

white = Col.white
red = Col.light_red
blue = Col.light_blue
green = Col.light_green

def cryptPY():

    def defkey():
        key = Fernet.generate_key()
        with open("CryptPY\key.txt", 'wb') as file:
            file.write(key)
        wlog(key)

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
    
    def clear_ter():
        os.system('cls' if os.name == 'nt' else 'clear')

    while True:

        clear_ter()
        input(f"{red}~ CryptPY [Fernet] ~{blue}\n \nPress Any Key ... {white}")
        time.sleep(1.5)
        clear_ter()

        choice = input(f"{red}~ CryptPY [Fernet] ~{blue}\n \nGet a Key: getkey\nCrypting a file: crypting/crypt\nDecrypting a file: decrypting/decrypt\nExit: exit/quit\n \n => {white}")
        if choice.lower() == "getkey":
            clear_ter()
            defkey()
            input(f'{green}Your key is on key.txt on CryptPY folder\n \nPress Any Key ... {white}')
            clear_ter()
        elif choice.lower() in ("crypting", "crypt"):
            clear_ter()
            filepath = input(f"{red}~ CryptPY [Fernet] ~{blue}\n \nComplete file path\n \n => {white}")
            clear_ter()
            my_key = str(input(f"{green}Your Fernet Key\n \n => {white}"))
            clear_ter()
            crypt(my_key, filepath)
            input(f"{red}~ CryptPY [Fernet] ~{blue}\n \nCrypting finish !\n \nPress Any Key ... {white}")
            clear_ter()
        elif choice.lower() in ("decrypting", "decrypt"):
            clear_ter()
            filepath = input(f"{red}~ CryptPY [Fernet] ~{blue}\n \nComplete file path ?\n \n => {white}")
            clear_ter()
            my_key = str(input(f"{green}Your Fernet Key\n \n => {white}"))
            clear_ter()
            decrypt(my_key, filepath)
            input(f"{red}~ CryptPY [Fernet] ~{blue}\n \nDecrypting finish !\n \nPress Any Key ... {white}")
            clear_ter()
        elif choice.lower() in ("quit", "exit"):
            clear_ter()
            input(f"{red}~ CryptPY [Fernet] ~{blue}\n \nPress Any Key To Quit... {white}")
            break      