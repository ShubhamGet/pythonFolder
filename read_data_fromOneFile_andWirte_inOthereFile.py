ptr1=open("alphachar.txt","r")
oldData=ptr1.read()

ptr2=open("alphachar1.txt","w")
ptr2.write(oldData)

for line in ptr1:
    ptr2.write(line)
