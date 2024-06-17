#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.


num1= int (input("enter num1: "))
num2= int(input("enter num2: "))
op= input("enter operator (/,*,+,-)")

if op=='+':
    print("sum is ", num1+num2)

elif op=='-':
    print("answer is ", num1-num2)

elif op=='*':
    print("product is ", num1*num2)

elif op=='/':
    print("answer is ", num1/num2)

else:
    print("invalid operator")