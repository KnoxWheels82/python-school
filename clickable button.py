#this was not part of school. I did this on my own.
#I modified the button so that it now moves around the screen and displays your reaction time every time you click it.
import tkinter as tk
import time
import random

class ReactionTimeApp:
    def __init__(self, master):
        self.master = master
        master.title("Reaction Time Test")
        master.geometry("400x300")

        self.start_time = None

        self.reaction_time_label = tk.Label(master, text="Click the button when it appears!", font=("Arial", 16))
        self.reaction_time_label.pack(pady=20)

        self.button = tk.Button(master, text="Click Me!", command=self.on_button_click, font=("Arial", 20), state=tk.DISABLED)
        self.button.pack(pady=20)  # Use pack now since we no longer move it

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_test, font=("Arial", 12))
        self.reset_button.pack(pady=10)

        self.prepare_test()

    def prepare_test(self):
        self.reaction_time_label.config(text="Get ready...")
        self.button.config(state=tk.DISABLED)
        self.start_time = None

        delay = random.randint(1500, 3000)
        self.master.after(delay, self.start_timer)

    def start_timer(self):
        self.reaction_time_label.config(text="Click Now!")
        self.start_time = time.time()
        self.button.config(state=tk.NORMAL)

        # Move the entire window to a random position on the screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = 400
        window_height = 300

        max_x = screen_width - window_width
        max_y = screen_height - window_height

        x = random.randint(0, max_x)
        y = random.randint(0, max_y)

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def on_button_click(self):
        if self.start_time is not None:
            end_time = time.time()
            reaction_time = end_time - self.start_time
            self.reaction_time_label.config(text=f"Your reaction time: {reaction_time:.3f} seconds")
            self.button.config(state=tk.DISABLED)
            self.start_time = None

            self.master.after(2000, self.prepare_test)

    def reset_test(self):
        self.prepare_test()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReactionTimeApp(root)
    root.mainloop()

