# Python program to give sum of natural numbers
num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = (num*(num+1))/2

print("The sum is",sum)

''' sum = 0
 while(num > 0):
       sum += num
       num -= 1
print("The sum is",sum)
'''
