import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        
        # Set up the level input
        self.label_level = tk.Label(root, text="Enter level (positive number):")
        self.label_level.pack()
        
        self.entry_level = tk.Entry(root)
        self.entry_level.pack()
        
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()
        
        # Set up the guess input (initially hidden)
        self.label_guess = tk.Label(root, text="Enter your guess:")
        self.label_guess.pack_forget()
        
        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack_forget()
        
        self.guess_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack_forget()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.target_number = None

    def start_game(self):
        try:
            n = int(self.entry_level.get())
            if n > 0:
                self.target_number = random.randint(1, n)
                self.label_guess.pack()
                self.entry_guess.pack()
                self.guess_button.pack()
                self.result_label.config(text="Game started! Make your guess.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for the level.")
    
    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            if guess > self.target_number:
                self.result_label.config(text="Too large!")
            elif guess < self.target_number:
                self.result_label.config(text="Too small!")
            else:
                self.result_label.config(text="Just right!")
                messagebox.showinfo("Congratulations!", "You guessed it right!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for your guess.")
    
    def reset_game(self):
        # Reset the UI to start a new game
        self.entry_level.delete(0, tk.END)
        self.entry_guess.delete(0, tk.END)
        self.label_guess.pack_forget()
        self.entry_guess.pack_forget()
        self.guess_button.pack_forget()
        self.result_label.config(text="")
        self.target_number = None

# Create and run the Tkinter window
root = tk.Tk()
app = GuessingGameApp(root)
root.mainloop()