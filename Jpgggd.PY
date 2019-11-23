input("Отпишись__")
print("Скажи-ка мне,сколько тебе лет?")
age = float(input("age:"))
if age>=19:
    print("Very Nice")
    
if age == 18:
    print("Good")
elif age<17:
    print("Ok")
if age == 17:
    print(True)
input("Если ты(вы)это видишь,то отпишись")
print("Какое у тебя имя?")
name = input("Введите ваше имя:")
print("Вас зовут:" + name + ",ваш возраст:" + str(age) + " лет")
print("Created by Danilchik")

