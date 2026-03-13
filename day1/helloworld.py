# from math import Calculator
# # print("Hello World!")
# # variables declaration
# num1 = int(input("Enter the first number: "))
# num2 = int(input( "Enter the second number: " ))
# calculation = str(input("Enter the calculation type: 'add', 'sub', 'mul', 'div': "))

# # adding two numbers
# # sum = num1 + num2

# if calculation == "add":
#     print(Calculator.addtion(num1, num2))
# elif calculation == "sub":
#     print(Calculator.subtraction(num1, num2))
# elif calculation == "mul":
#     print(Calculator.multiplication(num1, num2))
# elif calculation == "div":
#     print(Calculator.division(num1, num2))
# else:
#     print("Invalid calculation type")


tileArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tile = ""
while True:
    print("enter your tile (1-9):")
    tile = int(input())

    if type(tile) == int:
        break;

    print("you didn't enter a number")



print("you entered: " + str(tile))
tileArray.remove(tile)
print(tileArray)