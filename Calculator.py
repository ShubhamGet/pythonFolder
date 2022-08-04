while(True):
    n1=int(input("Enter Number "))
    n2=int(input("Enter number "))

    print("\n+(Add)","*(Mul)","-(Sub)","/(Div)")
    n3=input()

    if n3=='+':
        add=n1+n2
        print(add)
    elif n3=='*':
        mul=n1*n2
        print(mul)
    elif n3=='-':
        sub=n1+n2
        print(sub)
    elif n3=='/':
        div=n1/n2
        print(div)
    else:
        print("Out of Range")




