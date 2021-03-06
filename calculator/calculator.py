import tkinter as tk

disValue = 0
operator = {'+': 1,
            '-': 2,
            '/': 3,
            '*': 4,
            'C': 5,
            '=': 6
            }
stoValue = 0
opPre = 0


def test_check():
    print('test')


def number_click(value):
    # print('숫자 ', value)
    global disValue
    disValue = (disValue*10) + value
    str_value.set(str(disValue))


def clear():
    global disValue, operator, opPre
    disValue = 0
    operator = 0
    opPre = 0
    str_value.set(str(disValue))


def oprator_click(value):
    # print('명령 ', value)
    global disValue, operator, stoValue, opPre
    op = operator[value]
    if op == 5:  # C
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(str(disValue))
    elif op == 6:
        if opPre == 1:
            disValue = stoValue + disValue
        elif opPre == 2:
            disValue = stoValue - disValue
        elif opPre == 3:
            disValue = stoValue / disValue
        elif opPre == 4:
            disValue = stoValue * disValue

        str_value.set(str(disValue))
        disValue = 0
        stoValue = 0
        opPre = 0

    else:
        clear()

def button_click(value):
    print(value)
    try:
        value = int(value)
        number_click(value)

    except:
        oprator_click(value)


win = tk.Tk()
win.title('계산기')

str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable=str_value, justify='right', bg='white', fg='red')
dis.grid(column=0, row=0, columnspan=4, ipadx=100, ipady=20)

calItem = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

for i, items in enumerate(calItem):
    for k, item in enumerate(items):

        try:
            color = int(item)
            color = 'black'

        except:
            color = 'white'

        bt = tk.Button(win,
                       text=item,
                       width=10,
                       height=5,
                       background=color,
                       fg='green',
                       command=lambda cmd=item: button_click(cmd))
        bt.grid(column=k, row=(i + 1))

win.mainloop()
