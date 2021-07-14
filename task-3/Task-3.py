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
root.geometry('1200x400+200+150') #встановлює розміри вікна програми

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

    # Статистика USA:

    totalcases1 = data[0]['TotalCases']
    newcases1 = data[0]['NewCases']
    totaldeaths1 = data[0]['TotalDeaths']
    newdeaths1 = data[0]['NewDeaths']
    totalrecovered1 = data[0]['TotalRecovered']
    newrecovered1 = data[0]['NewRecovered']

    # ******************************************** #

    # Статистика India:

    totalcases2 = data[1]['TotalCases']
    newcases2 = data[1]['NewCases']
    totaldeaths2 = data[1]['TotalDeaths']
    newdeaths2 = data[1]['NewDeaths']
    totalrecovered2 = data[1]['TotalRecovered']
    newrecovered2 = data[1]['NewRecovered']

    # ******************************************** #

    # Статистика Brazil:

    totalcases3 = data[2]['TotalCases']
    newcases3 = data[2]['NewCases']
    totaldeaths3 = data[2]['TotalDeaths']
    newdeaths3 = data[2]['NewDeaths']
    totalrecovered3 = data[2]['TotalRecovered']
    newrecovered3 = data[2]['NewRecovered']

    # ******************************************** #

    # Статистика Russia:

    totalcases4 = data[3]['TotalCases']
    newcases4 = data[3]['NewCases']
    totaldeaths4 = data[3]['TotalDeaths']
    newdeaths4 = data[3]['NewDeaths']
    totalrecovered4 = data[3]['TotalRecovered']
    newrecovered4 = data[3]['NewRecovered']

    # ******************************************** #

    # Статистика France:

    totalcases5 = data[4]['TotalCases']
    newcases5 = data[4]['NewCases']
    totaldeaths5 = data[4]['TotalDeaths']
    newdeaths5 = data[4]['NewDeaths']
    totalrecovered5 = data[4]['TotalRecovered']
    newrecovered5 = data[4]['NewRecovered']

    # ******************************************** #

    # Статистика UK:

    totalcases6 = data[6]['TotalCases']
    newcases6 = data[6]['NewCases']
    totaldeaths6 = data[6]['TotalDeaths']
    newdeaths6 = data[6]['NewDeaths']
    totalrecovered6 = data[6]['TotalRecovered']
    newrecovered6 = data[6]['NewRecovered']
    
    # ******************************************** #

    # Повідомлення для статистики в USA(Covid-19) :

    message = f'\t• TotalCases of Covid-19 in USA: {totalcases1}\n\t• NewCases of Covid-19 in USA: {newcases1}\n\t• TotalDeaths from Covid-19 in USA: {totaldeaths1}\n\t• NewDeaths from Covid-19 in USA: {newdeaths1}\n\t• TotalRecovered from Covid-19 in USA: {totalrecovered1}\n\t• NewRecovered from Covid-19 in USA: {newrecovered1}'
    statisticUSA.set(message) #метод використовується для встановлення значення, що зберігається у tkinter-змінній

    # ******************************************** #

    # Повідомлення для статистики в India(Covid-19) :

    message = f'\t• TotalCases of Covid-19 in India: {totalcases2}\n\t• NewCases of Covid-19 in India: {newcases2}\n\t• TotalDeaths from Covid-19 in India: {totaldeaths2}\n\t• NewDeaths from Covid-19 in India: {newdeaths2}\n\t• TotalRecovered from Covid-19 in India: {totalrecovered2}\n\t• NewRecovered from Covid-19 in India: {newrecovered2}'
    statisticIndia.set(message) #метод використовується для встановлення значення, що зберігається у tkinter-змінній

    # ******************************************** #

    # Повідомлення для статистики в Brazil(Covid-19) :

    message = f'\t• TotalCases of Covid-19 in Brazil: {totalcases3}\n\t• NewCases of Covid-19 in Brazil: {newcases3}\n\t• TotalDeaths from Covid-19 in Brazil: {totaldeaths3}\n\t• NewDeaths from Covid-19 in Brazil: {newdeaths3}\n\t• TotalRecovered from Covid-19 in Brazil: {totalrecovered3}\n\t• NewRecovered from Covid-19 in Brazil: {newrecovered3}'
    statisticBrazil.set(message) #метод використовується для встановлення значення, що зберігається у tkinter-змінній

    # ******************************************** #

    # Повідомлення для статистики в Russia(Covid-19) :

    message = f'\t• TotalCases of Covid-19 in Russia: {totalcases4}\n\t• NewCases of Covid-19 in Russia: {newcases4}\n\t• TotalDeaths from Covid-19 in Russia: {totaldeaths4}\n\t• NewDeaths from Covid-19 in Russia: {newdeaths4}\n\t• TotalRecovered from Covid-19 in Russia: {totalrecovered4}\n\t• NewRecovered from Covid-19 in Russia: {newrecovered4}'
    statisticRussia.set(message) #метод використовується для встановлення значення, що зберігається у tkinter-змінній

    # ******************************************** #

    # Повідомлення для статистики в France(Covid-19) :

    message = f'\t• TotalCases of Covid-19 in France: {totalcases5}\n\t• NewCases of Covid-19 in France: {newcases5}\n\t• TotalDeaths from Covid-19 in France: {totaldeaths5}\n\t• NewDeaths from Covid-19 in France: {newdeaths5}\n\t• TotalRecovered from Covid-19 in France: {totalrecovered5}\n\t• NewRecovered from Covid-19 in France: {newrecovered5}'
    statisticFrance.set(message) #метод використовується для встановлення значення, що зберігається у tkinter-змінній

    # ******************************************** #

    # Повідомлення для статистики в UK(Covid-19) :

    message = f'\t• TotalCases of Covid-19 in UK: {totalcases6}\n\t• NewCases of Covid-19 in UK: {newcases6}\n\t• TotalDeaths from Covid-19 in UK: {totaldeaths6}\n\t• NewDeaths from Covid-19 in UK: {newdeaths6}\n\t• TotalRecovered from Covid-19 in UK: {totalrecovered6}\n\t• NewRecovered from Covid-19 in UK: {newrecovered6}'
    statisticUK.set(message) #метод використовується для встановлення значення, що зберігається у tkinter-змінній

    # ******************************************** #

label_near_display = Label(root, text='Enter the country name:', font=('Helvetica', 10, 'bold'), relief="flat")
label_near_display.grid(row=0, column=0, ipady=10, sticky=W)

txtDisplay = Entry(root, width=30, fg='#000000', bd=13, relief="sunken", justify=CENTER, font=('Helvetica', 10, 'bold'))
txtDisplay.grid(row=0, column=1, sticky=W)

input = Button(root, text='Find statistics!', width=12, height=2, font=('Helvetica', 10, 'bold'), activebackground='#00FF00', bg='#FAFAFA', bd=1, relief="raised", command=get_statistic_of_country)
input.grid(row=0, column=2, sticky=W, padx=5)
input.bind("<Enter>", button_hover) #функція прив'язки використовується для обробки подій, подія "<Enter>" наступає тоді, коли вказівник миші увійшов у віджет
input.bind("<Leave>", button_hover_leave) #подія "<Leave>" наступає тоді, коли вказівник миші залишає віджет

statistic = StringVar()
statistic_output = Label(root, textvariable=statistic, font=('Helvetica', 10, 'bold'), justify=LEFT)
statistic_output.grid(row=3, column=0, columnspan=2, ipady=5)

statisticUSA = StringVar()
statisticUSA_output = Label(root, textvariable=statisticUSA, font=('Helvetica', 10, 'bold'), justify=LEFT)
statisticUSA_output.grid(row=3, column=2, columnspan=2, ipady=5)

statisticIndia = StringVar()
statisticIndia_output = Label(root, textvariable=statisticIndia, font=('Helvetica', 10, 'bold'), justify=LEFT)
statisticIndia_output.grid(row=3, column=4, columnspan=2, ipady=5)

statisticBrazil = StringVar()
statisticBrazil_output = Label(root, textvariable=statisticBrazil, font=('Helvetica', 10, 'bold'), justify=LEFT)
statisticBrazil_output.grid(row=4, column=2, columnspan=2, ipady=5)

statisticRussia = StringVar()
statisticRussia_output = Label(root, textvariable=statisticRussia, font=('Helvetica', 10, 'bold'), justify=LEFT)
statisticRussia_output.grid(row=4, column=4, columnspan=2, ipady=5)

statisticFrance = StringVar()
statisticFrance_output = Label(root, textvariable=statisticFrance, font=('Helvetica', 10, 'bold'), justify=LEFT)
statisticFrance_output.grid(row=5, column=2, columnspan=2, ipady=5)

statisticUK = StringVar()
statisticUK_output = Label(root, textvariable=statisticUK, font=('Helvetica', 10, 'bold'), justify=LEFT)
statisticUK_output.grid(row=5, column=4, columnspan=2, ipady=5)

rel = Button(root, text='Reload', width=7, height=2, font=('Helvetica', 10, 'bold'), activebackground='#FFFF00', bg='#FAFAFA', bd=1, relief="raised", command=reload)
rel.grid(row=0, column=2, columnspan=1, padx=70)
rel.bind("<Enter>", button_hover1)
rel.bind("<Leave>", button_hover_leave1)

reload() #виклик функції без використання кнопки
root.mainloop() #метод, який належить кореневому вікну, він повинен бути викликаний, щоб GUI функціонував належним чином
