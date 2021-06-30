import random
#Генерує список з 30 випадкових цілих чисел від -100 до + 100
randomlist = random.sample(range(-100, 100), 30)
print("\n")
print(randomlist)

print("\nМаксимальний елемент списку: ", max(randomlist)) #знаходить і виводить максимальний елемент списку
print("Його порядковий номер: ", randomlist.index(max(randomlist))) #виводить порядковий номер максимального елемента списку
print("\n")

#Cписок, що складається тільки з непарних чисел вихідного списку
newlist = [i for i in randomlist if (i % 2) == 1] #генератор списку з умовою
if len(newlist) == 0: 
    print("Таких чисел немає!") #повідомляє, що таких чисел немає
print(sorted(newlist, reverse=True)) #список, виведений в порядку зменшення елементів
print("\n")