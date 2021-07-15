# PythonPractice
### Practising in Python language by doing some exercises

# Task-0
# Ключ SSH, пов'язаний з моїм обліковим записом
![0](https://user-images.githubusercontent.com/36934766/123948793-7d9c6000-d9aa-11eb-8fe4-86ce3ac89e23.png)

# Розташування мого публічного ключа SSH на комп'ютері
![1](https://user-images.githubusercontent.com/36934766/123948957-a9b7e100-d9aa-11eb-9db9-a89106482787.png)

# Переходимо на "Робочий стіл"
![2](https://user-images.githubusercontent.com/36934766/123949563-6316b680-d9ab-11eb-8fb3-7b7e870982e1.png)

# Клонуємо репозиторій через протокол SSH
### Спочатку копіюємо SSH URL
![3](https://user-images.githubusercontent.com/36934766/123950242-239c9a00-d9ac-11eb-8589-4a90e3402cd7.png)

### Потім клонуємо на "Робочий стіл"
![4](https://user-images.githubusercontent.com/36934766/123950609-8aba4e80-d9ac-11eb-9468-124bbd3b9f9d.png)

# За допомогою команди dir, що відображає файли в поточному каталозі, ми знаходимо папку PythonPractise
![photo_2021-06-30_15-27-53](https://user-images.githubusercontent.com/36934766/123960249-c1499680-d9b7-11eb-9866-6019bc7e9311.jpg)

# Потім переходимо до папки PythonPractise
![image_2021-06-30_14-22-30](https://user-images.githubusercontent.com/36934766/123960522-0bcb1300-d9b8-11eb-948a-f90b5e234807.png)

# Прописуємо git status, щоб побачити зміни у папці (перед виконанням цього я помістив файл Task-0.py у папку PythonPractise)
![image_2021-06-30_14-24-10](https://user-images.githubusercontent.com/36934766/123960627-30bf8600-d9b8-11eb-99a0-2be54d050d8e.png)

# Прописуємо команду git add . , що додає вміст (в поточному каталозі і його підкаталогах) в індекс для подальшого комміта
![image_2021-06-30_14-27-52](https://user-images.githubusercontent.com/36934766/123960954-8a27b500-d9b8-11eb-8bb5-bce3b0ab1bda.png)

# Прописуємо команду git commit, що записує індексовані зміни в репозиторій, та -m, тобто з повідомленням "Додавання файлу Task-0.py"
![image_2021-06-30_14-37-05](https://user-images.githubusercontent.com/36934766/123961053-a1ff3900-d9b8-11eb-9d94-dc80f95aa282.png)

# За допомогою команди git push origin ми замержуємо всі гілки локального репозиторія на віддалений репозиторій. Замержити, тобто здійснювати злиття
### Бачимо, що push відхилено

![image_2021-06-30_15-20-06](https://user-images.githubusercontent.com/36934766/123961285-da9f1280-d9b8-11eb-8b94-b49057fbf37f.png)

# Виправляємо помилку за допомогою команди git pull --rebase, що прибирає локальні комміти, оновлює гілку, і потім після оновлення знову застосовує комміти
![image_2021-06-30_15-22-30](https://user-images.githubusercontent.com/36934766/123961358-ebe81f00-d9b8-11eb-9fc1-54963c11422e.png)

# Знову прописуємо git push origin
![image_2021-06-30_15-23-24](https://user-images.githubusercontent.com/36934766/123961465-0fab6500-d9b9-11eb-9a2d-f1dbcbb64d0f.png)

# Бачимо, що все вдалося, і зміни надійшли
![image_2021-06-30_15-26-13](https://user-images.githubusercontent.com/36934766/123961512-1e921780-d9b9-11eb-8765-a18439c260cc.png)

# Task-1
![Знімок екрана 2021-07-03 184622](https://user-images.githubusercontent.com/36934766/124359750-fd3a6100-dc2e-11eb-821e-32ced7f0b520.png)
### Знадобився лише один комміт, хоча можна було розділити його на частини: потрібно було створити дві папки task-0 та task-1, в першу було переміщено файл завдання Task-0, а в другу було створено й додано файл завдання Task-1

# Пояснення до мого проєкту (завдання Task-1)
**Просто запускаємо код у редакторі коду (Visual Studio Code і т.д.) та вписуємо будь-який рядок. Як результат побачимо рядок без чисел, масив чисел, змінений рядок в якому кожне слово починається й закінчується великою літерою, максимальне значення в масиві чисел та інші числа, піднесені до степеню по їх індексу.**<br>
<br>***Поясненния також є в моєму коді (task-1.py), тобто коментарі.***
### 1
```python
import re
```
**модуль для роботи з регулярними виразами, тобто, працюючий з текстом, формальна мову пошуку і здійснення маніпуляцій з підрядками в тексті**
### 2
```python
string = input("\nВведіть будь-що: ")
```
**звичайне введення рядка**
### 3
```python
letters = ''.join([i for i in string if not i.isdigit()])
```
**генератор списку з умовою, що додає елемент з string до списку letters, який не є числом, та приєднує кожен символ без пробілу за допомогою join**
### 4
```python
nums = re.findall(r'\d+', string)
```
**для роботи з регулярними виразами використовується модуль re та одна з основних функцій цього модуля - findall, тобто повертає список всіх знайдених збігів; у нашому випадку шукає числа('\d' - відповідає будь-якій одній цифрі і замінює собою вираз [0-9] та '+' - позначає символ(для нашого випадку число), який повторюється кілька разів, тобто '\d+' означає одну або більше цифр [0-9])**
### 5
```python
nums = [int(i) for i in nums]
```
**генератор списку з додаванням цілих чисел до масиву чисел nums з nums**
### 6
```python
print("\nРядок без чисел:", letters)
```
**виведення рядка без чисел letters**
### 7
```python
print("Масив чисел:", nums)
```
**виведення масиву чисел nums**
### 8
```python
LetterS = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in letters.split())
```
**генератор списку, що: 
1) розділяє рядок без чисел letters на слова за допомогою функції split; 
2) за допомогою умови word[0].upper() for word in робить так, щоб слово починалося з великої літери, бо word[0] перша літера в слові; за допомогою word[1:-1] (тобто word[start:stop]) пробігається далі по літерам, починаючи з другої та закінчуючи на передостанній (останньої немає, бо :stop -> :-1 -> окрім останньої); за допомогою word[-1:].upper() робить так, щоб слово закінчувалося великою літерою, бо start: -> -1: -> остання літера слова; 
3) додає кожне змінене слово в список LetterS через пробіл, бо зробили відступ між лапками ' '.join**
### 9
```python
print("\nЗмінений рядок:", LetterS)
```
**виведення зміненого рядка LetterS, який містить слова, що починаються й закінчуються великою літерою**
### 10
```python
print("Максимальний елемент масиву:", max(nums))
```
**знаходить і виводить максимальне значення в масиві чисел nums**
### 11
```python
nums.remove(max(nums))
```
**просто видаляє максимальне значення в масиві чисел nums, щоб воно не заважало іншим числам, які будуть підноситися до степеню по їх індексу**
### 12
```python
nums_with_index = [nums[i]**i for i in range(0,len(nums))]
```
**генератор списку, який підносить числа до степеню по їх індексу з 0 до довжини nums та додає до масиву чисел nums_with_index**
### 13
```python
print("Масив чисел, піднесені до степеню по їх індексу:", nums_with_index)
```
**виводить масив чисел nums_with_index, які піднесені до степеню по їх індексу**

# Task-2
![Знімок екрана 2021-07-11 174323](https://user-images.githubusercontent.com/36934766/125199640-d05dfd80-e26f-11eb-926b-0d15c0ed7f80.png)
<br><br>**Перейшов до робочого столу -> до папки PythonPractice, побачив статус файлу та попередньо додав вміст, закомітив і замержив усі гілки локального репозиторія на віддалений репозиторій**<br><br>
![Знімок екрана 2021-07-11 174358](https://user-images.githubusercontent.com/36934766/125199642-d358ee00-e26f-11eb-82b1-99affdc920b5.png)
### Знадобився лише один комміт, хоча можна було розділити його на частини: в папку PythonPractice потрібно було створити папку task-2, в яку також створити й додати файл завдання Task-2

# Пояснення до мого проєкту (завдання Task-2)
**Просто запускаємо код у редакторі коду (Visual Studio Code і т.д.) та бачимо, що програма успішно запустилася. Як результат побачимо віконну програму, в якій реалізовані основні функції калькулятора: додавання, віднімання, множення, ділення; додаткові функції: знаходження значень синуса, косинуса, тангенса, котангенса, логарифма, натурального логарифма, ділення за модулем; також присутнє очищення введеного значення та повне очищення, кнопка видалення значень один за одним, кнопка "dot" для чисел з плаваючой точкою(float), виведення числа після операції(кнопка "дорівнює") та кнопка, яка буде переводити введене число до двійкового коду(binary code); авжеж, усі ці операції неможливо проводити без числа, тому програма має цифрову клавіатуру(numpad).**<br>
<br>***Поясненния також є в моєму коді (task-2.py), тобто коментарі.***

# Task-3
![Знімок екрана 2021-07-14 163132](https://user-images.githubusercontent.com/36934766/125631203-66897b3b-f9ea-4371-8def-0853600245f1.png)
<br><br>**Перейшов до робочого столу -> до папки PythonPractice, побачив статус файлу, додав вміст(git add .), закомітив і замержив усі гілки локального репозиторія на віддалений репозиторій**<br><br>
![Знімок екрана 2021-07-14 163406](https://user-images.githubusercontent.com/36934766/125631305-92411f02-36a8-472a-8371-bb0062dcf5ca.png)
### Знадобився лише один комміт, хоча можна було розділити його на частини: в папку PythonPractice потрібно було створити папку task-3, в яку також створити й додати файл завдання Task-3

# Пояснення до мого проєкту (завдання Task-3)
**Просто запускаємо код у редакторі коду (Visual Studio Code і т.д.) та бачимо, що програма успішно запустилася. Як результат побачимо віконну програму, в якій наведена статистика по 6 країнам(США, Індія, Бразилія, Росія, Франція, Великобританія); реалізована кнопка "Reload", за допомогою якої буде проходити оновлення інформації з ресурсу(VACCOVID.LIVE); реалізована кнопка "Find statistics!" і поле вводу, тобто все це дає нам можливість ввести країну в полі вводу, після введення настає виведення статистики по цій країні; також присутнє створення 2-ох файлів JSON, тобто парсинг(перший "all.json" надає всю інформацію з API VACCOVID, а другий "my.json" надає інформацію щодо статистики країни, яку я вводив у полі вводу.**<br>
<br>***Функція виводу інформації, що по даній країні інформація недоступна, тобто:***
```python
tkinter.messagebox.showerror("Country statistics related to COVID-19", "Error! Entered country does not exist!")
```
<br>***Її складно реалізувати через те, що в моєму коді розглядаються індекси країн; також json файл(у якому реалізований запит) не має масиву для списку країн (зручно було б, якщо він називався б "Countries")***<br>
<br>***Поясненния також є в моєму коді (task-3.py), тобто коментарі.***

# Task-4
![Знімок екрана 2021-07-15 154859](https://user-images.githubusercontent.com/36934766/125798071-efe63283-cdc5-4253-9a16-e47fda3b634e.png)
<br><br>**Перейшов до робочого столу -> до папки PythonPractice, побачив статус файлу, додав вміст(git add .), закомітив і замержив усі гілки локального репозиторія на віддалений репозиторій**<br><br>
![Знімок екрана 2021-07-15 163942](https://user-images.githubusercontent.com/36934766/125798124-2e1191d4-3643-4b1f-b9cc-812bef9127cc.png)
### Знадобився лише один комміт, хоча можна було розділити його на частини: в папку PythonPractice потрібно було створити папку task-4, в яку також створити й додати файл завдання Task-4; також потрібно було додати папку static для стікерів та відео з демонстрацією роботи бота(video.mkv)

# Пояснення до мого проєкту (завдання Task-4)

<br>***Функція виводу інформації, що по даній країні інформація недоступна, тобто:***
<br>***Вона працює некоректно через те, що до цього було прописано loop if message.text == str(message.text), але помилки при вводі іншого повідомлення немає, бо str цьому допомагає***
```python
elif country not in data: #якщо country немає в data
  if str(message.text) != country['Country']:
    bot.send_message(message.chat.id, '<b>Error! Incorrect input!</b>', parse_mode='html')
    sti6 = open('static/6.webp', 'rb')
    bot.send_sticker(message.chat.id, sti6)
```
<br>***Її складно реалізувати через те, що в моєму коді розглядаються індекси країн та message.text == str(message.text); також json файл(у якому реалізований запит) не має масиву для списку країн (зручно було б, якщо він називався б "Countries")***<br>
<br>***Поясненния також є в моєму коді (task-3.py), тобто коментарі.***
