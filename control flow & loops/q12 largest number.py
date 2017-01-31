# Python program to find the largest number among the 4 input numbers


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input('Enter fourth number: '))

if (num1 > num2) and (num1 > num3) and (num1>num4):
             largest = num1
   
elif (num2 > num1) and (num2 > num3) and (num2>num4):
             largest = num2
   
elif (num3>num1) and (num3>num2) and (num3>num4):
             largest = num3
    
else:
   largest = num4

print("The largest number between",num1,",",num2,",",num3,"and",num4,"is",largest)
