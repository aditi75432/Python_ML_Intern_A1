#Write a program that copies the contents of one text file to another.

sample_file= open("C:/Users/sanku/Desktop/py projects/sample_entry.txt", 'r')

# Read the lines of the file
file_lines = sample_file.readlines()
 
        # Print each line
print("File Content:")
for line in file_lines:
      print(line.strip(), file= copy_file)