n = int(input("Enter a number"))
originalvalue = n
reverse = 0
while(n>0):
    num = n%10
    reverse = reverse*10+num
    n = n//10
    print('rever of number {}is {}'. format(orginalvalue, reverse))
