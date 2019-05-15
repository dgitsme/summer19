#!usr/bin/env python3

print("WELCOME TO BASIC CALCULATOR OF TWO NUMBERS")
print("Enter the Two numbers for calculation")
a=int(input())
b=int(input())

print("Choose one of the following operations to perform:")

print("1.ADD/2.SUBTRACT/3.MULTIPLY/4.DIVIDE")
c=int(input())

def choice(c):
   switcher ={ 
      1: a+b,
      2: a-b,
      3: a*b,
      4: a/b,
   }
   return switcher.get(c,"wrong choice")
print("Your answer is" + str(choice(c)))


