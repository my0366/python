import random

number = int(input("반복할 횟수 입력 : "))
random_numbers = [random.randint(1, 100) for x in range(number)]
result = []

def call(number):
    for i in range(0,number):
        print(f'{i+1}번째 숫자 : {random_numbers[i]}')
        answer = input("홀 또는 짝 : ")
        b = random_numbers[i] % 2 == 0
        if b and answer == "짝":
            print("정답")
            result.append(f"{i+1}번째 : O")
        elif b == False and answer == "홀":
            print("정답")
            result.append(f"{i+1}번째 : O")
        else:
            print("오답")
            result.append(f"{i+1}번째 : X")

call(number)
print(result)

        
    


