import http.client
import json #Модуль Python, який дозволяє кодувати і декодувати дані в зручному форматі
import tkinter #модуль Python для створення додатків з графічним інтерфейсом користувача
from tkinter import * #імпортує всі функції
import tkinter.messagebox #він використовується для відображення вікон повідомлень у калькуляторі на python

def button_hover(smth): #для того, щоб змінювався колір тоді, коли наводимо на кнопку
    input["bg"] = "#49B92F"

def button_hover_leave(smth): #для того, щоб після прибирання курсора колір кнопки змінювався на заданий
    input["bg"] = "SystemButtonFace"

def button_hover1(smth):
    rel["bg"] = "#C1C03E"

def button_hover_leave1(smth):
    rel["bg"] = "SystemButtonFace"

def on_close():
    response=tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?') #askyesno використовується для підказки користувачам із параметрами «так» або «ні», тобто boolean значення
    if response:
        root.destroy()

root = Tk() #створює вікно для програми
root.protocol('WM_DELETE_WINDOW',on_close) #метод протоколу для прив’язки видалення вікна до функції

root['bg'] = '#F0F0F0' #встановлює колір задньої частини програми
root.title('Country statistics related to COVID-19') #встановлює назву програми
root.wm_attributes('-alpha', 0.95) #встановлює прозорість програми
root.geometry('600x200+500+150') #встановлює розміри вікна програми

root.resizable(height=False, width=False) #робить так, що користувач не може змінювати розміри вікна програми для кращого користувацького інтерфейсу, бо присутнє значення False; також можна використати (0,0)

def get_statistic_of_country():

    # ******************************************** #

    # Code Snippets (VACCOVID)
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "a90f570cc2msh466368c6ddb5c48p1ea807jsn27b6b6bac8fd",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/countries", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data = json.loads(data.decode("utf-8")) #отримує дані з API та зберігає у json(розпаковуємо)
    # print(data)
    with open('all.json', 'w') as file:
        json.dump(data, file, indent=3) #пакуємо з відступами

    # ******************************************** #

    # Отримати індекс для країни :

    searchcountry = txtDisplay.get() #привласнює значення того, що отримано з дисплея

    if txtDisplay.index('end') == 0: #отримати індекс останнього символу у віджеті(якщо останній індекс дорівнює 0, він порожній)
        tkinter.messagebox.showwarning("Country statistics related to COVID-19", "Warning! Entry box is empty!") #попередження, що дисплей для вводу порожній
        statistic.set("")
        statistic_output.config(textvariable=statistic) #очищує виведення статистики попередньої країни
    else:
        def get_country_index(country):
            for index, item in enumerate(data): #enumerate використовується для спрощення переходу по колекціям, наприклад, спискам
                if item['Country'] == country:
                    return index
                txtDisplay.delete(0, END) #очищує дисплей від останього введеного значення
        country_index = get_country_index(searchcountry) #привласнює значення того, що було знайдено з функції get_country_index(country)
        
        my = data[country_index]
        print(my)
        with open('my.json', 'w') as file:
            json.dump(my, file, indent=3)
        #! check = data[country_index]['Country']

        #! if txtDisplay.get() != check:
            #! tkinter.messagebox.showerror("Country statistics related to COVID-19", "Error! Entered country does not exist!")

        # ******************************************** #

        # Статистика країни :

        totalcases = data[country_index]['TotalCases']
        newcases = data[country_index]['NewCases']
        totaldeaths = data[country_index]['TotalDeaths']
        newdeaths = data[country_index]['NewDeaths']
        totalrecovered = data[country_index]['TotalRecovered']
        newrecovered = data[country_index]['NewRecovered']

        # ******************************************** #

        # Повідомлення для статистики (Covid-19) :

        message = f'\t• TotalCases of Covid-19 in {searchcountry}: {totalcases}\n\t• NewCases of Covid-19 in {searchcountry}: {newcases}\n\t• TotalDeaths from Covid-19 in {searchcountry}: {totaldeaths}\n\t• NewDeaths from Covid-19 in {searchcountry}: {newdeaths}\n\t• TotalRecovered from Covid-19 in {searchcountry}: {totalrecovered}\n\t• NewRecovered from Covid-19 in {searchcountry}: {newrecovered}'
        statistic.set(message) #метод використовується для встановлення значення, що зберігається у tkinter-змінній

        # ******************************************** #

def reload():
    new_data = get_statistic_of_country #отримання нової статистики для країни
    input['command']=new_data

label_near_display = Label(root, text='Enter the country name:', font=('Helvetica', 10, 'bold'), relief="flat")
label_near_display.grid(row=0, column=0, ipady=10)

txtDisplay = Entry(root, width=30, fg='#000000', bd=13, relief="sunken", justify=CENTER, font=('Helvetica', 10, 'bold'))
txtDisplay.grid(row=0, column=1)

input = Button(root, text='Find statistics!', width=12, height=2, font=('Helvetica', 10, 'bold'), activebackground='#00FF00', bg='#FAFAFA', bd=1, relief="raised", command=get_statistic_of_country)
input.grid(row=0, column=2)
input.bind("<Enter>", button_hover) #функція прив'язки використовується для обробки подій, подія "<Enter>" наступає тоді, коли вказівник миші увійшов у віджет
input.bind("<Leave>", button_hover_leave) #подія "<Leave>" наступає тоді, коли вказівник миші залишає віджет

statistic = StringVar()
statistic_output = Label(root, textvariable=statistic, font=('Helvetica', 10, 'bold'), justify=LEFT)
statistic_output.grid(row=3, column=0, columnspan=2, ipady=20)

rel = Button(root, text='Reload', width=7, height=2, font=('Helvetica', 10, 'bold'), activebackground='#FFFF00', bg='#FAFAFA', bd=1, relief="raised", command=reload)
rel.grid(row=0, column=3)
rel.bind("<Enter>", button_hover1)
rel.bind("<Leave>", button_hover_leave1)

root.mainloop() #метод, який належить кореневому вікну, він повинен бути викликаний, щоб GUI функціонував належним чином