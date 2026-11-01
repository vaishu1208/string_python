#1. Write a program to count the number of digits in a given integer.**python
n = int(input())
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n = n // 10
print(count)
#2. Write a program to find the sum of all even digits in a given number.*`python
n = int(input())
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total += digit
    n = n // 10
print(total)
#3. Write a program to find the product of all digits of a given integer.**
n = int(input())
product = 1
if n == 0:
    product = 0
else:
    while n > 0:
        digit = n % 10
        product = product * digit
        n = n // 10
print(product)
#4. Write a program to reverse a given integer.**
n = int(input())
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(reverse)
#5. Write a program to check whether a given number is a palindrome or not.**
n = int(input())
temp = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if temp == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
#6. Write a program to find the first digit of a given number.**
n = int(input())
while n >= 10:
    n = n // 10
print(n)
#7. Write a program to count how many zeros are present in a given number.**
n = int(input())
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        digit = n % 10
        if digit == 0:
            count += 1
        n = n // 10
print(count)
#8. Write a program to check whether a given number is an Armstrong number or not.**
n = int(input())
temp = n
digits = len(str(n))
total = 0
while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10
if total == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
#9. Write a program to check whether a number is a Strong number or not.**
n = int(input())
temp = n
total = 0
while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    total = total + fact
    n = n // 10
if total == temp:
    print("Strong")
else:
    print("Not Strong")
#10. Write a program to check whether a given number is a Perfect number or not.**
n = int(input())
total = 0
for i in range(1, n):
    if n % i == 0:
        total = total + i
if total == n:
    print("Perfect")
else:
    print("Not Perfect")