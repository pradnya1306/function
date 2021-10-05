# Write a Python function to find the Max of three numbers.
def max1(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num1 and num2>num3:
        print(num2)
    elif num3>num2 and num3>num1:
        print(num3)

num1=int(input("enter the 1st number :"))
num2=int(input("enter the 2nd number :"))
num3=int(input("enter the 3nd number :"))
max1(num1,num2,num3)