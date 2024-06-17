#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines
# Created an empty list named 'lines'
lines = []

# Continue to prompt the user for input indefinitely until a blank line is entered
while True:
    # Prompt the user to input a line of text
    l = input()
    
    # Check if the entered line is not empty (non-empty string)
    if l:
        # Convert the entered line to uppercase and append it to the 'lines' list
        lines.append(l.strip())
    else:
        # If the entered line is empty, break out of the loop
        break;

# Iterate through each line in the 'lines' list
for l in lines:
    # Print each line (converted to uppercase) from the 'lines' list
    print(l) 
	