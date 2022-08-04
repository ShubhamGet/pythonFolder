ptr=open("alphachar.txt","r")
data=ptr.read()
upperCase=0
for i in data:
    if i.isupper():
        upperCase=upperCase+1
print("Total number of Alphabets are ",upperCase)