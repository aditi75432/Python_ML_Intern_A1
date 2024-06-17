#Write a program that asks the user for their birth year and calculates their age

year= int(input("enter your birth year"))
age=0
diff= 2024-year
while diff>0:
      age=age+1
      diff=diff-1
print("age is: ", age)
