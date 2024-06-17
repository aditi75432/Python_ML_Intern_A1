#3. Write a python program that calculates the factorial of a given number


num1=int(input("enter the nuber whose factorial is to be calculated: "))
if(num1==0 or num1==1):
    print("The factorial of the number is : 1")
elif(num1<0):
    print("Please enter a positive integer as the factorial of negative numbers do not exist")
else:
    fact=1
    while(num1>0):
        fact*=num1
        num1-=1

    print("The factorial of the given number:",fact)