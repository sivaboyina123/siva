#A list is a collection which is ordered and changeable. lists are written with square brackets.
numberlist = [14.6353,166.876368,6663.938737,73636,736737,12.6875]
#index is starting with 0
print(numberlist[0])
#lists are written with square brackets
print(numberlist[1])
print(numberlist[2])
print(numberlist[3])
print(numberlist[4])
#negative index are starting with -1
print(numberlist[-1])
print(numberlist[-2])
print(numberlist[-3])
print(numberlist[-4])
print(numberlist[-5])
#we can specify the range of index in b/w list also
print(numberlist[3:6])
print(numberlist[2:4])
print(numberlist[5:8])
#append
numberlist.append(255378873)
print(numberlist)
#lenth
print(len(numberlist))
#insert
numberlist.insert(4,6765543)
print(numberlist)
#pop
numberlist.pop(4)
print(numberlist)
#extend
addlist =[678,254,77572,753792]
numberlist.extend(addlist)
print(numberlist)
#reverse
numberlist.reverse()
print(numberlist)
#clear
numberlist.clear()
print(numberlist)

                
