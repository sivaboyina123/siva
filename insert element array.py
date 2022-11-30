#insert numbers in an array

import array as arr

 #defining the array

a = arr.array('d',[1.1,1.2,3.2])

print(a)

#adding the element

a.append(2.5)

print(a)

# extend the elements

a.extend([3.8,4.8,3.2,5.0])

print(a)

a.pop(4)

print(a)
