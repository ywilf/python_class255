'''
Open a new python file under lecture1 project and name it conditions.py
Create a string variable named x with any value that you want, length of the string must be at least 10 characters.
1. If the character in index 0 is ‘A’ print the characters in indexes 7, 8, 9,
    else print the last character
2. If index 7 in string is equal to ‘d’ and index 8 is equal to ‘e’
    or If index 8 in string is equal to ‘e’ and index 9 is equal to ‘f’
    print “version A”.
Else print “version B”
Try several strings in your code.
'''
str1 = "this is python course, lecture 2"
str2 = "Ahis is python course, lecture 2"
str3 = "hi by tttdadaf adfasfdas"
str4 = ""
x = str2

if x[0] == 'A':
    print(x[7:10])
else:
    print(x[-1])

if (x[7] == 'd' and x[8] == 'e') or (x[8] == 'e' and x[9] == 'f'):
    print("Version A")
else:
    print("Version B")

