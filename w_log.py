import time 
import os

time = time.strftime("%m/%d/%Y, %H:%M:%S")

if os.name == "nt":
    os_name = "Windows"
else:
    os_name = "Linux or Mac"

def wlog_cmd():

    with open("CryptPY\log.txt", "a") as f:
        f.write(f"\n \n[-] cmd program run on : {os_name}\n[-] At {time}")

def wlogkey_cmd(key):

    with open("CryptPY\log.txt", "a") as f:
        f.write(f"\n \n[+] Key : {key} \n[-] Delivered at : {time}")

def wlogcrypt_cmd(key):

    with open("CryptPY\log.txt", "a") as f:
        f.write(f"\n \n[+] Text crypted at {time} \n[+] With key : {key}")

def wlogdecrypt_cmd(key):

    with open("CryptPY\log.txt", "a") as f:
        f.write(f"\n \n[+] Text decrypted at {time} \n[+] With key : {key}")

def wlog_gui():

    with open("CryptPY\log.txt", "a") as f:
        f.write(f"\n \n[-] Gui program run on {os_name} \n[-] At {time}")

