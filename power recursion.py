def power(base,exponent):
    if exponent==0:
        return1
    elif exponent >0:
      return base * power(base,exponent-1)
    else:
            return 1/power(base,-exponent)
base = int(input("enter the number"))
exponent=int(input("enter power of a number"))
result=power(base,exponent)
print(result)
