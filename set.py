#set is started with flower brackets
#a set can be defined as a collection which is unordered and unindexed. sets ar
#sets are written with curly brackets.
#once a set is created, you cannot change its items, butyou can add new items.
#by referring to an index, you cannot access items in a set. since are unordered
#the items has no index.
#by using for loop we can access the set items, or ask if a specified value is
#present in a set, by using the in keyword.
Rollnoset = {1123112332,14424442525,766333243,234234553,252525235,452542}

print(Rollnoset)
#for adding single element
Rollnoset.add(1245452)

print(Rollnoset)
#for adding more elements/add set also
Rollnoset.update({2134213,2345253,252523,2535452})

print(Rollnoset)
#it is unordered so it has no index values
#print(rollnoset[0])

for set in Rollnoset:
   print(set)

print(2344253 in Rollnoset)

Rollnoset.discard(2134213 in Rollnoset)

print(len(Rollnoset))

Rollnoset.pop()

print(Rollnoset)

set1 = {123456,123467,123897,2763782,397472345}

set2 ={123456,3245693,472804,842084,123897}

set3 = set1.union(set2)

print(set3)

set3 = set1.intersection(set2)

print(set3)

Rollnoset.clear()

print(Rollnoset)
