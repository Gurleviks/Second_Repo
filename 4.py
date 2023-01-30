list1 = ["lion", "monkey", "dog","fish"]
for element in list1:
    print(element)

tuple1 = ("lion", "monkey", "dog","fish")
for element in tuple1:
    print(element)

set1 = {"lion", "monkey", "dog","fish"}
for element in set1:
    print(element)

dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}
for animal, habitat in dict1.items():
    if habitat == "land":
        print(animal, "lives in", habitat)
