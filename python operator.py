#1.Write a program that reads one value of each type from the user in the following order
a=int(input())
b=float(input())
c=input().strip()
d=int(input())
e=float(input())
print(a)
print(b)
print(c)
print(d)
print(e)
#2.Progressive Float Execution
import struct 
a = float(input( ))
a=struct.unpack('f',struct.pack('f',a))[0]
print(f"{a:.5f}")
print(f"{a:.4f}")
print(f"{a:.3f}")
print(f"{a:.2f}")
print(f"{a:.1f}")
print(f"{a:.0f}")
#3.Given two integers A and B, print their sum, difference,product, quotient and remainder each on a new line
A,B=map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
if A<0 or B<0:
  c=abs(A)%abs(B)
  print(-1*c)
else:
  print(A%B)
  
#4.Write the program to execute conversion of other datatype
a=int(input())
b=chr(a)
print(b)

#5.You are given an integer counter. Perform the following operations in order:
a=int(input())
b=((a+5)*2)-3
print(b)

#6.Write a program that reads an integer and prints whether the number is Odd or Even using Ternary operator.
num=int(input())
if num%2 ==0:
  print("Even")
else:
  print("Odd")

#7.Write a program that reads an integer and print greatest among tree number using Ternary operator.
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
  print(a)
elif b>=c:
  print(b)
else:
  print(c)

#8.Write a program that reads a single character representing a digit ('0' to '9') and prints its integer value.
a=input()
print(a)

#9.Write a program that asks the user to enter their name (a single word).then, print a personalized greeting using that name in a sentence
a=input()
print(f"Hi {a}, welcome to the programming class!")

#10.John wants to learn how to calculate the total and average marks of a student in programming.
#Write a program that reads the student's name and marks in five subjects. Then calculate and print:
a=input()
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
total=b+c+d+e+f
avg=total/5
avg=f"{avg:.2f}"
print("Student Name:",a)
print("Total Marks:",total)
print("Average Marks:",avg)

#11.Veena wants to learn how to calculate the area of different shapes (Square, Rectangle, Circle, Triangle) and implement it in programming.
#Write a program to calculate the area of each shape based on the given inputs.
a = int(input())
l = int(input())
b = int(input())
r = int(input())
B = int(input())
h = int(input())
square = a * a
rectangle = l * b
circle = 3.14 * r * r
triangle = 0.5 * B * h
print("Area of Square=", square, sep="")
print("Area of Rectangle=", rectangle, sep="")
print("Area of Circle=", round(circle, 2), sep="")
print("Area of Triangle=", int(triangle) if triangle.is_integer() else triangle, sep="")

#12.Veena wants to learn how to calculate the perimeter of different shapes — Square, Rectangle, Circle, and Triangle — to implement them in programming.
#Write a program that reads the required dimensions and calculates the perimeter of each shape using the given formulas
a = int(input())
l = int(input())
w = int(input())
r = int(input())
side1 = int(input())
side2 = int(input())
base = int(input())

square = 4 * a
rectangle = 2 * (l + w)
circle = 2 * 3.14 * r
triangle = side1 + side2 + base
print(square)
print(rectangle)
print(round(circle, 2))
print(triangle)

#13.Priya is writing a program that needs to take two kinds of input from the user — first an integer, and then a sentence on the next line.
a=int(input())
b=input()
print(a)
print(b)