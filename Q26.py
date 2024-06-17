#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

string= "Aditi Mehta"
suffix= "hta"
preffix= "Adi"

if (  string.index(suffix)==len(string)-len(suffix) ):
    print("suffix exists")

else:
    print("suffix doesnt exist")

if(string.index(preffix)==0):
    print("preffix exists")
else:
    print("preffix doesnt exist")