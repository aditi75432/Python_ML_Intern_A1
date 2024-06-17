#Write a python program that removes all punctuation from a given string.

str=input("enter a string ")

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


# Removing punctuations in string
# Using loop + punctuation string
for ele in str:
	if ele in punc:
		str = str.replace(ele, "")

# printing result
print("The string after punctuation filter : " + str)
