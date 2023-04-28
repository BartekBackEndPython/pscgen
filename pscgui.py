# if it works don't touch it

# import required libraries
import tkinter as tk
import generator


# set app's colours
bg_color = '#1e3837'
font_color = 'white'
buttons_color = '#949494'

# create and configure tkinter window
psc_window = tk.Tk()
psc_window.geometry('400x400')
psc_window.title("PaySafeCard Generator")
psc_window.resizable(False, False)
psc_window.config(bg=bg_color)

# define checkboxes' state variables
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
v4 = tk.IntVar()
v5 = tk.IntVar()


# create tkinter widgets
select_number = tk.Label(psc_window, bg=bg_color, fg=font_color, text="Wybierz ilość kodów",
                         font=('Times New Roman', 18))
select_number.place(relx=0.5, anchor=tk.N)

button_add = tk.Button(psc_window, bg=buttons_color, text="+", font='2', padx=1, pady=1)
button_add.place(relx=0.2, rely=0.085)

select_1 = tk.Checkbutton(psc_window, bg=bg_color, activebackground=bg_color, variable=v1)
select_1.place(relx=0.3, rely=0.1)
select_2 = tk.Checkbutton(psc_window, bg=bg_color, activebackground=bg_color, variable=v2)
select_2.place(relx=0.4, rely=0.1)
select_3 = tk.Checkbutton(psc_window, bg=bg_color, activebackground=bg_color, variable=v3)
select_3.place(relx=0.5, rely=0.1)
select_4 = tk.Checkbutton(psc_window, bg=bg_color, activebackground=bg_color, variable=v4)
select_4.place(relx=0.6, rely=0.1)
select_5 = tk.Checkbutton(psc_window, bg=bg_color, activebackground=bg_color, variable=v5)
select_5.place(relx=0.7, rely=0.1)

button_generate = tk.Button(psc_window, bg=buttons_color, fg='black', text="Generate", padx=30, pady=10,
                            font=('Times New Roman', 10))
button_generate.place(relx=0.350, rely=0.2)

button_copy = tk.Button(psc_window, bg=buttons_color, fg='black', text="Copy", padx=10, pady=8,
                        font=('Times New Roman', 10), command=lambda: generator.copy_code(result_label))
button_copy.place(relx=0.8, rely=0.350)

result_label = tk.Label(psc_window, bg=font_color, fg='black', width=25, font=('Times New Roman', 10))
result_label.place(relx=0.5, rely=0.4, anchor=tk.N)

# create lists that will be given to generator's functions
checkboxes_list = [select_1, select_2, select_3, select_4, select_5]
var_list = [v1, v2, v3, v4, v5]
button_generate.config(command=lambda: generator.generate_and_put(var_list, result_label))
button_add.config(command=lambda: generator.add_check_button(var_list))

# call psc_window mainloop
psc_window.mainloop()
