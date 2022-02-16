import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class PomodoroTimer:
    
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Elijah's Pomodoro Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="pomodoro.png"))
        
        self.s = ttk.Style()
        self.s.configure("TNoteBook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        self.root.mainloop()
    
    def start_timer_thread(self):
        pass
    
    def start_timer(self):
        pass
    
    def reset_clock(self):
        pass
    
    def skip_clock(self):
        pass
 
PomodoroTimer()