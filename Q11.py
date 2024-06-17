#Write a python program that generates the first n numbers in the Fibonacci sequence.

n= int(input("enter number of terms: "))
num1=0
num2=1
n=n-2
print(" ",num1)
print( " ", num2)
while  n>0:
       next_num= num1+num2
       print(" ", next_num)
       num1=num2
       num2= next_num
       next_num=num1+num2
       n=n-1

print("sequence complete")
