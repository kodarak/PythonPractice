import tkinter #модуль Python для створення додатків з графічним інтерфейсом користувача
import numpy #модуль Python, який надає загальні математичні і числові операції
import math #вбудований модуль, який можна використовувати для математичних завдань
#!import bitstring #модуль Python, який може перетворювати рядки, цілі числа, байти, шістнадцяткові числа в бітові рядки
from tkinter import * #імпортує всі функції
import tkinter.messagebox #він використовується для відображення вікон повідомлень у калькуляторі на python

# ****************************************************************************************************** #

root = Tk() #створює вікно для програми

root['bg'] = '#E6E6E6' #встановлює колір задньої частини програми
root.title('Калькулятор') #встановлює назву програми
root.wm_attributes('-alpha', 0.95) #встановлює прозорість програми
root.geometry('482x568+450+90') #встановлює розміри вікна програми

root.resizable(height=False, width=False) #робить так, що користувач не може змінювати розміри вікна програми для кращого користувацького інтерфейсу, бо присутнє значення False; також можна використати (0,0)

calc = Frame(root)
calc.grid() #табличний спосіб розміщення

# ****************************************************************************************************** #

# Визначаємо hover для різних кнопок

def button_hover(smth): #для того, щоб змінювався колір тоді, коли наводимо на кнопку
    btnClearEntry["bg"] = "#D7D7D7"

def button_hover_leave(smth): #для того, щоб після прибирання курсора колір кнопки змінювався на заданий
    btnClearEntry["bg"] = "SystemButtonFace"

def button_hover1(smth):
    btnClearAll["bg"] = "#D7D7D7"

def button_hover_leave1(smth):
    btnClearAll["bg"] = "SystemButtonFace"

def button_hover2(smth):
    btnClearLast["bg"] = "#D7D7D7"

def button_hover_leave2(smth):
    btnClearLast["bg"] = "SystemButtonFace"

def button_hover3(smth):
    btnbin["bg"] = "#D7D7D7"

def button_hover_leave3(smth):
    btnbin["bg"] = "SystemButtonFace"

def button_hover4(smth):
    btnAdd["bg"] = "#D7D7D7"

def button_hover_leave4(smth):
    btnAdd["bg"] = "SystemButtonFace"

def button_hover5(smth):
    btnSub["bg"] = "#D7D7D7"

def button_hover_leave5(smth):
    btnSub["bg"] = "SystemButtonFace"

def button_hover6(smth):
    btnMul["bg"] = "#D7D7D7"

def button_hover_leave6(smth):
    btnMul["bg"] = "SystemButtonFace"

def button_hover7(smth):
    btnDiv["bg"] = "#D7D7D7"

def button_hover_leave7(smth):
    btnDiv["bg"] = "SystemButtonFace"

def button_hover8(smth):
    btnDot["bg"] = "#D7D7D7"

def button_hover_leave8(smth):
    btnDot["bg"] = "SystemButtonFace"

def button_hover9(smth):
    btnEquals["bg"] = "#C8A759"

def button_hover_leave9(smth):
    btnEquals["bg"] = "#DBC99A"

def button_hover10(smth):
    btnsin["bg"] = "#D7D7D7"

def button_hover_leave10(smth):
    btnsin["bg"] = "SystemButtonFace"

def button_hover11(smth):
    btncos["bg"] = "#D7D7D7"

def button_hover_leave11(smth):
    btncos["bg"] = "SystemButtonFace"

def button_hover12(smth):
    btntan["bg"] = "#D7D7D7"

def button_hover_leave12(smth):
    btntan["bg"] = "SystemButtonFace"

def button_hover13(smth):
    btnctg["bg"] = "#D7D7D7"

def button_hover_leave13(smth):
    btnctg["bg"] = "SystemButtonFace"

def button_hover14(smth):
    btnlog["bg"] = "#D7D7D7"

def button_hover_leave14(smth):
    btnlog["bg"] = "SystemButtonFace"

def button_hover15(smth):
    btnln["bg"] = "#D7D7D7"

def button_hover_leave15(smth):
    btnln["bg"] = "SystemButtonFace"

def button_hover16(smth):
    btnmodulo["bg"] = "#D7D7D7"

def button_hover_leave16(smth):
    btnmodulo["bg"] = "SystemButtonFace"

# ****************************************************************************************************** #

# Класи для всіх кнопок в калькуляторі

class Calc():
    def __init__(self): #належить до групи методів перевантаження операторів; конструктор об'єктів класу в ООП
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False

    def enter_number(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def overall_value(self): #вивід значення
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self, value): #те, що буде показуватися після запуска калькулятора й після деякий операцій(коли буде використовуватися .display)
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            if self.current == 0:
                tkinter.messagebox.showerror("Калькулятор", "Помилка!")
            else:
                self.total /= self.current
        if self.op == "mod":
            if self.current == 0:
                tkinter.messagebox.showerror("Калькулятор", "Помилка!")
            else:
                self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def backspace(self): #видалення по одному елементу в дисплеї
        if self.current == float(self.current): #помилка, бо описує об'єкти, які є "containers", тобто вони містять інші об'єкти (subscriptable)
            tkinter.messagebox.showerror("Калькулятор", "Помилка!")
        else:
            self.current = self.current[:-1]
            self.display(self.current)
    
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True
    
    def Clear_All_Entry(self):
        self.Clear_Entry()
        self.total=0

    def convert_to_bin(self):
        if self.current == float(self.current):
            tkinter.messagebox.showerror("Калькулятор", "Помилка!")
        elif "." in self.current:
            tkinter.messagebox.showerror("Калькулятор", "Помилка!")
        else:
            self.result = False
            self.current = numpy.binary_repr(int(txtDisplay.get()), width=None)
            #!self.current = bitstring.BitArray(float(txtDisplay.get()), length=None)
            self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
    
    def ctg(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))/math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def ln(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()

# ****************************************************************************************************** #

# Дисплей для калькулятора

txtDisplay = Entry(calc, font=('Helvetica', 20, 'bold'), bg='#E6E6E6', fg='black', bd=30, relief="flat", width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0") #відразу вставити в рядок дисплея число 0

# ****************************************************************************************************** #

# Цифрова клавіатура для калькулятора 

numbers = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg='#FAFAFA', activebackground='#B2AEB5', fg='black', font=('Helvetica',20,'bold'), bd=1, relief="raised", text=numbers[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=numbers[i]:added_value.enter_number(x)
        i+=1 

# ****************************************************************************************************** #

# Оформлення кнопок для основних функцій у калькуляторі

btnClearEntry = Button(calc, text=chr(67)+chr(69), width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="groove", command=added_value.Clear_Entry)
btnClearEntry.grid(row=1, column= 0, pady = 12)
btnClearEntry.bind("<Enter>", button_hover)
btnClearEntry.bind("<Leave>", button_hover_leave)

btnClearAll = Button(calc, text=chr(67), width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5',fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="groove", command=added_value.Clear_All_Entry)
btnClearAll.grid(row=1, column= 1, pady = 1)
btnClearAll.bind("<Enter>", button_hover1)
btnClearAll.bind("<Leave>", button_hover_leave1)

btnClearLast = Button(calc, text="\u2190", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="groove", command=added_value.backspace)
btnClearLast.grid(row=1, column= 2, pady = 1)
btnClearLast.bind("<Enter>", button_hover2)
btnClearLast.bind("<Leave>", button_hover_leave2)

btnbin = Button(calc, text="bin", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20), bd=1, relief="groove", command=added_value.convert_to_bin)
btnbin.grid(row=1, column= 3, pady = 1)
btnbin.bind("<Enter>", button_hover3)
btnbin.bind("<Leave>", button_hover_leave3)

btnAdd = Button(calc, text="+", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20), bd=1, relief="groove", command=lambda:added_value.operation("add"))
btnAdd.grid(row=2, column= 3, pady = 1)
btnAdd.bind("<Enter>", button_hover4)
btnAdd.bind("<Leave>", button_hover_leave4)

btnSub = Button(calc, text="-", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20), bd=1, relief="groove", command=lambda:added_value.operation("sub"))
btnSub.grid(row=3, column= 3, pady = 1)
btnSub.bind("<Enter>", button_hover5)
btnSub.bind("<Leave>", button_hover_leave5)

btnMul = Button(calc, text="x", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20), bd=1, relief="groove", command=lambda:added_value.operation("multi"))
btnMul.grid(row=4, column= 3, pady = 1)
btnMul.bind("<Enter>", button_hover6)
btnMul.bind("<Leave>", button_hover_leave6)

btnDiv = Button(calc, text="/", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20), bd=1, relief="groove", command=lambda:added_value.operation("divide"))
btnDiv.grid(row=5, column= 3, pady = 1)
btnDiv.bind("<Enter>", button_hover7)
btnDiv.bind("<Leave>", button_hover_leave7)

btnDot = Button(calc, text=".", width=6, height=2, bg='#FAFAFA', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="raised", command=lambda:added_value.enter_number("."))
btnDot.grid(row=5, column= 0, pady = 1)
btnDot.bind("<Enter>", button_hover8)
btnDot.bind("<Leave>", button_hover_leave8)

btnZero = Button(calc, text="0", width=6, height=2, bg='#FAFAFA', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="raised", command=lambda:added_value.enter_number(0))
btnZero.grid(row=5, column= 1, pady = 1)

btnEquals = Button(calc, text="=", width=6, height=2, bg='#DBC99A', activebackground='#CC9E29', fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="raised", command=added_value.overall_value)
btnEquals.grid(row=5, column= 2, pady = 1)
btnEquals.bind("<Enter>", button_hover9)
btnEquals.bind("<Leave>", button_hover_leave9)

# ****************************************************************************************************** #

# Оформлення кнопок для додаткових функцій у калькуляторі

# Рядок 0:
btnsin = Button(calc, text="sin", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="groove", command=added_value.sin)
btnsin.grid(row=0, column= 4, pady = 1)
btnsin.bind("<Enter>", button_hover10)
btnsin.bind("<Leave>", button_hover_leave10)

btncos = Button(calc, text="cos", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica',20,'bold'), bd=1, relief="groove", command=added_value.cos)
btncos.grid(row=0, column= 5, pady = 1)
btncos.bind("<Enter>", button_hover11)
btncos.bind("<Leave>", button_hover_leave11)

# Рядок 1:
btntan = Button(calc, text="tan", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica',20,'bold'), bd=1, relief="groove", command=added_value.tan)
btntan.grid(row=1, column= 4, pady = 1)
btntan.bind("<Enter>", button_hover12)
btntan.bind("<Leave>", button_hover_leave12)

btnctg = Button(calc, text="ctg", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica',20,'bold'), bd=1, relief="groove", command=added_value.ctg)
btnctg.grid(row=1, column= 5, pady = 1)
btnctg.bind("<Enter>", button_hover13)
btnctg.bind("<Leave>", button_hover_leave13)

# Рядок 2:
btnlog = Button(calc, text="log",width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica',20,'bold'), bd=1, relief="groove", command=added_value.log10)
btnlog.grid(row=2, column= 4, pady = 1)
btnlog.bind("<Enter>", button_hover14)
btnlog.bind("<Leave>", button_hover_leave14)

btnln = Button(calc, text="ln", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica',20,'bold'), bd=1, relief="groove", command=added_value.ln)
btnln.grid(row=2, column= 5, pady = 1)
btnln.bind("<Enter>", button_hover15)
btnln.bind("<Leave>", button_hover_leave15)

# Рядок 3:
btnmodulo = Button(calc, text="%", width=6, height=2, bg='#F0F0F0', activebackground='#B2AEB5', fg='black', font=('Helvetica', 20, 'bold'), bd=1, relief="groove", command=lambda:added_value.operation("mod"))
btnmodulo.grid(row=3, column= 4, pady = 1)
btnmodulo.bind("<Enter>", button_hover16)
btnmodulo.bind("<Leave>", button_hover_leave16)

# ******************************************************************************************************************** #

# Функції для меню

def Exit():
    Exit = tkinter.messagebox.askyesno("Калькулятор", "Чи дійсно Ви хочете вийти?") #askyesno використовується для підказки користувачам із параметрами «так» або «ні», тобто boolean значення
    if Exit>0:
        root.destroy()
        return

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

def Expanded():
    root.resizable(width=False, height=False)
    root.geometry("718x568+0+0")

# ******************************************************************************************************************** #

#Меню для калькулятора, в якому присутні три команди

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0, activebackground="#DAA520")
menubar.add_cascade(label = 'Файл', menu = filemenu)
filemenu.add_command(label = "Основні функції", command = Standard)
filemenu.add_command(label = "Додаткові функції", command = Expanded)
filemenu.add_separator()
filemenu.add_command(label = "Вихід", command = Exit)

root.config(menu=menubar)

# ******************************************************************************************************************** #

root.mainloop() #метод, який належить кореневому вікну, він повинен бути викликаний, щоб GUI функціонував належним чином
