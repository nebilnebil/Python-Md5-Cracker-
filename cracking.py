from hashlib import md5
from colorama import Fore
#imported md5 Libary for Checking  hash
logo=Fore.RED+f"""
      ######################
            [MD5 CRACKER]
            *************
      
      Facebook:nebil Sharifi
      Telegram:nebil_247
      github:nebilnebil
      ######################
       
"""
print(logo)
hash_encrypted=input("Enter Md5 hash:")
if(len(hash_encrypted)<32):
    print(Fore.RED+"Hash is Invalid Type")
    exit()
wordlist=input("Enter Wordlist Name Or Path:")
def main(file):
    f=open(file,"rb")
    for line in f.readlines():
        word=line.split()
        md=md5()
        for newline in word:
            new=newline
            md=md5()
            md.update(new)
            if(md.hexdigest() == hash_encrypted):
               
               print(f"Password Found[+]:{Fore.GREEN+str(new.decode())}")
               print(Fore.WHITE+f"Hash is:{Fore.GREEN+hash_encrypted}")
               break
            else:
                print("Not Found")
        
main(wordlist)
#Created By Nebil Sharifi  
        
        
        

