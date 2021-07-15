import http.client
import json #модуль Python, який дозволяє кодувати і декодувати дані в зручному форматі
import telebot #модуль Python, який дає просту, але розширену реалізацію Python для API Telegram Bot
import os #модуль Python, який забезпечує функції взаємодії з поточною операційною системою; для взаємодії з файловою системою

from telebot import types #функція з модуля telebot для клавіатури

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

TOKEN = '1844435394:AAGatsjr8KPCNRP_0Wcu-WS7KfWRQfmEhoQ' #токен бота з @BotFather
bot = telebot.TeleBot(TOKEN) #використання TOKEN для присвоєння його до bot для подальшого запуску

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

@bot.message_handler(commands=['start']) #декоратор, який відстежує тип введеного бота повідомлення('/start')

# Функції, які будуть відповідати за обробку команди '/start'
def welcome(message): 
    sti1 = open('static/1.webp', 'rb') #відкриває файл(стікер) у двійковому форматі для читання
    bot.send_sticker(message.chat.id, sti1) #надсилає стікер(метод send_sticker), тобто повідомлення буде містити чат ID для конкретного повідомлення; воно буде утримуватися під ключем message.chat.id

    # Клавіатура :
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #задає клавіатуру за допомогою функції types і методу ReplyKeyboardMarkup з варіантами відповіді(параметр для зміни розміру клавіатури вертикально для оптимального прилягання)
    btn1 = types.KeyboardButton("🌐 Current statistics of 6 countries") #задає кнопку за допомогою функції types і методу KeyboardButton
    btn2 = types.KeyboardButton("↺ Reload")
    # btn3 = types.KeyboardButton("❔ Enter the country name")
    
    # Додає кнопки на клавіатуру :
    markup.add(btn1) 
    markup.add(btn2)
    # markup.add(btn3)

    bot.send_message(message.chat.id, "Welcome, <strong>{0.first_name}</strong>!\nI am a <b>{1.first_name}</b> bot which is created for country statistics related to COVID-19.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

def get_txt(message):
    txt = open("InfoFromVACCOVID.txt", "w") #створює текствоий файл

    text = ""
    text += f"\n\t***************************************"
    text += f"\n\t• TotalCases of Covid-19 in USA: {totalcases1}\n\t• NewCases of Covid-19 in USA: {newcases1}\n\t• TotalDeaths from Covid-19 in USA: {totaldeaths1}\n\t• NewDeaths from Covid-19 in USA: {newdeaths1}\n\t• TotalRecovered from Covid-19 in USA: {totalrecovered1}\n\t• NewRecovered from Covid-19 in USA: {newrecovered1}"
    text += f"\n\t***************************************"
    text += f"\n\t• TotalCases of Covid-19 in India: {totalcases2}\n\t• NewCases of Covid-19 in India: {newcases2}\n\t• TotalDeaths from Covid-19 in India: {totaldeaths2}\n\t• NewDeaths from Covid-19 in India: {newdeaths2}\n\t• TotalRecovered from Covid-19 in India: {totalrecovered2}\n\t• NewRecovered from Covid-19 in India: {newrecovered2}"
    text += f"\n\t***************************************"
    text += f"\n\t• TotalCases of Covid-19 in Brazil: {totalcases3}\n\t• NewCases of Covid-19 in Brazil: {newcases3}\n\t• TotalDeaths from Covid-19 in Brazil: {totaldeaths3}\n\t• NewDeaths from Covid-19 in Brazil: {newdeaths3}\n\t• TotalRecovered from Covid-19 in Brazil: {totalrecovered3}\n\t• NewRecovered from Covid-19 in Brazil: {newrecovered3}"
    text += f"\n\t***************************************"
    text += f"\n\t• TotalCases of Covid-19 in Russia: {totalcases4}\n\t• NewCases of Covid-19 in Russia: {newcases4}\n\t• TotalDeaths from Covid-19 in Russia: {totaldeaths4}\n\t• NewDeaths from Covid-19 in Russia: {newdeaths4}\n\t• TotalRecovered from Covid-19 in Russia: {totalrecovered4}\n\t• NewRecovered from Covid-19 in Russia: {newrecovered4}"
    text += f"\n\t***************************************"
    text += f"\n\t• TotalCases of Covid-19 in France: {totalcases5}\n\t• NewCases of Covid-19 in France: {newcases5}\n\t• TotalDeaths from Covid-19 in France: {totaldeaths5}\n\t• NewDeaths from Covid-19 in France: {newdeaths5}\n\t• TotalRecovered from Covid-19 in France: {totalrecovered5}\n\t• NewRecovered from Covid-19 in France: {newrecovered5}"
    text += f"\n\t***************************************"
    text += f"\n\t• TotalCases of Covid-19 in UK: {totalcases6}\n\t• NewCases of Covid-19 in UK: {newcases6}\n\t• TotalDeaths from Covid-19 in UK: {totaldeaths6}\n\t• NewDeaths from Covid-19 in UK: {newdeaths6}\n\t• TotalRecovered from Covid-19 in UK: {totalrecovered6}\n\t• NewRecovered from Covid-19 in UK: {newrecovered6}"
    text += f"\n\t***************************************"
    txt.write(text) #записали дані в текстовий файл
    txt.close() #після кожної операції над файлом бажано його закривати, щоб не було помилок

    txt = open("InfoFromVACCOVID.txt", "r") #відкрити для читання
    bot.send_document(message.message.chat.id, txt) #надсилає текстовий файл

    # Ловимо виняток(PermissionError(13, 'Процесс не может получить доступ к файлу, так как этот файл занят другим процессом')) :
    try:
        if os.access("InfoFromVACCOVID.txt", os.R_OK and os.X_OK): #метод access модуля os використовує реальний uid / gid (ідентифікатори) для тестування доступу до шляху (R_OK and X_OK значення, що передаються як параметр access(), щоб перевірити читабельність та виконуваності шляху відповідно)
            os.remove("InfoFromVACCOVID.txt") #видаліть шлях до текстового файлу
    except PermissionError: #процесс не может получить доступ к файлу, так как этот файл занят другим процессом
        pass #конструкція except: pass по суті заглушає будь-які виняткові умови, що виникають під час виконання коду, описаного в блоці try:

@bot.message_handler(content_types=['text']) #декоратор, який відстежує тип введеного бота повідомлення('text'), який можна використовувати для кнопок та введеного значення в поле
def buttons(message):
    if message.chat.type == 'private':
        txtfile = types.InlineKeyboardMarkup() #задає вбудовану клавіатуру за допомогою функції types і методу InlineKeyboardMarkup
        btnget_textfile = types.InlineKeyboardButton("Get txtfile of the current statistics of 6 countries ✉", callback_data="for_txtfile") #задає вбудовану кнопку за допомогою функції types і методу InlineKeyboardButton
        txtfile.add(btnget_textfile) #додає вбудовану кнопку на вбудовану клавіатуру

        if message.text == '🌐 Current statistics of 6 countries': #якщо введене повідомлення дорівнює тексту(у нашому випадку кнопці з текстом)
            sti2 = open('static/2.webp', 'rb')
            bot.send_sticker(message.chat.id, sti2)

            text = ""
            text += f"\n***************************************"
            text += f"\n\t• TotalCases of Covid-19 in USA: {totalcases1}\n\t• NewCases of Covid-19 in USA: {newcases1}\n\t• TotalDeaths from Covid-19 in USA: {totaldeaths1}\n\t• NewDeaths from Covid-19 in USA: {newdeaths1}\n\t• TotalRecovered from Covid-19 in USA: {totalrecovered1}\n\t• NewRecovered from Covid-19 in USA: {newrecovered1}"
            text += f"\n***************************************"
            text += f"\n\t• TotalCases of Covid-19 in India: {totalcases2}\n\t• NewCases of Covid-19 in India: {newcases2}\n\t• TotalDeaths from Covid-19 in India: {totaldeaths2}\n\t• NewDeaths from Covid-19 in India: {newdeaths2}\n\t• TotalRecovered from Covid-19 in India: {totalrecovered2}\n\t• NewRecovered from Covid-19 in India: {newrecovered2}"
            text += f"\n***************************************"
            text += f"\n\t• TotalCases of Covid-19 in Brazil: {totalcases3}\n\t• NewCases of Covid-19 in Brazil: {newcases3}\n\t• TotalDeaths from Covid-19 in Brazil: {totaldeaths3}\n\t• NewDeaths from Covid-19 in Brazil: {newdeaths3}\n\t• TotalRecovered from Covid-19 in Brazil: {totalrecovered3}\n\t• NewRecovered from Covid-19 in Brazil: {newrecovered3}"
            text += f"\n***************************************"
            text += f"\n\t• TotalCases of Covid-19 in Russia: {totalcases4}\n\t• NewCases of Covid-19 in Russia: {newcases4}\n\t• TotalDeaths from Covid-19 in Russia: {totaldeaths4}\n\t• NewDeaths from Covid-19 in Russia: {newdeaths4}\n\t• TotalRecovered from Covid-19 in Russia: {totalrecovered4}\n\t• NewRecovered from Covid-19 in Russia: {newrecovered4}"
            text += f"\n***************************************"
            text += f"\n\t• TotalCases of Covid-19 in France: {totalcases5}\n\t• NewCases of Covid-19 in France: {newcases5}\n\t• TotalDeaths from Covid-19 in France: {totaldeaths5}\n\t• NewDeaths from Covid-19 in France: {newdeaths5}\n\t• TotalRecovered from Covid-19 in France: {totalrecovered5}\n\t• NewRecovered from Covid-19 in France: {newrecovered5}"
            text += f"\n***************************************"
            text += f"\n\t• TotalCases of Covid-19 in UK: {totalcases6}\n\t• NewCases of Covid-19 in UK: {newcases6}\n\t• TotalDeaths from Covid-19 in UK: {totaldeaths6}\n\t• NewDeaths from Covid-19 in UK: {newdeaths6}\n\t• TotalRecovered from Covid-19 in UK: {totalrecovered6}\n\t• NewRecovered from Covid-19 in UK: {newrecovered6}"
            text += f"\n***************************************"
            
            bot.send_message(message.chat.id, text, reply_markup=txtfile)
            sti3 = open('static/3.webp', 'rb')
            bot.send_sticker(message.chat.id, sti3)

        elif message.text == '↺ Reload':

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

            bot.send_message(message.chat.id, '<em><strong>Reloaded!</strong></em>', parse_mode='html')
            sti4 = open('static/4.webp', 'rb')
            bot.send_sticker(message.chat.id, sti4)

        elif message.text == str(message.text): #якщо введене повідомлення є текстом, тобто str(це потрібно для того, щоб можна було вводити назву країни для пошуку її статистики; також через те, що в нас використовується список й індекси, а тому str обов'язковий)

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

            for country in data: #метод loop, тобто для кожного входження country в data(список статистики)
                if str(message.text) == country['Country']: #якщо наша послідовність символів з повідомлення дорівнює country з індексом-ключем 'Country'

                    searchcountry = message.text

                    def get_country_index(country):
                        for index, item in enumerate(data): #enumerate використовується для спрощення переходу по колекціям, наприклад, спискам
                            if item['Country'] == country:
                                return index
                    country_index = get_country_index(searchcountry) #привласнює значення того, що було знайдено з функції get_country_index(country)
                    
                    my = data[country_index]
                    with open('my.json', 'w') as file:
                        json.dump(my, file, indent=3)
                    
                    # ******************************************** #

                    # Статистика країни :

                    totalcases = data[country_index]['TotalCases']
                    newcases = data[country_index]['NewCases']
                    totaldeaths = data[country_index]['TotalDeaths']
                    newdeaths = data[country_index]['NewDeaths']
                    totalrecovered = data[country_index]['TotalRecovered']
                    newrecovered = data[country_index]['NewRecovered']

                    # ******************************************** #

                    text = ""
                    text += f"\n***************************************"
                    text += f"\n\t• TotalCases of Covid-19 in {searchcountry}: {totalcases}\n\t• NewCases of Covid-19 in {searchcountry}: {newcases}\n\t• TotalDeaths from Covid-19 in {searchcountry}: {totaldeaths}\n\t• NewDeaths from Covid-19 in {searchcountry}: {newdeaths}\n\t• TotalRecovered from Covid-19 in {searchcountry}: {totalrecovered}\n\t• NewRecovered from Covid-19 in {searchcountry}: {newrecovered}"
                    text += f"\n***************************************"

                    bot.send_message(message.chat.id, text)
                    sti5 = open('static/5.webp', 'rb')
                    bot.send_sticker(message.chat.id, sti5)
            
                elif country not in data: #якщо country немає в data
                    if str(message.text) != country['Country']:
                        bot.send_message(message.chat.id, '<b>Error! Incorrect input!</b>', parse_mode='html')
                        sti6 = open('static/6.webp', 'rb')
                        bot.send_sticker(message.chat.id, sti6)

@bot.callback_query_handler(func=lambda call: True) #обробка натискання на кнопку вбудованої клавіатури
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'for_txtfile':
                get_txt(call)
                bot.send_message(call.message.chat.id, '<b>Done!</b>', parse_mode='html')

            # Видаляє вбудовану кнопку і показує текст :
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🌐 Current statistics of 6 countries", reply_markup=None)
            # Показує повідомлення після натискання вбудованої кнопки :
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="The txtfile of the current statistics of 6 countries ✉ was created!")

    except Exception as e: #приймає лише винятки, які призначено зловити
        print(repr(e)) #якщо збираєтеся роздрукувати виняток

# Запуск: 
bot.polling(none_stop=True)
