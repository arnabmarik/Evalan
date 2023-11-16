from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to Km converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


#Labels
# label = tk.Label(text="Mile to Km converter")
# label.pack()

def calculate_km():
    miles_to_km = (miles_input.get()) * 1.6
    kilometer_result_label = Label(text=f"{miles_to_km}")
    kilometer_result_label.grid(column=1, row=1)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

Km_label = Label(text="Km")
Km_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command= calculate_km)
calculate_button.grid(column=1, row=2)





window.mainloop()
