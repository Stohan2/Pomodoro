from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global ticks, reps
    window.after_cancel(timer)
    prog_name.config(text="Timer", fg=GREEN)
    ticks = ""
    reps = 0
    canvas.itemconfig(timer_text, text="25:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        prog_name.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        prog_name.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        prog_name.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global ticks
    work_time = count
    mins, secs = divmod(work_time, 60)
    time_format = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text, text=time_format)
    if work_time > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            ticks += "✔"
            label_T.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

prog_name = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
prog_name.grid(column=1,row=0)

canvas = Canvas(width=208, height =228, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(104, 114, image=tomato_png)
timer_text = canvas.create_text(104, 140, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

but_start = Button(text="Start", font=(FONT_NAME, 16, "normal"), bg=YELLOW, highlightthickness=0, command=start_timer)
but_start.grid(column=0, row=3)

but_reset = Button(text="Reset", font=(FONT_NAME, 16, "normal"), bg=YELLOW, highlightthickness=0, command=reset_timer)
but_reset.grid(column=2, row=3)

label_T = Label(text="", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label_T.grid(column=1, row=4)



window.mainloop()