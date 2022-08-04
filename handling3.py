try:
    ptr=open("file.log","r")
    read_data=ptr.read()
except:
    print("could not open file.log")

