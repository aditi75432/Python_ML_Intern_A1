#5. Write a program that takes a string input from the user and writes it to a text file

#Write a program that takes a string input from the user and writes it to a text file

string_name= input("enter the string")
sample_file= open("C:/Users/aditi/Desktop/pyprojects/sample_entry.txt", 'w')
print(string_name, file= sample_file)