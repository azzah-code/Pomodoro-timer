import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from plyer import notification

# Set the default time for work and break intervals
WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60

class PomodoroTimer: 
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.geometry("300x250")
        self.root.title("Fokus Azzah!")

        self.status_label = tk.Label(self.root, text="kuy fokus duls!", font=("TkDefaultFont", 16), fg="blue")
        self.status_label.pack(pady=(15,0))

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=(0,0))

        self.start_button = ttk.Button(self.root, text="Mulai best", command=self.start_timer, bootstyle="success")
        self.start_button.pack(pady=(3,0))

        self.stop_button = ttk.Button(self.root, text="Stop best", command=self.stop_timer, state=tk.DISABLED, bootstyle="danger")
        self.stop_button.pack(pady=(3,0))

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME 
                    
                    title = "ISTIRAHATT"
                    if self.pomodoros_completed % 4 == 0:
                        message = "Gacoorr!, \n Kereen dah slese nich!"
                    else:
                        message = "Refresh ur mind duls, trs Lanjyuut!"

                    notification.nontify(
                    title=title,
                    message=message,
                    timeout=10)

            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME

                    notification.nontify(
                        title="FOKUSS",
                        message="Fokus lagii, \n Gass Lanjyuut!",
                        timeout=10)

            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)

PomodoroTimer()
