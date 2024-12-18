# Zebiri Saad
# HE202391
# 2TM2

import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jeu de devinettes")
        self.geometry("400x300")  # Taille de la fenêtre
        self.configure(bg="#dde")  # Couleur de fond de la fenêtre

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        label_style = {'bg': '#dde', 'font': ('Helvetica', 14)}
        entry_style = {'font': ('Helvetica', 12)}
        button_style = {'font': ('Helvetica', 12, 'bold'), 'bg': '#abd', 'fg': 'white'}
        result_style = {'bg': '#dde', 'font': ('Helvetica', 12, 'italic')}

        self.label = tk.Label(self, text="Devinez un nombre entre 1 et 100:", **label_style)
        self.label.pack(pady=20)

        self.entry = tk.Entry(self, **entry_style)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_guess)  # Lier la touche Enter à la fonction check_guess

        self.guess_button = tk.Button(self, text="Devinez", command=self.check_guess, **button_style)
        self.guess_button.pack(pady=20)

        self.result_label = tk.Label(self, text="", **result_style)
        self.result_label.pack(pady=10)

    def check_guess(self, event=None):  # Ajouter un paramètre optionnel pour gérer l'événement
        guess = int(self.entry.get())
        self.attempts += 1

        if guess == self.secret_number:
            messagebox.showinfo("Félicitations!", f"Bravo! Vous avez trouvé le numéro en {self.attempts} essais.")
            self.reset_game()
        elif guess < self.secret_number:
            self.result_label.config(text="Plus haut!", fg='blue')
        else:
            self.result_label.config(text="Plus bas!", fg='red')

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()
