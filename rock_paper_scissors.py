import tkinter as tk
from random import choice

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("800x600")

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer's score: {computer_score}")

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="Result: ")
    user_score_label.config(text="Your score: 0")
    computer_score_label.config(text="Computer's score: 0")
def feedback(feedback_text):
    feedback_label.config(text=f"Feedback: {feedback_text}")

frame = tk.Frame(root)
frame.pack(pady=20)

instruction_label = tk.Label(frame, text="Choose Rock , Paper or Scissors \n Instructions \n Rock beats Scissors,Scissors beats Paper,Paper beats Rock ", font=('arial', 14))
instruction_label.grid(row=0, column=0, columnspan=3)

user_choice_label = tk.Label(frame, text="Your choice: ", font=('arial', 12))
user_choice_label.grid(row=1, column=0, columnspan=3)

computer_choice_label = tk.Label(frame, text="Computer's choice: ", font=('arial', 12))
computer_choice_label.grid(row=2, column=0, columnspan=3)

result_label = tk.Label(frame, text="Result: ", font=('arial', 12))
result_label.grid(row=3, column=0, columnspan=3)

user_score_label = tk.Label(frame, text="Your score: 0", font=('arial', 12))
user_score_label.grid(row=4, column=0, padx=10, pady=10)

computer_score_label = tk.Label(frame, text="Computer's score: 0", font=('arial', 12))
computer_score_label.grid(row=4, column=2, padx=10, pady=10)

rock_button = tk.Button(frame, text="Rock", font=('arial', 12), command=lambda: play("Rock"))
rock_button.grid(row=5, column=0, padx=10, pady=10)

paper_button = tk.Button(frame, text="Paper", font=('arial', 12), command=lambda: play("Paper"))
paper_button.grid(row=5, column=1, padx=10, pady=10)

scissors_button = tk.Button(frame, text="Scissors", font=('arial', 12), command=lambda: play("Scissors"))
scissors_button.grid(row=5, column=2, padx=10, pady=10)

reset_button = tk.Button(frame, text="Play Again", font=('arial', 12), command=reset)
reset_button.grid(row=6, column=0, columnspan=3, pady=20)

tk.Label(root, text="Was this game good, okay, or bad?", font=('arial', 14)).pack(pady=10)
tk.Button(root, text="Good", font=('arial', 18, 'bold'), command=lambda: feedback('Good')).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Okay", font=('arial', 18, 'bold'), command=lambda: feedback('Okay')).pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Bad", font=('arial', 18, 'bold'), command=lambda: feedback('Bad')).pack(side=tk.LEFT, padx=10)

feedback_label = tk.Label(root, text="Feedback: ", font=('arial', 14))
feedback_label.pack(pady=20)

root.mainloop()
