#Tuple: tuple is starting with c brackets and is immutable
t = (1,2,3,4) # tuple
l = [1,2,3,4] # list
print(type(t))
print(type(l))

l[0] = 10
#t[0] = 10
print (l)
print (t)
print("lenth of the tuple:",len(t))
print("lenth of the list:", len(l))
print("maximum valu of tuple:", max(t))
print("maximum value of list:", max(l))
print("minimum value of list:", min(l))
print("minumu value of tuple:", min(t))
