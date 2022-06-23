import random

menu = "짜장","짬뽕"
def b(a):
    if a == "짜장" or a == "짬뽕":
        m = random.choice(menu)
        print(f"{m}먹어")
    # 여기에서 짜장과 짬뽕중에 인공지능의 추천결과는?
    else:
        print("짬짜면 먹어!")