num=int(input("Enter number "))
sum=0
for i in range(num):
    ld=num%10
    num=num/10
    sum=sum+i
print(sum)

