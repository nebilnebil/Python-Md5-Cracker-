f=open("word.txt","w")
word="admin"
for i in range(0,1000):
    f.write(word+str(i))
    f.write("\n")

f.close()
    
