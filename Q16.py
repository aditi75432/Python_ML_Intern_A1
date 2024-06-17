#Write a program in python that counts the frequency of each character in a string
count =0
str= input("enter a string ")
char= input("enter a char ")
values =range(0,len(str), 1)
for i in values:
    if str[i]==char:
        count+=1

print("occurance of char is ", count)