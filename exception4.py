import sys
def x():
    assert('linux' in sys.platform)

try:
    x()

except:
    print("dvbju")

try:
    x()
    
except AssertionError as error:
    print(error)
    print("The linux_interaction() function was not executed ")
