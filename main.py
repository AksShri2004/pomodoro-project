from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    global check
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
    check = ""
    label_check.config(text=check)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def on_click():
    global reps
    global check
    work_seconds = (WORK_MIN * 60)
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 9 == 0 and reps != 0:
        check_count()
        label_timer.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 != 0:
        check_count()
        label_timer.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="WORK", fg=GREEN)
        count_down(work_seconds)
    reps += 1


# ------------------------------CHECKS COUNTER------------------------------------#
def check_count():
    global check
    check += "✔"
    label_check.config(text=check)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60

    global timer

    if minutes < 10 and seconds < 10:
        canvas.itemconfig(timer_text, text="0" + str(minutes) + ":" + "0" + str(seconds))
    elif minutes < 10 and seconds > 9:
        canvas.itemconfig(timer_text, text="0" + str(minutes) + ":" + str(seconds))
    else:
        canvas.itemconfig(timer_text, text=str(minutes) + ":" + str(seconds))

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        on_click()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_ing = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_ing)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

check = ""

label_timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=1, column=2)

button_reset = Button(text="Reset", command=reset)
button_reset.grid(row=3, column=3)

button_start = Button(text="Start", command=on_click)
button_start.grid(row=3, column=1)

label_check = Label(text=check, fg=GREEN, bg=YELLOW)
label_check.grid(row=4, column=2)

window.mainloop()
