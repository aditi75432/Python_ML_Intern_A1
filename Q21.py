#Write a python program that counts the occurrences of a specific element in a list
list1=[1,2,3,4,5,3,3,8,9]
num=3
count=0

value=range(0, len(list1),1)

for i in value:
    if list1[i]==num:
        count+=1
print("count is ", count)