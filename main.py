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
    textbox.delete("0.0", "end")
    textbox.insert("0.0", form)


def do_calculation():
    global form
    sentence_to_save = form

    transformed_form_1 = form.replace('√', 'math.sqrt')
    transformed_form_2 = transformed_form_1.replace('π', 'math.pi')
    transformed_form_3 = transformed_form_2.replace('sin', 'math.sin')
    transformed_form_4 = transformed_form_3.replace('cos', 'math.cos')
    transformed_form_5 = transformed_form_4.replace('tan', 'math.tan')
    transformed_form_6 = transformed_form_5.replace('ctg', '1/math.tan')
    transformed_form_7 = transformed_form_6.replace('power', '**')
    transformed_form_8 = transformed_form_7.replace('e', 'math.e')
    transformed_form_9 = transformed_form_8.replace('deg', 'math.degrees')
    transformed_form_10 = transformed_form_9.replace('rad', 'math.radians')
    transformed_form_11 = transformed_form_10.replace('log10', 'math.log10')

    try:
        result = str(eval(transformed_form_11))
        form = ""
        textbox.delete(1.0, "end")
        textbox.insert(1.0, result)

    except:
        clear_field()
        textbox.insert(1.0, "Error")

    sentence_to_save += ('=' + result)
    saving_results(sentence_to_save)


def delete_char():
    global form
    form = form[0:len(form) - 1]
    textbox.delete(1.0, "end")
    textbox.insert(1.0, form)


def clear_field():
    global form
    form = ""
    textbox.delete(1.0, "end")


def saving_results(word_to_save):
    local_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = word_to_save + '\t' + local_dt + '\n'

    with open('results.txt', 'a+') as f:
        f.write(result)


window = ctk.CTk()
window.geometry("600x700")
window.title('Simple Calculator')

frame = ctk.CTkFrame(master=window, corner_radius=25)
frame.pack(pady=20, padx=20, fill="both", expand=True)

textbox = ctk.CTkTextbox(master=frame, height=120, width=500, font=('Arial', 20))
textbox.place(rely=0.05, relx=0.5, anchor=tk.S)
textbox.pack(fill="both")

button_1 = ctk.CTkButton(master=window, text='1', height=60, width=60, command=lambda: add_to_calculation(1))
button_1.place(relx=0.15, rely=0.3, anchor=tk.CENTER)
button_2 = ctk.CTkButton(master=window, text='2', height=60, width=60, command=lambda: add_to_calculation(2))
button_2.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
button_3 = ctk.CTkButton(master=window, text='3', height=60, width=60, command=lambda: add_to_calculation(3))
button_3.place(relx=0.35, rely=0.3, anchor=tk.CENTER)
button_4 = ctk.CTkButton(master=window, text='4', height=60, width=60, command=lambda: add_to_calculation(4))
button_4.place(relx=0.15, rely=0.4, anchor=tk.CENTER)
button_5 = ctk.CTkButton(master=window, text='5', height=60, width=60, command=lambda: add_to_calculation(5))
button_5.place(relx=0.25, rely=0.4, anchor=tk.CENTER)
button_6 = ctk.CTkButton(master=window, text='6', height=60, width=60, command=lambda: add_to_calculation(6))
button_6.place(relx=0.35, rely=0.4, anchor=tk.CENTER)
button_7 = ctk.CTkButton(master=window, text='7', height=60, width=60, command=lambda: add_to_calculation(7))
button_7.place(relx=0.15, rely=0.5, anchor=tk.CENTER)
button_8 = ctk.CTkButton(master=window, text='8', height=60, width=60, command=lambda: add_to_calculation(8))
button_8.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
button_9 = ctk.CTkButton(master=window, text='9', height=60, width=60, command=lambda: add_to_calculation(9))
button_9.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
button_0 = ctk.CTkButton(master=window, text='0', height=60, width=60, command=lambda: add_to_calculation(0))
button_0.place(relx=0.15, rely=0.6, anchor=tk.CENTER)
button_dot = ctk.CTkButton(master=window, text='.', height=60, width=60, command=lambda: add_to_calculation('.'))
button_dot.place(relx=0.25, rely=0.6, anchor=tk.CENTER)
button_plus = ctk.CTkButton(master=window, text='+', height=60, width=60, command=lambda: add_to_calculation('+'))
button_plus.place(relx=0.45, rely=0.3, anchor=tk.CENTER)
button_minus = ctk.CTkButton(master=window, text='-', height=60, width=60, command=lambda: add_to_calculation('-'))
button_minus.place(relx=0.45, rely=0.4, anchor=tk.CENTER)
button_mul = ctk.CTkButton(master=window, text='*', height=60, width=60, command=lambda: add_to_calculation('*'))
button_mul.place(relx=0.45, rely=0.5, anchor=tk.CENTER)
button_div = ctk.CTkButton(master=window, text='/', height=60, width=60, command=lambda: add_to_calculation('/'))
button_div.place(relx=0.45, rely=0.6, anchor=tk.CENTER)
button_root_two = ctk.CTkButton(master=window, text='√', height=60, width=60, command=lambda: add_to_calculation('√('))
button_root_two.place(relx=0.65, rely=0.5, anchor=tk.CENTER)
button_power = ctk.CTkButton(master=window, text='x\u02b8', height=60, width=60,
                             command=lambda: add_to_calculation('power('))
button_power.place(relx=0.55, rely=0.5, anchor=tk.CENTER)
button_log10 = ctk.CTkButton(master=window, text='log10', height=60, width=60,
                             command=lambda: add_to_calculation('log10('))
button_log10.place(relx=0.75, rely=0.6, anchor=tk.CENTER)

button_pi = ctk.CTkButton(master=window, text='π', height=60, width=60, command=lambda: add_to_calculation('π'))
button_pi.place(relx=0.35, rely=0.6, anchor=tk.CENTER)
button_e = ctk.CTkButton(master=window, text='e', height=60, width=60, command=lambda: add_to_calculation('e'))
button_e.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
button_open = ctk.CTkButton(master=window, text='(', height=60, width=60, command=lambda: add_to_calculation('('))
button_open.place(relx=0.55, rely=0.6, anchor=tk.CENTER)
button_close = ctk.CTkButton(master=window, text=')', height=60, width=60, command=lambda: add_to_calculation(')'))
button_close.place(relx=0.65, rely=0.6, anchor=tk.CENTER)

button_sin = ctk.CTkButton(master=window, text='sin', height=60, width=60, command=lambda: add_to_calculation('sin('))
button_sin.place(relx=0.55, rely=0.3, anchor=tk.CENTER)
button_cos = ctk.CTkButton(master=window, text='cos', height=60, width=60, command=lambda: add_to_calculation('cos('))
button_cos.place(relx=0.65, rely=0.3, anchor=tk.CENTER)
button_tg = ctk.CTkButton(master=window, text='tan', height=60, width=60, command=lambda: add_to_calculation('tan('))
button_tg.place(relx=0.55, rely=0.4, anchor=tk.CENTER)
button_ctg = ctk.CTkButton(master=window, text='ctg', height=60, width=60, command=lambda: add_to_calculation('ctg('))
button_ctg.place(relx=0.65, rely=0.4, anchor=tk.CENTER)
button_deg = ctk.CTkButton(master=window, text='deg', height=60, width=60, command=lambda: add_to_calculation('deg('))
button_deg.place(relx=0.75, rely=0.3, anchor=tk.CENTER)
button_rad = ctk.CTkButton(master=window, text='rad', height=60, width=60, command=lambda: add_to_calculation('rad('))
button_rad.place(relx=0.75, rely=0.4, anchor=tk.CENTER)

#actions buttons
button_calc = ctk.CTkButton(text='=', command=do_calculation, font=("Arial", 12), height=60, width=150, master=window)
button_calc.place(relx=0.25, rely=0.7, anchor=tk.CENTER)
button_ce = ctk.CTkButton(text='CE', command=clear_field, font=("Arial", 12), height=60, width=150, master=window)
button_ce.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
button_c = ctk.CTkButton(text='C', command=delete_char, font=("Arial", 12), height=60, width=150, master=window)
button_c.place(relx=0.75, rely=0.7, anchor=tk.CENTER)




window.mainloop()
