num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
print(num1)
print(num2)
print(num3)

if ((num1>num2) and (num1>num3)):
    largest_num = num1
    print(num1, " is greater than num2 & num3" )

elif ((num2>num1) and (num2>num3)):
    largest_num = num2
    print(num2, "is greater than num1 & num3")
else:
    largest_num = num3
    print(num3, "is greater than num1 & num2")
