import tkinter as tk
import json

root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

with open("questions.json") as file:
    questions = json.load(file)

current_question = 0
score = 0

var = tk.StringVar()


question_label = tk.Label(root, text="", wraplength=350)
question_label.pack(pady=10)

options = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=var, value="")
    btn.pack(anchor="w")
    options.append(btn)

def display_question():
    var.set("")
    question_label.config(text=questions[current_question]["question"])

    shuffled_options = questions[current_question]["options"][:]

    for i, option in enumerate(shuffled_options):
        options[i].config(text=option, value=option)

def next_question():
    global current_question, score

    if var.get() == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        question_label.config(
            text="Quiz Finished!\nYour Score: " + str(score) + "/" + str(len(questions))
        )
        for btn in options:
            btn.config(state="disabled")
        next_button.config(state="disabled")
next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack(pady=10)
display_question()
root.mainloop()