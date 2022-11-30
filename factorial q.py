n = int(input("Enter the number: "))

if (n<0):
    print("Enter number is invalid")
elif (n==0):
      print("Factorial of 0 is 1")
else :
    mul=1
    for i in range(1,n+1):
        mul = mul * i
        print("factorial of {} = {}".format (n,mul))
