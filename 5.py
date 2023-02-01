list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}

#1
print(len(list1))
print(len(tuple1))
print(len(set1))
print(len(dict1))

#2
print( list1[0])
print(tuple1[0])

#3
print(list1[0])
print(tuple1[0])

#4
print(dict1['lion'])

#5
list1[1] = "rabbit"
print(list1)

#6
list1.append("monkey")
print(list1)

#7
list1.remove("rabbit")
print(list1)

#8
dict1["fish"] = 0
print( dict1)
