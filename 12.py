my_list = [*range(5)]
pow2 = lambda x: x**2
sum = list(map(pow2, my_list))
print(sum)