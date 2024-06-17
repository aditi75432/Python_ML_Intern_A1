#Write a python program that calculates the sum of the digits of a given number.

num= int(input("enter number "))
sum=0
while num>0:
      n= num %10
      sum= sum+n
      num=num//10

print("sum of digits is ", sum)