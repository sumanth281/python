#arthmetic operations
"""
print("Arithmetic Operations:")
a=5
b=2
sum=a+b
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#reminder
print(a**b)#power
print()

#relational operators
print("Relational operations")
a = 50
b = 20
print(a==b) #False
print(a!=b) #True
print(a>b) #True
print(a<b) #False
print(a>=b)
print(a<=b)
print()

#Assignment operators
print("assignment operation")
num = 10
num+=10
num-=10
num*=5
num/=10
num%=3
num**=3
print("num:",num)
print()

#Logical operations
print("Logical operations")
a = 50
b = 30
print(not False)
print(not [a>b])# a>b is true but not a>b is false
print("or operator is:",[a==b] or [a>b])# a==b is false but a>b is true so or operator is true not true is false

val1 = True
val2 = True
print("and operator:",val1 and val2)
print("or operator:",val1 or val2)
print()

#Type conversion two types 1 is "conversion" automatic 2 is "casting" manual
#conversion automatic
a=2
b=3.5
print(a+b)
print()
#type casting manual
print("type casting")
a=int("2") #casting
b=3.5
print(a+b)
"""
# input methods
'''
print("input methods")
input("enter your name:")
age=int(input("enter your age:"))
marks=float(input("enter your  marks:"))
value=int("33344")
value=int(input("enter same value"))
print(type(value),value)#type checking
print("name is:")
print("age is:",age)
print("marks is:",marks)
print("value is:",value)
print()
'''
#q1 write tp input 2 numbers & print their sum
a=int(input("enter your first number"))
b=int(input("enter your second number"))
print("sum is:",a+b)
print()

#q2 write a program side of a square and print its area.
#square side is int/float and area is side*side(sqare)
side=float(input("enter the side of square"))
print("area of square is:",side*side)
print("area of square is:",side**2)
print()

#q3 write a program input 2 floating oint numbers and print thier average
a=float(input("enter first number"))
b=float(input("enter second number"))
print("the average is:",(a+b)/2)
print()

#q4 write a program to input 2 int numbers, a and b print True if a greater than or equal to b.if not print False
a=int(input("enter first number"))
b=int(input("enter second number"))
print(a>=b)