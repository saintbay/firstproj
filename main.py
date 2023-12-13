def bmi_calculatur(height,weight):
    return weight / height**2

weihgt = float(input("Введите свой вес в килограммах "))
height = float(input("Введите свой рост в самтиметрах "))
bmi = bmi_calculatur(weihgt,height)
if bmi < 18.5:
    print(f"У вас недовес. Ваш показатель bmi = {bmi}")
elif bmi > 18.5 and bmi < 24.9:
    print(f"Все отлично. Ваш показатель bmi = {bmi}")
else:
    print(f"У вас перевес. Ваш показатель bmi = {bmi}")