#!usr/bin/python3

print("WELCOME TO BASIC CALCULATOR OF TWO NUMBERS")
print("Enter the Two numbers for calculation")
input(a)
input(b)

print("Choose one of the following operations to perform:")

print("1.ADD/2.SUBTRACT/3.MULTIPLY/4.DIVIDE")
input(c)
def choice(c)
switcher={ 
1:
Ans=a+b
2:
Ans=a-b
3:
Ans=a*b
4:
Ans=a/b
}
return switcher.get (c,"wrong choice")
print('Your answer is '+ Ans)


