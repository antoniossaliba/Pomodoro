from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    canvas.itemconfig(text, text="00:00")
    check_mark["text"] = ""
    label["text"] = "Timer"
    label["fg"] = GREEN
    globals()["reps"] = 1
    window.after_cancel(globals()["timer"])

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start():
    def count_down(count):
        count_min = count // 60
        count_secs = count % 60
        if count_min < 10:
            if count_secs < 10:
                canvas.itemconfig(text, text=f"0{count_min}:0{count_secs}")
            else:
                canvas.itemconfig(text, text=f"0{count_min}:{count_secs}")
        else:
            if count_secs < 10:
                canvas.itemconfig(text, text=f"{count_min}:0{count_secs}")
            else:
                canvas.itemconfig(text, text=f"{count_min}:{count_secs}")
        if count > 0:
            globals()["timer"] = window.after(1000, count_down, count - 1)
        else:
            if globals()["reps"] % 2 != 0 and globals()["reps"] < 8:
                check_mark["text"] += "✓"
            globals()["reps"] += 1
            start()

    current_timer = globals()["reps"]
    if current_timer % 2 != 0 and current_timer < 8:
        label["text"] = "Work"
        label["fg"] = globals()["GREEN"]
        count_down(globals()["WORK_MIN"] * 60)
    else:
        if current_timer < 8:
            label["text"] = "Short Break"
            label["fg"] = globals()["RED"]
            count_down(globals()["SHORT_BREAK_MIN"] * 60)
        else:
            if current_timer == 8:
                label["text"] = "Long Break"
                label["fg"] = globals()["PINK"]
                count_down(globals()["LONG_BREAK_MIN"] * 60)
            else:
                return

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, width=500, height=500)
window.maxsize(width=500, height=500)
window.minsize(width=500, height=500)

label = Label(text="Timer", fg=GREEN, font=("Courier", 35, "bold"), bg=YELLOW)
label.place(x=80, y=0)

canvas = Canvas(width=200, height=223, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
text = canvas.create_text(102, 138, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.place(x=50, y=50)

start_button = Button(text="Start", borderwidth=3, border=3, font=("Courier", 9, "bold"), command=start_timer)
start_button.place(x=30, y=300)

reset_button = Button(text="Reset", border=3, borderwidth=3, font=("Courier", 9, "bold"), command=reset)
reset_button.place(x=230, y=300)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=("Courier", 12, "bold"))
check_mark.place(x=140, y=330)

window.mainloop()