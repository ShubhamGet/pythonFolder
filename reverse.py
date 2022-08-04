"""
#reverse
num=int(input("Enter number "))
rev=0
while(num!=0):
    ld=num%10
    num=num//10
    rev=rev*10+ld
print(rev)
"""
"""
#armstrong
num=int(input("Enter number "))
sum=0
temp=num
while(num!=0):
    ld=num%10
    num=num//10
    sum=sum+ld*ld*ld

    if(sum==temp):
        print("Number is Armstrong ",sum)
    else:
        print("Number is not Armstrong ",sum)
"""
"""
#palindrome
num=int(input("Enter number "))
rev=0
temp=num
while(num!=0):
    ld=num%10
    num=num//10
    rev=rev*10+ld

    if(rev==temp):
        print("Number is Palindrome ",rev)
    else:
        print("Numbe is not Palindrome ",rev)
"""

"""
#Sum of number

num=int(input("Enter number "))
sum=0
while(num!=0):
    ld=num%10
    num=num//10
    sum=sum+ld
print(sum)

"""

"""
#fibonci
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))

num=int(input("Enter number "))
print(fib(num))

"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


def palin(num):
    rev = 0
    temp = num
    while (num != 0):
        ld = num % 10
        num = num // 10
        rev = rev * 10 + ld

        if (rev == temp):
            print("Number is Palindrome ", rev)
        else:
            print("Number is not Palindrome ", rev)


def aram(num):
    sum = 0
    temp = num
    while (num != 0):
        ld = num % 10
        num = num // 10
        sum = sum + ld * ld * ld

        if (sum == temp):
            print("Number is Armstrong ", sum)
        else:
            print("Number is not Armstrong ", sum)


while (True):
    print("Menu Driven ")
    print("1.Aramstrong ")
    print("2.Palindrome ")
    print("3. Fibonaci ")
    ch = int(input("Enter ur choice "))
    if ch == 1:
        num = int(input("Enter number "))
        print(aram(num))
    elif ch == 2:
        num = int(input("Enter number "))
        print(palin(num))
    elif ch == 3:
        num = int(input("Enter number "))
        print(fib(num))
    else:
        print("No choice avaible ")
