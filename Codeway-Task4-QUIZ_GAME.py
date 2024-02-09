from tkinter import *

question = {
    "What does CPU stand for?": ['Central Processing Unit', 'Central Process Unit', 'Computer Personal Unit', 'Central Processor Unit'],
    "Which programming language is known as the 'mother of all languages'?": ['C++', 'Python', 'C', 'Java'],
    "What does GUI stand for?": ['Graphical User Interface', 'General User Interface', 'Graphical Unified Interface', 'General Unified Interface'],
    "Which company developed the Python programming language?": ['Microsoft', 'Apple', 'Google', 'Facebook'],
    "In computer science, what does the acronym API stand for?": ['Application Programming Interface', 'Advanced Programming Interface', 'Automated Programming Interface', 'Application Process Interface'],
    "What is the purpose of the 'elif' keyword in Python?": ['To define a new function', 'To handle exceptions', 'To create a loop', 'To check multiple conditions'],
    "What is the default port number for the HTTP protocol?": ['80', '8080', '8000', '8888'],
    "Which data structure uses the Last In, First Out (LIFO) principle?": ['Queue', 'Stack', 'Linked List', 'Array'],
    "What is the role of a compiler in the process of program execution?": ['Converts source code to machine code', 'Executes the program', 'Optimizes the program', 'Debugs the program'],
    "In object-oriented programming, what is encapsulation?": ['Encapsulation', 'Polymorphism', 'Abstraction', 'Inheritance'],

    "What does HTML stand for?": ['Hyper Text Markup Language', 'Highly Typed Modeling Language', 'Hyperlink and Text Markup Language', 'Home Tool Markup Language'],
    "Which programming language is often used for web development?": ['Java', 'C++', 'Python', 'JavaScript'],
    "What is the purpose of CSS in web development?": ['Creating beautiful web pages', 'Handling server-side logic', 'Defining the structure of a webpage', 'Managing databases'],
    "What is the function of a firewall in network security?": ['Monitor and control incoming and outgoing network traffic', 'Detect and remove computer viruses', 'Encrypt data transmissions', 'Manage hardware components'],
    "What is the main role of a database management system (DBMS)?": ['Manage and organize data', 'Design user interfaces', 'Create graphics and animations', 'Compile source code'],
    "Which company developed the Java programming language?": ['Microsoft', 'Apple', 'Google', 'Sun Microsystems'],
    "What does SQL stand for in the context of databases?": ['Structured Query Language', 'Sequential Question Language', 'Simple Question Language', 'Standardized Query Language'],
    "What is the purpose of the Python library 'NumPy'?": ['Numerical computing', 'Web development', 'Artificial intelligence', 'Data visualization'],
    "What is a VPN used for?": ['Securely connecting to a private network over the internet', 'Accessing websites with geographical restrictions', 'Encrypting files on a local computer', 'Managing virtual machines'],
    "What does the acronym API stand for in software development?": ['Application Programming Interface', 'Automated Process Integration', 'Advanced Programming Interface', 'Artificial Processing Interface'],
    "What is the capital of France?": ['Berlin', 'Madrid', 'Paris', 'Rome'],
    "Which planet is known as the Red Planet?": ['Venus', 'Mars', 'Jupiter', 'Saturn'],
    "What is the largest mammal on Earth?": ['Elephant', 'Blue Whale', 'Giraffe', 'Lion'],
    "Who wrote the play 'Romeo and Juliet'?": ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Mark Twain'],
    "What is the chemical symbol for gold?": ['Au', 'Ag', 'Fe', 'Cu'],
    "Which continent is the largest by land area?": ['Asia', 'North America', 'Africa', 'Europe'],
    "What is the square root of 64?": ['6', '8', '10', '12'],
    "Who discovered penicillin?": ['Marie Curie', 'Alexander Fleming', 'Louis Pasteur', 'Gregor Mendel'],
    "What is the currency of Japan?": ['Yuan', 'Won', 'Yen', 'Ringgit'],
    "Who is known as the 'Father of Computer Science'?": ['Alan Turing', 'Bill Gates', 'Steve Jobs', 'Mark Zuckerberg']
}

# Difficulty levels
easy_questions = list(question.items())[:10] 
medium_questions = list(question.items())[10:20] 
hard_questions = list(question.items())[20:]

answers = [
    'Central Processing Unit', 'Python', 'Graphical User Interface', 'Microsoft', 
    'Application Programming Interface', 'To check multiple conditions', '80', 'Stack', 
    'Converts source code to machine code', 'Encapsulation',
    'Hyper Text Markup Language', 'JavaScript', 'Creating beautiful web pages', 'Monitor and control incoming and outgoing network traffic', 
    'Manage and organize data', 'Sun Microsystems', 'Structured Query Language', 'Numerical computing', 
    'Securely connecting to a private network over the internet', 'Application Programming Interface',
    'Paris', 'Mars', 'Blue Whale', 'William Shakespeare', 'Au', 'Asia', '8', 'Alexander Fleming', 'Alan Turing'
]

# Grouping answers based on difficulty level
easy_ans = list(answers[:10] )
medium_ans = list(answers[10:20])
hard_ans = list(answers[20:]) 

current_question = 0

def start_quiz(difficulty):
    global current_question
    current_question = 0

    if difficulty == 'easy':
        questions = easy_questions
        answers = easy_ans
    elif difficulty == 'medium':
        questions = medium_questions
        answers = medium_ans
    elif difficulty == 'hard':
        questions = hard_questions
        answers = hard_ans
    else:
        raise ValueError("Invalid difficulty level")

    hide_difficulty_buttons()
    start_button.forget()
    quit_button.pack(side=TOP, anchor=NE, padx=0, pady=10)
    next_button.config(command=lambda: next_question(questions, answers, difficulty))
    next_button.pack()
    next_question(questions, answers, difficulty)

def next_question(questions, answers, difficulty):
    global current_question
    if current_question < len(questions):
        check_ans(answers)
        user_ans.set('None')
        c_question, options = questions[current_question]
        clear_frame()
        Label(f1, text=f"Difficulty level: {difficulty.capitalize()}",justify="center", font="calibre 13 normal").pack(anchor=NW)
        Label(f1, text=f"Question {current_question + 1} : {c_question}", padx=15,
            font="calibre 13 normal").pack(anchor=NW)
        for option in options:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option, padx=28).pack(anchor=NW)
        question_label = Label(f1, text=f"Question {current_question + 1} : {c_question}", padx=15,
                       font="calibre 13 normal", justify="center")
        

        current_question += 1
    else:
        hide_difficulty_buttons()
        quit_button.forget()
        next_button.forget()
        check_ans(answers)
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(questions)}"
        Label(f1, text=output, font="calibre 25 bold").pack()
        Label(f1, text="Thanks for Participating",
            font="calibre 19 bold").pack()
        show_difficulty_buttons()
        quit_button.pack(side=TOP, anchor=NE, padx=0, pady=10)


def check_ans(answers):
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == answers[current_question-1]:
        user_score.set(user_score.get()+1)

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

def show_difficulty_buttons():
    start_button.pack()
    medium_button.pack()
    hard_button.pack()

def hide_difficulty_buttons():
    start_button.forget()
    medium_button.forget()
    hard_button.forget()

if __name__ == "__main__":
    root = Tk()
    root.title("QUIZ APP")
    root.geometry("820x480")
    root.minsize(800, 400)

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    Label(root, text="Quiz App",
        font="arial 50 bold",
        relief=SUNKEN, background="red",
        padx=10, pady=9).pack()
    Label(root, text="", font="calibre 14 bold").pack()

    start_button = Button(root,
                        text="Easy Quiz",
                        command=lambda: start_quiz('easy'),
                        font="calibre 15 bold")

    medium_button = Button(root,
                        text="Medium Quiz",
                        command=lambda: start_quiz('medium'),
                        font="calibre 15 bold")

    hard_button = Button(root,
                        text="Hard Quiz",
                        command=lambda: start_quiz('hard'),
                        font="calibre 15 bold")
    quit_button = Button(root, text="Quit",
                        command=root.destroy,
                        font="calibre 15 bold")

    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)

    next_button = Button(root, text="Next Question",
                    command=lambda: next_question(question, answers, 'easy'),
                    font="calibre 15 bold")

    quit_button = Button(root, text="Quit",
                        command=root.destroy,
                        font="calibre 15 bold")

    show_difficulty_buttons()

    root.mainloop()