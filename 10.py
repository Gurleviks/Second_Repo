import random

def random_list_summer(n=15):
    random_list = [random.randint(-100, 100) for i in range(n)]
    print("Random List:", random_list)
    list_sum = sum(random_list)
    print("Sum of the elements:", list_sum)

random_list_summer()
