#Write a python program that takes a list of numbers and returns their sum

list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
value= range(0,len(list1),1)
for i in value:
    sum=sum+list1[i]

print("sum is ", sum)