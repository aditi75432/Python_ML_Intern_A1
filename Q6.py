#Write a program that reads the content of a text file and prints it to the console.

sample_file= open("C:/Users/sanku/Desktop/py projects/sample_entry.txt", 'r')

# Read the lines of the file
file_lines = sample_file.readlines()
 
        # Print each line
print("File Content:")
for line in file_lines:
     print(line.strip())