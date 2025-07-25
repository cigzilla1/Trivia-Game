import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    ("What does CPU stand for?", "central processing unit"),
    ("What does RAM stand for?", "random access memory"),
    ("Who is the GOAT? a. lionel messi b. pele c. maradona d. cristiano ronaldo", "d"),
    ("What process is responsible for converting sunlight into energy in plants?", "photosynthesis"),
    ("In what fictional town does SpongeBob SquarePants live?", "bikini bottom"),
    ("Who painted the Mona Lisa?", "leonardo da vinci"),
    ("What is the capital city of Japan?", "tokyo"),
    ("What is the largest ocean on Earth?", "pacific ocean"),
    ("What is the name of the galaxy that contains our Solar System?", "milky way"),
    ("Which country has won the most FIFA World Cup titles?", "brazil")
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.q_index = 0

        self.label = tk.Label(root, text="Welcome to Quiz Game", font=("Arial", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        self.start_button.pack_forget()
        self.label.config(text="")
        self.ask_question()

    def ask_question(self):
        if self.q_index < len(questions):
            self.label.config(text=f"Q{self.q_index + 1}: {questions[self.q_index][0]}")
            self.answer_entry = tk.Entry(self.root, width=50)
            self.answer_entry.pack(pady=10)
            self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
            self.submit_button.pack()
        else:
            self.show_result()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = questions[self.q_index][1]
        if user_answer == correct_answer:
            self.score += 1
        self.answer_entry.destroy()
        self.submit_button.destroy()
        self.q_index += 1
        self.ask_question()

    def show_result(self):
        percentage = (self.score / len(questions)) * 100
        messagebox.showinfo("Quiz Completed", f"You got {self.score} out of {len(questions)} questions correct!\nScore: {percentage:.2f}%")
        self.root.quit()

# Run the game
root = tk.Tk()
quiz = QuizGame(root)
root.mainloop()
