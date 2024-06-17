#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input

conv= input("enter f for fahrenheit conv and d for degree conv ")

if conv=='f':
    C= int(input("input celcius value"))
    F= 1.8 *C +32
    print(F)

elif conv=='d':
    F=int(input("input fakrenheit value"))
    C= (F-32)/1.8
    print(C)

else:
    print("invalid input")