# 1.Take a string from the input and print the length of that string
a=input()
print(len(a))
# 2.Take two strings from the input, join those two strings with a space and print the new string
a=input()
b=input()
print(a+" "+b)
# 3.Take two strings from the input and print whether or not the strings are equal
a=input()
b=input()
if a==b:
  print("true")
else:
  print("false")
# 4.Take a string from the input and print the first character of that string
a=input()
print(a[0])
# 5.Take a string from the input and print the last character of that string
a=input()
print(a[-1])
# 6.Take a string from the input and print the first character and last characters of the string together
a=input()
print(a[0]+a[-1])
# 7.Take a string from the input and check whether or not it contains both letters and numerals
s = input()

letter = False
number = False

for i in s:
    if i.isalpha():
        letter = True
    if i.isdigit():
        number = True

if letter and number:
    print("true")
else:
    print("false")
# 8.Take a string from the input and check all the letters in the string are of upper case
a=input()
if a.isupper():
  print("true")
else:
  print("false")
# 9.Take a string from the input and check all the letters in the string are of lower case
a=input()
if a.islower():
  print("true")
else:
  print("false")
# 10.Take two strings from the input and check the lengths of those strings equal or not
a=input()
b=input()
if len(a)==len(b):
  print("true")
else:
  print("false")
# 11.Take a string from the input and print it in reverse
a=input()
print(a[::-1])
# 12.Take a string from the input and split the strings with comma. Print the new strings one per line
a=input()
b=a.split(",")
for i in b:
  print(i)
# 13.Take a string from the input and remove the vowels and print it
a=input()
for i in a:
  if i not in "aeiouAEIOU":
    print(i,end="")
#14.Take a string from the input and change lowercase characters to uppercase and uppercase characters to lowercase
a=input()
print(a.swapcase())
#15.Take a string from the input and print ascii character
a=input()
print(ord(a))
#16.Take a string from the input and remove all occurrences of given char from that string
a=input()
d=input()
a=a.replace(d,"")
print(a)
#17.Search a word existence inside a given string
a=input()
b=input()
if b in a:
  print("true")
else:
  print("false")
#18 Count the total vowels and consonants in a given string and print them
s = input()
v = 0
c = 0
for i in s:
  if i in "aeiou":
    v = v + 1
  elif i.isalpha():
    c = c + 1
print(v)
print(c)
#19 Check the given 2 strings are anagrams.
a=input()
b=input()
a=a.replace(" ","").upper()
b=b.replace(" ","").upper()
if sorted(a)==sorted(b):
  print("true")
else:
  print("false")
# 20.Check whether or not the given string is a palindrome
a=input()
b=a[::-1]
if a==b:
    print("true")
else:
    print("false")