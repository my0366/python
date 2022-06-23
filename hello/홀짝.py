import random

number = int(input("반복할 횟수 입력 : "))
random_numbers = [random.randint(0, 1) for x in range(number)]
