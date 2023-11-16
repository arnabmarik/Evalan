
from tkinter import *
import numpy as np
import random
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps= 0
# ---------------------------- TIMER RESET ------------------------------- # 



stop_var = False
timer_id = None
def reset_time():
    window.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps=0




# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_time():
    global reps
    global stop_var
    reps_mins = [25,5,25,5,25,5,25,20]
    reps_mins = [i*60 for i in reps_mins]
    count_down(reps_mins[reps])
    reps += 1




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    # print(count)
    count_min = int((count/60))
    count_sec = count % 60
    if count_sec in range(10):
        count_sec = f'0{count_sec}'
    text =f'{count_min}:{count_sec}'
    canvas.itemconfig(timer_text, text=text)
    if count >0:
        global timer_id
        timer_id = window.after(1000, count_down, count - 1)
    else:
        start_time()




# canvas.itemconfig(timer_text, text=0)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()



window.title("Pomodoro")
window.config(padx=90,pady=50,bg=YELLOW, highlightthickness=0)


title_label = Label(text="Timer", fg=GREEN, bg = YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0 , column=1)

canvas = Canvas(width=225, height=224,bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="White", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_time)
start_button.grid(column=0,row=2)
reset_button = Button(text="Reset", command = reset_time)
reset_button.grid(column=2,row=2)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)





window.mainloop()