import numbers
import random


def call(number):
    result = []
    print("0은 왼쪽, 1은 오른쪽")
    random_numbers = [random.randint(0, 1) for x in range(number)]
    print(random_numbers)
    for i in range(0,number):
        a = int(input())
        if a == random_numbers[i]:
            result.append("생존")
            print("생존")
        else:
            result.append("사망")
            print("사망")
            break

    print(result)
        

number = int(input("길이 설정 : "))
call(number)