# PythonPractice
Practising in Python language by doing some exercises

# Ключ SSH, пов'язаний з моїм обліковим записом
![0](https://user-images.githubusercontent.com/36934766/123948793-7d9c6000-d9aa-11eb-8fe4-86ce3ac89e23.png)

# Розташування мого публічного ключа SSH на комп'ютері
![1](https://user-images.githubusercontent.com/36934766/123948957-a9b7e100-d9aa-11eb-9db9-a89106482787.png)

# Переходимо на "Робочий стіл"
![2](https://user-images.githubusercontent.com/36934766/123949563-6316b680-d9ab-11eb-8fb3-7b7e870982e1.png)

# Клонуємо репозиторій через протокол SSH
Спочатку копіюємо SSH URL
![3](https://user-images.githubusercontent.com/36934766/123950242-239c9a00-d9ac-11eb-8589-4a90e3402cd7.png)

Потім клонуємо на "Робочий стіл"
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
Бачимо, що push відхилено

![image_2021-06-30_15-20-06](https://user-images.githubusercontent.com/36934766/123961285-da9f1280-d9b8-11eb-8b94-b49057fbf37f.png)

# Виправляємо помилку за допомогою команди git pull --rebase, що прибирає локальні комміти, оновлює гілку, і потім після оновлення знову застосовує комміти
![image_2021-06-30_15-22-30](https://user-images.githubusercontent.com/36934766/123961358-ebe81f00-d9b8-11eb-9fc1-54963c11422e.png)

# Знову прописуємо git push origin
![image_2021-06-30_15-23-24](https://user-images.githubusercontent.com/36934766/123961465-0fab6500-d9b9-11eb-9a2d-f1dbcbb64d0f.png)

# Бачимо, що все вдалося, і зміни надійшли
![image_2021-06-30_15-26-13](https://user-images.githubusercontent.com/36934766/123961512-1e921780-d9b9-11eb-8765-a18439c260cc.png)
