from asyncore import read


try:
    linux_interaction()

    ptr=open("file.log","r")
    read_data=ptr.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print("Linux linux_interaction() fun was not executed ")