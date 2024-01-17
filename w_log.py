import time 

time = time.strftime("%m/%d/%Y, %H:%M:%S")

def wlog(key):

    with open("CryptPY\log.txt", "a") as f:
        f.write(f"\n \n[+] key : {key} delivered at : {time}")