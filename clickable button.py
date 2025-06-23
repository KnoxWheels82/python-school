import tkinter as tk
import time

class ReactionTimeApp:
    def __init__(self, master):
        self.master = master
        master.title("Reaction Time Test")

        self.start_time = None
        self.reaction_time_label = tk.Label(master, text="Click the button when it appears!", font=("Arial", 16))
        self.reaction_time_label.pack(pady=20)

        self.button = tk.Button(master, text="Click Me!", command=self.on_button_click, font=("Arial", 20), state=tk.DISABLED)
        self.button.pack(pady=50)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_test, font=("Arial", 12))
        self.reset_button.pack(pady=10)

        self.prepare_test()

    def prepare_test(self):
        self.reaction_time_label.config(text="Get ready...")
        self.button.config(state=tk.DISABLED)
        # Schedule the button to appear after a random delay
        self.master.after(2000, self.start_timer) # 2-second delay

    def start_timer(self):
        self.reaction_time_label.config(text="Click Now!")
        self.button.config(state=tk.NORMAL)
        self.start_time = time.time()

    def on_button_click(self):
        if self.start_time is not None:
            end_time = time.time()
            reaction_time = end_time - self.start_time
            self.reaction_time_label.config(text=f"Your reaction time: {reaction_time:.3f} seconds")
            self.button.config(state=tk.DISABLED)
            self.start_time = None

    def reset_test(self):
        self.prepare_test()

if __name__ == "__main__":
    root = tk.Tk()
    app = ReactionTimeApp(root)
    root.mainloop()
