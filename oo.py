sentence = "The quick brown fox jumps over the lazy dog."
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("List of odd numbers:", odd_numbers)

mixed = [1, "apple", 3, "banana", 5, "cherry"]
numbers = [item for item in mixed if isinstance(item, int)]
strings = [item for item in mixed if isinstance(item, str)]

print("List of numbers:", numbers)
print("List of strings:", strings)
