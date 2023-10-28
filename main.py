# Simple Calculator in Python using tkinter
import tkinter as tk
import customtkinter as ctk
import math
import os
from datetime import datetime

current_dir = os.getcwd()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

form = ""


def add_to_calculation(symbol):
    global form
    form += str(symbol)
    calculating_box.delete("0.0", "end")
    calculating_box.insert("0.0", form)


def transformation(word):
    new_word_1 = word.replace('√', 'math.sqrt')
    new_word_2 = new_word_1.replace('π', 'math.pi')
    new_word_3 = new_word_2.replace('sin', 'math.sin')
    new_word_4 = new_word_3.replace('cos', 'math.cos')
    new_word_5 = new_word_4.replace('tan', 'math.tan')
    new_word_6 = new_word_5.replace('ctg', '1/math.tan')
    new_word_7 = new_word_6.replace('power', '**')
    new_word_8 = new_word_7.replace('e', 'math.e')
    new_word_9 = new_word_8.replace('log10', 'math.log10')

    return new_word_9


def do_calculation():
    global form
    sentence_to_save = form
    word_to_calculate = transformation(form)

    try:
        result = str(round(eval(word_to_calculate), 4))
        form = ""
        calculating_box.delete(1.0, "end")
        calculating_box.insert(1.0, result)

    except:
        clear_field()
        calculating_box.insert(1.0, "Error")

    sentence_to_save += ('=' + result)
    saving_results(sentence_to_save)
    reading_results()


def delete_char():
    global form
    form = form[0:len(form) - 1]
    calculating_box.delete(1.0, "end")
    calculating_box.insert(1.0, form)


def clear_field():
    global form
    form = ""
    calculating_box.delete(1.0, "end")


def saving_results(word_to_save):
    local_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = word_to_save + '\t\t - \t' + local_dt + '\n'
    transformed_result = result.replace('π', 'pi')

    with open('results.txt', 'a+') as f:
        f.write(transformed_result)


def reading_results():
    with open('results.txt', 'r') as f:
        for line in f:
            results_box.insert(1.0, line)


# main objects
window = ctk.CTk()
window.geometry("700x700")
window.title('Simple Calculator')

frame = ctk.CTkFrame(master=window, corner_radius=25)
frame.pack(pady=20, padx=20, fill="both", expand=True)

calculating_box = ctk.CTkTextbox(master=frame, height=120, width=400, font=('Arial', 20))
calculating_box.place(rely=0.05, relx=0.1, anchor=ctk.CENTER)
calculating_box.pack(pady=20, padx=20, fill="both", expand=False)

results_box = ctk.CTkTextbox(master=window, height=120, width=500, font=('Arial', 20))
results_box.place(rely=0.05, relx=0.5, anchor=ctk.S)
results_box.pack(pady=20, padx=20, fill="both", expand=False)

# numbers buttons
button_1 = ctk.CTkButton(master=window, text='1', height=60, width=60, command=lambda: add_to_calculation(1))
button_1.place(relx=0.10, rely=0.3, anchor=ctk.CENTER)
button_2 = ctk.CTkButton(master=window, text='2', height=60, width=60, command=lambda: add_to_calculation(2))
button_2.place(relx=0.20, rely=0.3, anchor=ctk.CENTER)
button_3 = ctk.CTkButton(master=window, text='3', height=60, width=60, command=lambda: add_to_calculation(3))
button_3.place(relx=0.30, rely=0.3, anchor=ctk.CENTER)
button_4 = ctk.CTkButton(master=window, text='4', height=60, width=60, command=lambda: add_to_calculation(4))
button_4.place(relx=0.10, rely=0.4, anchor=ctk.CENTER)
button_5 = ctk.CTkButton(master=window, text='5', height=60, width=60, command=lambda: add_to_calculation(5))
button_5.place(relx=0.20, rely=0.4, anchor=ctk.CENTER)
button_6 = ctk.CTkButton(master=window, text='6', height=60, width=60, command=lambda: add_to_calculation(6))
button_6.place(relx=0.30, rely=0.4, anchor=ctk.CENTER)
button_7 = ctk.CTkButton(master=window, text='7', height=60, width=60, command=lambda: add_to_calculation(7))
button_7.place(relx=0.10, rely=0.5, anchor=ctk.CENTER)
button_8 = ctk.CTkButton(master=window, text='8', height=60, width=60, command=lambda: add_to_calculation(8))
button_8.place(relx=0.20, rely=0.5, anchor=ctk.CENTER)
button_9 = ctk.CTkButton(master=window, text='9', height=60, width=60, command=lambda: add_to_calculation(9))
button_9.place(relx=0.30, rely=0.5, anchor=ctk.CENTER)
button_0 = ctk.CTkButton(master=window, text='0', height=60, width=60, command=lambda: add_to_calculation(0))
button_0.place(relx=0.10, rely=0.6, anchor=ctk.CENTER)
button_dot = ctk.CTkButton(master=window, text='.', height=60, width=60, command=lambda: add_to_calculation('.'))
button_dot.place(relx=0.20, rely=0.6, anchor=ctk.CENTER)

button_pi = ctk.CTkButton(master=window, text='π', height=60, width=60, command=lambda: add_to_calculation('π'))
button_pi.place(relx=0.30, rely=0.6, anchor=ctk.CENTER)
button_e = ctk.CTkButton(master=window, text='e', height=60, width=60, command=lambda: add_to_calculation('e'))
button_e.place(relx=0.70, rely=0.3, anchor=ctk.CENTER)
button_open = ctk.CTkButton(master=window, text='(', height=60, width=60, command=lambda: add_to_calculation('('))
button_open.place(relx=0.50, rely=0.6, anchor=ctk.CENTER)
button_close = ctk.CTkButton(master=window, text=')', height=60, width=60, command=lambda: add_to_calculation(')'))
button_close.place(relx=0.60, rely=0.6, anchor=ctk.CENTER)

# calculationg buttons
button_plus = ctk.CTkButton(master=window, text='+', height=60, width=60, command=lambda: add_to_calculation('+'))
button_plus.place(relx=0.40, rely=0.3, anchor=ctk.CENTER)
button_minus = ctk.CTkButton(master=window, text='-', height=60, width=60, command=lambda: add_to_calculation('-'))
button_minus.place(relx=0.40, rely=0.4, anchor=ctk.CENTER)
button_mul = ctk.CTkButton(master=window, text='*', height=60, width=60, command=lambda: add_to_calculation('*'))
button_mul.place(relx=0.40, rely=0.5, anchor=ctk.CENTER)
button_div = ctk.CTkButton(master=window, text='/', height=60, width=60, command=lambda: add_to_calculation('/'))
button_div.place(relx=0.40, rely=0.6, anchor=ctk.CENTER)
button_root_two = ctk.CTkButton(master=window, text='√', height=60, width=60, command=lambda: add_to_calculation('√('))
button_root_two.place(relx=0.60, rely=0.5, anchor=ctk.CENTER)
button_power = ctk.CTkButton(master=window, text='x\u02b8', height=60, width=60,
                             command=lambda: add_to_calculation('power('))
button_power.place(relx=0.50, rely=0.5, anchor=ctk.CENTER)
button_log10 = ctk.CTkButton(master=window, text='log10', height=60, width=60,
                             command=lambda: add_to_calculation('log10('))
button_log10.place(relx=0.70, rely=0.4, anchor=ctk.CENTER)

# trigonometry buttons
button_sin = ctk.CTkButton(master=window, text='sin', height=60, width=60, command=lambda: add_to_calculation('sin('))
button_sin.place(relx=0.50, rely=0.3, anchor=ctk.CENTER)
button_cos = ctk.CTkButton(master=window, text='cos', height=60, width=60, command=lambda: add_to_calculation('cos('))
button_cos.place(relx=0.60, rely=0.3, anchor=ctk.CENTER)
button_tg = ctk.CTkButton(master=window, text='tan', height=60, width=60, command=lambda: add_to_calculation('tan('))
button_tg.place(relx=0.50, rely=0.4, anchor=ctk.CENTER)
button_ctg = ctk.CTkButton(master=window, text='ctg', height=60, width=60, command=lambda: add_to_calculation('ctg('))
button_ctg.place(relx=0.60, rely=0.4, anchor=ctk.CENTER)


#actions buttons
button_calc = ctk.CTkButton(text='=', command=do_calculation, font=("Arial", 12), height=60, width=150, master=window)
button_calc.place(relx=0.2, rely=0.7, anchor=ctk.CENTER)
button_ce = ctk.CTkButton(text='CE', command=clear_field, font=("Arial", 12), height=60, width=150, master=window)
button_ce.place(relx=0.45, rely=0.7, anchor=ctk.CENTER)
button_c = ctk.CTkButton(text='C', command=delete_char, font=("Arial", 12), height=60, width=150, master=window)
button_c.place(relx=0.70, rely=0.7, anchor=ctk.CENTER)


window.mainloop()
