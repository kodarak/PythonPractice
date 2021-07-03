import re #модуль для роботи з регулярними виразами

string = input("\nВведіть будь-що: ")

letters = ''.join([i for i in string if not i.isdigit()]) #генератор списку з умовою та приєднанням елементів

nums = re.findall(r'\d+', string) #шукає всі збіги з шаблоном string, тобто цілі числа
nums = [int(i) for i in nums] #генератор списку з додаванням цілих чисел

print("\nРядок без чисел:", letters)
print("Масив чисел:", nums)

LetterS = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in letters.split()) #утворення великих літер за допомогою позначень зрізу через зріз слів
print("\nЗмінений рядок:", LetterS)
print("Максимальний елемент масиву:", max(nums)) #знаходить і виводить максимальне значення в масиві чисел

nums.remove(max(nums)) #видаляє максимальне значення в масиві чисел nums
nums_with_index = [nums[i]**i for i in range(0,len(nums))] #генератор списку з піднесенням масиву чисел до степеню по їх індексу
print("Масив чисел, піднесені до степеню по їх індексу:", nums_with_index)
print("\n")