ptr=open("alphachar.txt","r")
data=ptr.read()
alphanumeric=0
for i in data:
    if i.isalpha():
        alphanumeric=alphanumeric+1
print("Total Alphanumerics ",alphanumeric)