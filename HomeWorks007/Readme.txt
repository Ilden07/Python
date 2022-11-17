1. Перед тем как начать работать, нужно установить все нужные компоненты, нам нужно скачать только Tkinter, 
для этого для Python прописываем команду PIP:

>>> pip install tk

2. Первым делом нужно импортировать нужные компоненты и создать переменные 
которые нам пригодятся:

>>> from tkinter import *
>>> from decimal import *

3. После импортирования, мы создаём приложение и задаём ему заголовок:
>>> root = Tk()
>>> root.title('Calculator')

4. После создаём кортеж кнопок, где каждый картеж, это отдельная строчка кнопок в приложение:
>>> buttons = (('7', '8', '9', '/', '4'),
              ('4', '5', '6', '*', '4'),
              ('1', '2', '3', '-', '4'),
              ('0', '.', '=', '+', '4')
              )

5. Далее мы создаём переменную activeStr, которая отвечает за наспанные числа в строчки ввода, и вторая переменная это список,
 чисел и команда которые нужно будет выполнить.
 >>> activeStr = ''
 >>> stack = []

6. Дальше создаём функцию, которая будет считать получившийся результат:

>>>def calculate():
       global stack
       global label
       result = 0
       operand2 = Decimal(stack.pop())
       operation = stack.pop()
       operand1 = Decimal(stack.pop())
 
       if operation == '+':
           result = operand1 + operand2
       if operation == '-':
           result = operand1 - operand2
       if operation == '/':
           result = operand1 / operand2
       if operation == '*':
           result = operand1 * operand2
       label.configure(text=str(result))

7. Как видите в начале функции мы всё раскладываем на числа которые мы получаем и знаки на которые мы нажали, 
потом всё зависимо от от знака мы считаем вместе эти два числа и в вставляем это в нашу строку ввода.

8. Теперь перейдём к функции которая будет обрабатывать клик на кнопки:
>>> ef click(text):
        global activeStr
        global stack
        if text == 'CE':
            stack.clear()
            activeStr = ''
            label.configure(text='0')
        elif '0' <= text <= '9':
            activeStr += text
            label.configure(text=activeStr)
        elif text == '.':
            if activeStr.find('.') == -1:
                activeStr += text
                label.configure(text=activeStr)
        else:
            if len(stack) >= 2:
                stack.append(label['text'])
                calculate()
                stack.clear()
                stack.append(label['text'])
                activeStr = ''
                if text != '=':
                    stack.append(text)
            else:
                if text != '=':
                    stack.append(label['text'])
                    stack.append(text)
                    activeStr = ''
                    label.configure(text='0')
В начале мы проверяем, нажата ли кнопка CE, если да, то тогда всё удаляем и выводим ноль, иначе если были нажаты цифры, 
то добавляет это всё в поле ввода, если нажата точка, то тоже добавляем в поле.
Иначе, проверяем если у нас stack больше или равен двум, то считаем что у нас получилось и выводим число в поле,
которое получилось, и, если не было нажата равно, то вставляем это число в stack.
Иначе опять проверяем не было ли нажата равно, если нет, то всё так же добавляем значения в список stack.

9.Будем создавать таблицу но вначале сделаем поле, и потом уже саму таблицу, после того как мы это сделаем, 
создадим  кнопку «CE», дальше  остальные кнопки, по четыре столбца, это важно, и последние задаём конфигурации 
для строчки и столбцов:
>>> label = Label(root, text='0', width=35)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")
 
    button = Button(root, text='CE', command=lambda text='CE': click(text))
    button.grid(row=1, column=3, sticky="nsew")
    for row in range(4):
        for col in range(4):
            button = Button(root, text=buttons[row][col],
                    command=lambda row=row, col=col: click(buttons[row][col]))
            button.grid(row=row + 2, column=col, sticky="nsew")
 
    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(4, weight=1)
 
    root.mainloop()