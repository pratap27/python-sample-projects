# HCF (highest common factor or GCD (greatest common divisor)

# take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def computeHCF(a, b):
   """This function takes two
   integers and returns the H.C.F"""
   a = int(a)
   b = int(b)

   # choose the smaller number
   if a > b:
       x = a
   else:
       x = b

   for i in range(1,x):
       if a % i == 0 and b % i == 0:
           hcf = i
         return hcf
       

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))


# Euclidean algorithm:

def computerHCF(x, y):
   """This function implements the Euclidian algorithm to find H.C.F. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

print(computerHCF(300, 400))
