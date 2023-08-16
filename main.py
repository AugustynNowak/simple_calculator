# Simple Calculator in Python using tkinter
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    textbox.delete("0.0", "end")
    textbox.insert("0.0", calculation)


def do_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        textbox.delete(1.0, "end")
        textbox.insert(1.0, result)

    except:
        clear_field()
        textbox.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    textbox.delete(1.0, "end")


window = ctk.CTk()
window.geometry("600x700")
window.title('Simple Calculator')

frame = ctk.CTkFrame(master=window,
                     corner_radius=25)
frame.pack(pady=20,
           padx=20,
           fill="both",
           expand=True)

textbox = ctk.CTkTextbox(master=window,
                         height=120,
                         width=500,
                         font=('Arial', 20))
textbox.place(rely=0.05,
              relx=0.5,
              anchor=tk.N)

button_1 = ctk.CTkButton(master=window, text='1', height=60, width=60,
                         command=lambda: add_to_calculation(1))
button_1.place(relx=0.2, rely=0.3, anchor=tk.CENTER)
button_2 = ctk.CTkButton(master=window, text='2', height=60, width=60,
                         command=lambda: add_to_calculation(2))
button_2.place(relx=0.4, rely=0.3, anchor=tk.CENTER)
button_3 = ctk.CTkButton(master=window, text='3', height=60, width=60,
                         command=lambda: add_to_calculation(3))
button_3.place(relx=0.6, rely=0.3, anchor=tk.CENTER)
button_4 = ctk.CTkButton(master=window, text='4', height=60, width=60,
                         command=lambda: add_to_calculation(4))
button_4.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
button_5 = ctk.CTkButton(master=window, text='5', height=60, width=60,
                         command=lambda: add_to_calculation(5))
button_5.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
button_6 = ctk.CTkButton(master=window, text='6', height=60, width=60,
                         command=lambda: add_to_calculation(6))
button_6.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
button_7 = ctk.CTkButton(master=window, text='7', height=60, width=60,
                         command=lambda: add_to_calculation(7))
button_7.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
button_8 = ctk.CTkButton(master=window, text='8', height=60, width=60,
                         command=lambda: add_to_calculation(8))
button_8.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
button_9 = ctk.CTkButton(master=window, text='9', height=60, width=60,
                         command=lambda: add_to_calculation(9))
button_9.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
button_0 = ctk.CTkButton(master=window, text='0', height=60, width=60,
                         command=lambda: add_to_calculation(0))
button_0.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
button_plus = ctk.CTkButton(master=window, text='+', height=60, width=60,
                            command=lambda: add_to_calculation('+'))
button_plus.place(relx=0.8, rely=0.3, anchor=tk.CENTER)
button_minus = ctk.CTkButton(master=window, text='-', height=60, width=60,
                             command=lambda: add_to_calculation('-'))
button_minus.place(relx=0.8, rely=0.4, anchor=tk.CENTER)
button_mul = ctk.CTkButton(master=window, text='*', height=60, width=60,
                           command=lambda: add_to_calculation('*'))
button_mul.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
button_div = ctk.CTkButton(master=window, text='/', height=60, width=60,
                           command=lambda: add_to_calculation('/'))
button_div.place(relx=0.8, rely=0.6, anchor=tk.CENTER)
button_open = ctk.CTkButton(master=window, text='(', height=60, width=60,
                            command=lambda: add_to_calculation('('))
button_open.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

button_close = ctk.CTkButton(master=window, text=')', height=60, width=60,
                             command=lambda: add_to_calculation(')'))
button_close.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

button_c = ctk.CTkButton(text='C',
                         command=clear_field,
                         font=("Arial", 12),
                         height=60,
                         width=150,
                         master=window)
button_c.place(relx=0.55,
               rely=0.7,
               anchor=tk.W)

button_calc = ctk.CTkButton(text='=',
                            command=do_calculation,
                            font=("Arial", 12),
                            height=60,
                            width=150,
                            master=window)
button_calc.place(relx=0.45,
                  rely=0.7,
                  anchor=tk.E)

window.mainloop()
