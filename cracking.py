from hashlib import md5
#imported md5 Libary for Checking  hash
user=input("Enter Md5 hash:")
wordlist=input("Enter Wordlist path:")
def file_handling(file):
    f=open(file,"rb")
    for line in f.readlines():
        word=line.split()
        md=md5()
        for newline in word:
            newhash=newline
            md=md5()
            md.update(newhash)
            if(md.hexdigest() == user):
               
               print(f"Password Found:{newhash}")
               print(f"Hash is:{user}")
               break
            else:
                pass
        
file_handling(wordlist)
#Created By Nebil Sharifi  
        
        
        

