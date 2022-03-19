from math import *
Binary = input("Enter the Binary value: ")
i = len(Binary)
decimal = 0

for letter in Binary:
  i -= 1
  decimal += (float(letter)* (pow(2, i)))
  print(decimal)

print("The decimal: " + str(decimal))