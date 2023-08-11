import cProfile
from tkinter import *
import customtkinter as ct
import ttkbootstrap as tw
import time
import threading
from PIL import Image, ImageTk

ct.set_appearance_mode("dark")
ct.set_default_color_theme("theme.json")
ct.set_widget_scaling(1.3)
root = ct.CTk(fg_color="#001e4d")
root.title("Quiz App")
root.geometry("850x600+450+100")
root.resizable(False, False)

class Quiz:
    def __init__(self, root, **kwargs):
        self.root = root
        self.score = 0
        self.quiz_fram = ct.CTkFrame(self.root, fg_color="#fff")

        self.title_frame = ct.CTkFrame(self.quiz_fram, fg_color="#fff")

        self.simple_quiz = ct.CTkLabel(self.title_frame, text="Simple Quiz", font=("Poppins", 20, "bold"), text_color="black")
        self.simple_quiz.pack(side=TOP, anchor="nw", pady=0, padx=0)

        self.score_lbl = ct.CTkLabel(self.root, text=f"Score : {self.score}", font=("Poppins", 20, "bold"), text_color="black", fg_color="#fff")
        self.score_lbl.place(x=450, y=50)

        self.line = Label(self.title_frame, text="__________________________________________________", fg="black", font=("consolas", 20, "bold"),
                          bg="#fff")
        self.line.pack(side=TOP, pady=0)

        self.title_frame.pack(side=TOP, pady=10)

        self.option_fram = ct.CTkFrame(self.quiz_fram, fg_color="#fff")

        self.question1 = kwargs["question_1"]
        self.q1option_1 = kwargs["q1option_1"]
        self.q1option_2 = kwargs["q1option_2"]
        self.q1option_3 = kwargs["q1option_3"]
        self.q1option_4 = kwargs["q1correct_option"]

        self.question2 = kwargs["question_2"]
        self.q2option_1 = kwargs["q2option_1"]
        self.q2option_2 = kwargs["q2option_2"]
        self.q2option_3 = kwargs["q2option_3"]
        self.q2option_4 = kwargs["q2correct_option"]

        self.question3 = kwargs["question_3"]
        self.q3option_1 = kwargs["q3option_1"]
        self.q3option_2 = kwargs["q3option_2"]
        self.q3option_3 = kwargs["q3option_3"]
        self.q3option_4 = kwargs["q3correct_option"]

        self.question4 = kwargs["question_4"]
        self.q4option_1 = kwargs["q4option_1"]
        self.q4option_2 = kwargs["q4option_2"]
        self.q4option_3 = kwargs["q4option_3"]
        self.q4option_4 = kwargs["q4correct_option"]

        self.question5 = kwargs["question_5"]
        self.q5option_1 = kwargs["q5option_1"]
        self.q5option_2 = kwargs["q5option_2"]
        self.q5option_3 = kwargs["q5option_3"]
        self.q5option_4 = kwargs["q5correct_option"]

        self.question6 = kwargs["question_6"]
        self.q6option_1 = kwargs["q6option_1"]
        self.q6option_2 = kwargs["q6option_2"]
        self.q6option_3 = kwargs["q6option_3"]
        self.q6option_4 = kwargs["q6correct_option"]

        self.question7 = kwargs["question_7"]
        self.q7option_1 = kwargs["q7option_1"]
        self.q7option_2 = kwargs["q7option_2"]
        self.q7option_3 = kwargs["q7option_3"]
        self.q7option_4 = kwargs["q7correct_option"]

        self.question8 = kwargs["question_8"]
        self.q8option_1 = kwargs["q8option_1"]
        self.q8option_2 = kwargs["q8option_2"]
        self.q8option_3 = kwargs["q8option_3"]
        self.q8option_4 = kwargs["q8correct_option"]

        self.question9 = kwargs["question_9"]
        self.q9option_1 = kwargs["q9option_1"]
        self.q9option_2 = kwargs["q9option_2"]
        self.q9option_3 = kwargs["q9option_3"]
        self.q9option_4 = kwargs["q9correct_option"]

        self.question10 = kwargs["question_10"]
        self.q10option_1 = kwargs["q10option_1"]
        self.q10option_2 = kwargs["q10option_2"]
        self.q10option_3 = kwargs["q10option_3"]
        self.q10option_4 = kwargs["q10correct_option"]

        self.question_1 = ct.CTkLabel(self.option_fram, text=f"{self.question1}", text_color="black", font=("consolas", 20, "normal"))
        self.question_1.pack(side=TOP, anchor="nw", padx=27, pady=20)

        self.option_padding_y = 3
        self.option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q1option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q1option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q1option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q1option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        
        self.option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.option_4.pack(fill=X, padx=25, pady=self.option_padding_y)

        self.next = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_2)

        self.option_1.bind("<Enter>", lambda e: self.option_1.configure(fg_color="black", text_color="white"))
        self.option_1.bind("<Leave>", lambda e: self.option_1.configure(fg_color="white", text_color="black"))
        self.option_2.bind("<Enter>", lambda e: self.option_2.configure(fg_color="black", text_color="white"))
        self.option_2.bind("<Leave>", lambda e: self.option_2.configure(fg_color="white", text_color="black"))
        self.option_3.bind("<Enter>", lambda e: self.option_3.configure(fg_color="black", text_color="white"))
        self.option_3.bind("<Leave>", lambda e: self.option_3.configure(fg_color="white", text_color="black"))
        self.option_4.bind("<Enter>", lambda e: self.option_4.configure(fg_color="black", text_color="white"))
        self.option_4.bind("<Leave>", lambda e: self.option_4.configure(fg_color="white", text_color="black"))

        self.option_1.configure(command=lambda: self.test_answer("option1"))
        self.option_2.configure(command=lambda: self.test_answer("option2"))
        self.option_3.configure(command=lambda: self.test_answer("option3"))
        self.option_4.configure(command=lambda: self.test_answer("option4"))

        self.option_fram.pack(side=TOP, fill=BOTH, expand=True) 
        self.quiz_fram.pack(side=TOP, pady=40, ipadx=40, ipady=100)

    def test_answer(self, selected_answer):
        self.my_correct_option = "option4"
        self.selected_answer = selected_answer

        if self.my_correct_option == self.selected_answer:
            print("Correct !!!")
            self.option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.option_1.unbind()  
            self.option_2.unbind()
            self.option_3.unbind()
            self.option_4.unbind()
            self.next.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.option_1.unbind()
            self.option_2.unbind()
            self.option_3.unbind()
            self.option_4.unbind()
            self.next.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_2(self):
        self.question_1.configure(text=f"{self.question2}")

        self.option_1.pack_forget()
        self.option_2.pack_forget()
        self.option_3.pack_forget()
        self.option_4.pack_forget()

        self.next.pack_forget()

        self.q2option_1_ = ct.CTkButton(self.option_fram, text=f"  {self.q2option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q2option_2_ = ct.CTkButton(self.option_fram, text=f"  {self.q2option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q2option_3_ = ct.CTkButton(self.option_fram, text=f"  {self.q2option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q2option_4_ = ct.CTkButton(self.option_fram, text=f"  {self.q2option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next2 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_3)

        self.q2option_1_.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q2option_4_.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q2option_2_.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q2option_3_.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q2option_1_.bind("<Enter>", lambda e: self.q2option_1_.configure(fg_color="black", text_color="white"))
        self.q2option_1_.bind("<Leave>", lambda e: self.q2option_1_.configure(fg_color="white", text_color="black"))
        self.q2option_2_.bind("<Enter>", lambda e: self.q2option_2_.configure(fg_color="black", text_color="white"))
        self.q2option_2_.bind("<Leave>", lambda e: self.q2option_2_.configure(fg_color="white", text_color="black"))
        self.q2option_3_.bind("<Enter>", lambda e: self.q2option_3_.configure(fg_color="black", text_color="white"))
        self.q2option_3_.bind("<Leave>", lambda e: self.q2option_3_.configure(fg_color="white", text_color="black"))
        self.q2option_4_.bind("<Enter>", lambda e: self.q2option_4_.configure(fg_color="black", text_color="white"))
        self.q2option_4_.bind("<Leave>", lambda e: self.q2option_4_.configure(fg_color="white", text_color="black"))

        self.q2option_1_.configure(command=lambda: self.test_answer_2("option1"))
        self.q2option_2_.configure(command=lambda: self.test_answer_2("option2"))
        self.q2option_3_.configure(command=lambda: self.test_answer_2("option3"))
        self.q2option_4_.configure(command=lambda: self.test_answer_2("option4"))

    def test_answer_2(self, selected_answer2):
        self.my_correct_option = "option4"
        self.selected_answer2 = selected_answer2

        if self.my_correct_option == self.selected_answer2:
            print("Correct !!!")
            self.q2option_1_.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q2option_2_.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q2option_3_.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q2option_4_.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q2option_1_.unbind()  
            self.q2option_2_.unbind()
            self.q2option_3_.unbind()
            self.q2option_4_.unbind()
            self.next2.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q2option_1_.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q2option_2_.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q2option_3_.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q2option_4_.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q2option_1_.unbind()
            self.q2option_2_.unbind()
            self.q2option_3_.unbind()
            self.q2option_4_.unbind()
            self.next2.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_3(self):
        self.question_1.configure(text=f"{self.question3}")

        self.q2option_1_.pack_forget()
        self.q2option_2_.pack_forget()
        self.q2option_3_.pack_forget()
        self.q2option_4_.pack_forget()

        self.next2.pack_forget()

        self.q3option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q3option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q3option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q3option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q3option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q3option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q3option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q3option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next3 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_4)

        self.q3option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q3option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q3option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q3option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q3option_1.bind("<Enter>", lambda e: self.q3option_1.configure(fg_color="black", text_color="white"))
        self.q3option_1.bind("<Leave>", lambda e: self.q3option_1.configure(fg_color="white", text_color="black"))
        self.q3option_2.bind("<Enter>", lambda e: self.q3option_2.configure(fg_color="black", text_color="white"))
        self.q3option_2.bind("<Leave>", lambda e: self.q3option_2.configure(fg_color="white", text_color="black"))
        self.q3option_3.bind("<Enter>", lambda e: self.q3option_3.configure(fg_color="black", text_color="white"))
        self.q3option_3.bind("<Leave>", lambda e: self.q3option_3.configure(fg_color="white", text_color="black"))
        self.q3option_4.bind("<Enter>", lambda e: self.q3option_4.configure(fg_color="black", text_color="white"))
        self.q3option_4.bind("<Leave>", lambda e: self.q3option_4.configure(fg_color="white", text_color="black"))

        self.q3option_1.configure(command=lambda: self.test_answer_3("option1"))
        self.q3option_2.configure(command=lambda: self.test_answer_3("option4"))
        self.q3option_3.configure(command=lambda: self.test_answer_3("option3"))
        self.q3option_4.configure(command=lambda: self.test_answer_3("correct_option"))

    def test_answer_3(self, selected_answer3):
        self.my_correct_option = "correct_option"
        self.selected_answer3 = selected_answer3

        if self.my_correct_option == self.selected_answer3:
            print("Correct !!!")
            self.q3option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q3option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q3option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q3option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q3option_1.unbind()  
            self.q3option_2.unbind()
            self.q3option_3.unbind()
            self.q3option_4.unbind()
            self.next3.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q3option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q3option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q3option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q3option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q3option_1.unbind()
            self.q3option_2.unbind()
            self.q3option_3.unbind()
            self.q3option_4.unbind()
            self.next3.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_4(self):
        self.question_1.configure(text=f"{self.question4}")

        self.q3option_1.pack_forget()
        self.q3option_2.pack_forget()
        self.q3option_3.pack_forget()
        self.q3option_4.pack_forget()

        self.next3.pack_forget()

        self.q4option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q4option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q4option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q4option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next4 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120)

        self.q4option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q4option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q4option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q4option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q4option_1.bind("<Enter>", lambda e: self.q4option_1.configure(fg_color="black", text_color="white"))
        self.q4option_1.bind("<Leave>", lambda e: self.q4option_1.configure(fg_color="white", text_color="black"))
        self.q4option_2.bind("<Enter>", lambda e: self.q4option_2.configure(fg_color="black", text_color="white"))
        self.q4option_2.bind("<Leave>", lambda e: self.q4option_2.configure(fg_color="white", text_color="black"))
        self.q4option_3.bind("<Enter>", lambda e: self.q4option_3.configure(fg_color="black", text_color="white"))
        self.q4option_3.bind("<Leave>", lambda e: self.q4option_3.configure(fg_color="white", text_color="black"))
        self.q4option_4.bind("<Enter>", lambda e: self.q4option_4.configure(fg_color="black", text_color="white"))
        self.q4option_4.bind("<Leave>", lambda e: self.q4option_4.configure(fg_color="white", text_color="black"))

        self.q4option_1.configure(command=lambda: self.test_answer_4("option1"))
        self.q4option_2.configure(command=lambda: self.test_answer_4("option4"))
        self.q4option_3.configure(command=lambda: self.test_answer_4("option3"))
        self.q4option_4.configure(command=lambda: self.test_answer_4("correct_option"))

    def test_answer_4(self, selected_answer4):
        self.my_correct_option = "correct_option"
        self.selected_answer4 = selected_answer4

        if self.my_correct_option == self.selected_answer4:
            print("Correct !!!")
            self.q4option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q4option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q4option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q4option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q4option_1.unbind()  
            self.q4option_2.unbind()
            self.q4option_3.unbind()
            self.q4option_4.unbind()
            self.next4.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q4option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q4option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q4option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q4option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q4option_1.unbind()
            self.q4option_2.unbind()
            self.q4option_3.unbind()
            self.q4option_4.unbind()
            self.next4.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
            
    def question_4(self):
        self.question_1.configure(text=f"{self.question4}")

        self.q3option_1.pack_forget()
        self.q3option_2.pack_forget()
        self.q3option_3.pack_forget()
        self.q3option_4.pack_forget()

        self.next3.pack_forget()

        self.q4option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q4option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q4option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q4option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q4option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next4 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_5)

        self.q4option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q4option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q4option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q4option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q4option_1.bind("<Enter>", lambda e: self.q4option_1.configure(fg_color="black", text_color="white"))
        self.q4option_1.bind("<Leave>", lambda e: self.q4option_1.configure(fg_color="white", text_color="black"))
        self.q4option_2.bind("<Enter>", lambda e: self.q4option_2.configure(fg_color="black", text_color="white"))
        self.q4option_2.bind("<Leave>", lambda e: self.q4option_2.configure(fg_color="white", text_color="black"))
        self.q4option_3.bind("<Enter>", lambda e: self.q4option_3.configure(fg_color="black", text_color="white"))
        self.q4option_3.bind("<Leave>", lambda e: self.q4option_3.configure(fg_color="white", text_color="black"))
        self.q4option_4.bind("<Enter>", lambda e: self.q4option_4.configure(fg_color="black", text_color="white"))
        self.q4option_4.bind("<Leave>", lambda e: self.q4option_4.configure(fg_color="white", text_color="black"))

        self.q4option_1.configure(command=lambda: self.test_answer_4("option1"))
        self.q4option_2.configure(command=lambda: self.test_answer_4("option4"))
        self.q4option_3.configure(command=lambda: self.test_answer_4("option3"))
        self.q4option_4.configure(command=lambda: self.test_answer_4("correct_option"))

    def test_answer_4(self, selected_answer4):
        self.my_correct_option = "correct_option"
        self.selected_answer4 = selected_answer4

        if self.my_correct_option == self.selected_answer4:
            print("Correct !!!")
            self.q4option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q4option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q4option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q4option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q4option_1.unbind()  
            self.q4option_2.unbind()
            self.q4option_3.unbind()
            self.q4option_4.unbind()
            self.next4.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q4option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q4option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q4option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q4option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q4option_1.unbind()
            self.q4option_2.unbind()
            self.q4option_3.unbind()
            self.q4option_4.unbind()
            self.next4.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_5(self):
        self.question_1.configure(text=f"{self.question5}")

        self.q4option_1.pack_forget()
        self.q4option_2.pack_forget()
        self.q4option_3.pack_forget()
        self.q4option_4.pack_forget()

        self.next4.pack_forget()

        self.q5option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q5option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q5option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q5option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q5option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q5option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q5option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q5option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next5 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_6)

        self.q5option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q5option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q5option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q5option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q5option_1.bind("<Enter>", lambda e: self.q5option_1.configure(fg_color="black", text_color="white"))
        self.q5option_1.bind("<Leave>", lambda e: self.q5option_1.configure(fg_color="white", text_color="black"))
        self.q5option_2.bind("<Enter>", lambda e: self.q5option_2.configure(fg_color="black", text_color="white"))
        self.q5option_2.bind("<Leave>", lambda e: self.q5option_2.configure(fg_color="white", text_color="black"))
        self.q5option_3.bind("<Enter>", lambda e: self.q5option_3.configure(fg_color="black", text_color="white"))
        self.q5option_3.bind("<Leave>", lambda e: self.q5option_3.configure(fg_color="white", text_color="black"))
        self.q5option_4.bind("<Enter>", lambda e: self.q5option_4.configure(fg_color="black", text_color="white"))
        self.q5option_4.bind("<Leave>", lambda e: self.q5option_4.configure(fg_color="white", text_color="black"))

        self.q5option_1.configure(command=lambda: self.test_answer_5("option1"))
        self.q5option_2.configure(command=lambda: self.test_answer_5("option4"))
        self.q5option_3.configure(command=lambda: self.test_answer_5("option3"))
        self.q5option_4.configure(command=lambda: self.test_answer_5("correct_option"))

    def test_answer_5(self, selected_answer5):
        self.my_correct_option = "correct_option"
        self.selected_answer5 = selected_answer5

        if self.my_correct_option == self.selected_answer5:
            print("Correct !!!")
            self.q5option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q5option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q5option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q5option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q5option_1.unbind()  
            self.q5option_2.unbind()
            self.q5option_3.unbind()
            self.q5option_4.unbind()
            self.next5.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q5option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q5option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q5option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q5option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q5option_1.unbind()
            self.q5option_2.unbind()
            self.q5option_3.unbind()
            self.q5option_4.unbind()
            self.next5.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_6(self):
        self.question_1.configure(text=f"{self.question6}")

        self.q5option_1.pack_forget()
        self.q5option_2.pack_forget()
        self.q5option_3.pack_forget()
        self.q5option_4.pack_forget()

        self.next5.pack_forget()

        self.q6option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q6option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q6option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q6option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q6option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q6option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q6option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q6option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next6 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_7)

        self.q6option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q6option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q6option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q6option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q6option_1.bind("<Enter>", lambda e: self.q6option_1.configure(fg_color="black", text_color="white"))
        self.q6option_1.bind("<Leave>", lambda e: self.q6option_1.configure(fg_color="white", text_color="black"))
        self.q6option_2.bind("<Enter>", lambda e: self.q6option_2.configure(fg_color="black", text_color="white"))
        self.q6option_2.bind("<Leave>", lambda e: self.q6option_2.configure(fg_color="white", text_color="black"))
        self.q6option_3.bind("<Enter>", lambda e: self.q6option_3.configure(fg_color="black", text_color="white"))
        self.q6option_3.bind("<Leave>", lambda e: self.q6option_3.configure(fg_color="white", text_color="black"))
        self.q6option_4.bind("<Enter>", lambda e: self.q6option_4.configure(fg_color="black", text_color="white"))
        self.q6option_4.bind("<Leave>", lambda e: self.q6option_4.configure(fg_color="white", text_color="black"))

        self.q6option_1.configure(command=lambda: self.test_answer_6("option1"))
        self.q6option_2.configure(command=lambda: self.test_answer_6("option4"))
        self.q6option_3.configure(command=lambda: self.test_answer_6("option3"))
        self.q6option_4.configure(command=lambda: self.test_answer_6("correct_option"))

    def test_answer_6(self, selected_answer6):
        self.my_correct_option = "correct_option"
        self.selected_answer6 = selected_answer6

        if self.my_correct_option == self.selected_answer6:
            print("Correct !!!")
            self.q6option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q6option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q6option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q6option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q6option_1.unbind()  
            self.q6option_2.unbind()
            self.q6option_3.unbind()
            self.q6option_4.unbind()
            self.next6.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q6option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q6option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q6option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q6option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q6option_1.unbind()
            self.q6option_2.unbind()
            self.q6option_3.unbind()
            self.q6option_4.unbind()
            self.next6.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_7(self):
        self.question_1.configure(text=f"{self.question7}")

        self.q6option_1.pack_forget()
        self.q6option_2.pack_forget()
        self.q6option_3.pack_forget()
        self.q6option_4.pack_forget()

        self.next6.pack_forget()

        self.q7option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q7option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q7option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q7option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q7option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q7option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q7option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q7option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next7 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_8)

        self.q7option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q7option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q7option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q7option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q7option_1.bind("<Enter>", lambda e: self.q7option_1.configure(fg_color="black", text_color="white"))
        self.q7option_1.bind("<Leave>", lambda e: self.q7option_1.configure(fg_color="white", text_color="black"))
        self.q7option_2.bind("<Enter>", lambda e: self.q7option_2.configure(fg_color="black", text_color="white"))
        self.q7option_2.bind("<Leave>", lambda e: self.q7option_2.configure(fg_color="white", text_color="black"))
        self.q7option_3.bind("<Enter>", lambda e: self.q7option_3.configure(fg_color="black", text_color="white"))
        self.q7option_3.bind("<Leave>", lambda e: self.q7option_3.configure(fg_color="white", text_color="black"))
        self.q7option_4.bind("<Enter>", lambda e: self.q7option_4.configure(fg_color="black", text_color="white"))
        self.q7option_4.bind("<Leave>", lambda e: self.q7option_4.configure(fg_color="white", text_color="black"))

        self.q7option_1.configure(command=lambda: self.test_answer_7("option1"))
        self.q7option_2.configure(command=lambda: self.test_answer_7("option4"))
        self.q7option_3.configure(command=lambda: self.test_answer_7("option3"))
        self.q7option_4.configure(command=lambda: self.test_answer_7("correct_option"))

    def test_answer_7(self, selected_answer7):
        self.my_correct_option = "correct_option"
        self.selected_answer7 = selected_answer7

        if self.my_correct_option == self.selected_answer7:
            print("Correct !!!")
            self.q7option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q7option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q7option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q7option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q7option_1.unbind()  
            self.q7option_2.unbind()
            self.q7option_3.unbind()
            self.q7option_4.unbind()
            self.next7.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q7option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q7option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q7option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q7option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q7option_1.unbind()
            self.q7option_2.unbind()
            self.q7option_3.unbind()
            self.q7option_4.unbind()
            self.next7.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_8(self):
        self.question_1.configure(text=f"{self.question8}")

        self.q7option_1.pack_forget()
        self.q7option_2.pack_forget()
        self.q7option_3.pack_forget()
        self.q7option_4.pack_forget()

        self.next7.pack_forget()

        self.q8option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q8option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q8option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q8option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q8option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q8option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q8option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q8option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next8 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_9)

        self.q8option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q8option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q8option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q8option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q8option_1.bind("<Enter>", lambda e: self.q8option_1.configure(fg_color="black", text_color="white"))
        self.q8option_1.bind("<Leave>", lambda e: self.q8option_1.configure(fg_color="white", text_color="black"))
        self.q8option_2.bind("<Enter>", lambda e: self.q8option_2.configure(fg_color="black", text_color="white"))
        self.q8option_2.bind("<Leave>", lambda e: self.q8option_2.configure(fg_color="white", text_color="black"))
        self.q8option_3.bind("<Enter>", lambda e: self.q8option_3.configure(fg_color="black", text_color="white"))
        self.q8option_3.bind("<Leave>", lambda e: self.q8option_3.configure(fg_color="white", text_color="black"))
        self.q8option_4.bind("<Enter>", lambda e: self.q8option_4.configure(fg_color="black", text_color="white"))
        self.q8option_4.bind("<Leave>", lambda e: self.q8option_4.configure(fg_color="white", text_color="black"))

        self.q8option_1.configure(command=lambda: self.test_answer_8("option1"))
        self.q8option_2.configure(command=lambda: self.test_answer_8("option4"))
        self.q8option_3.configure(command=lambda: self.test_answer_8("option3"))
        self.q8option_4.configure(command=lambda: self.test_answer_8("correct_option"))

    def test_answer_8(self, selected_answer8):
        self.my_correct_option = "correct_option"
        self.selected_answer8 = selected_answer8

        if self.my_correct_option == self.selected_answer8:
            print("Correct !!!")
            self.q8option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q8option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q8option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q8option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q8option_1.unbind()  
            self.q8option_2.unbind()
            self.q8option_3.unbind()
            self.q8option_4.unbind()
            self.next8.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q8option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q8option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q8option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q8option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q8option_1.unbind()
            self.q8option_2.unbind()
            self.q8option_3.unbind()
            self.q8option_4.unbind()
            self.next8.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_9(self):
        self.question_1.configure(text=f"{self.question9}")

        self.q8option_1.pack_forget()
        self.q8option_2.pack_forget()
        self.q8option_3.pack_forget()
        self.q8option_4.pack_forget()

        self.next8.pack_forget()
        
        self.source_img = Image.open("exit.png")
        self.close_image = ImageTk.PhotoImage(self.source_img.resize((40, 40)))

        self.exit = ct.CTkButton(self.option_fram, text="Exit Quiz", fg_color="red", hover_color="#cd2222", 
                                 text_color="white", width=120, height=35, image=self.close_image, compound=LEFT, command=quit)
        
        self.q9option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q9option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q9option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q9option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q9option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q9option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q9option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q9option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next9 = ct.CTkButton(self.option_fram, text="Next", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.question_10)

        self.q9option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q9option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q9option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q9option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q9option_1.bind("<Enter>", lambda e: self.q9option_1.configure(fg_color="black", text_color="white"))
        self.q9option_1.bind("<Leave>", lambda e: self.q9option_1.configure(fg_color="white", text_color="black"))
        self.q9option_2.bind("<Enter>", lambda e: self.q9option_2.configure(fg_color="black", text_color="white"))
        self.q9option_2.bind("<Leave>", lambda e: self.q9option_2.configure(fg_color="white", text_color="black"))
        self.q9option_3.bind("<Enter>", lambda e: self.q9option_3.configure(fg_color="black", text_color="white"))
        self.q9option_3.bind("<Leave>", lambda e: self.q9option_3.configure(fg_color="white", text_color="black"))
        self.q9option_4.bind("<Enter>", lambda e: self.q9option_4.configure(fg_color="black", text_color="white"))
        self.q9option_4.bind("<Leave>", lambda e: self.q9option_4.configure(fg_color="white", text_color="black"))

        self.q9option_1.configure(command=lambda: self.test_answer_9("option1"))
        self.q9option_2.configure(command=lambda: self.test_answer_9("option4"))
        self.q9option_3.configure(command=lambda: self.test_answer_9("option3"))
        self.q9option_4.configure(command=lambda: self.test_answer_9("correct_option"))

    def test_answer_9(self, selected_answer9):
        self.my_correct_option = "correct_option"
        self.selected_answer9 = selected_answer9

        if self.my_correct_option == self.selected_answer9:
            print("Correct !!!")
            self.q9option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q9option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q9option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q9option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q9option_1.unbind()  
            self.q9option_2.unbind()
            self.q9option_3.unbind()
            self.q9option_4.unbind()
            self.next9.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q9option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q9option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q9option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q9option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q9option_1.unbind()
            self.q9option_2.unbind()
            self.q9option_3.unbind()
            self.q9option_4.unbind()
            self.next9.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def question_10(self):
        self.question_1.configure(text=f"{self.question10}")

        self.q9option_1.pack_forget()
        self.q9option_2.pack_forget()
        self.q9option_3.pack_forget()
        self.q9option_4.pack_forget()

        self.next9.pack_forget()

        self.q10option_1 = ct.CTkButton(self.option_fram, text=f"  {self.q10option_1}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q10option_2 = ct.CTkButton(self.option_fram, text=f"  {self.q10option_2}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q10option_3 = ct.CTkButton(self.option_fram, text=f"  {self.q10option_3}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)
        self.q10option_4 = ct.CTkButton(self.option_fram, text=f"  {self.q10option_4}", fg_color="#fff", text_color="black", border_color="black", border_width=1, font=("Poppins", 15), height=40, anchor=W)

        self.next10 = ct.CTkButton(self.option_fram, text="Finish", fg_color="#001e4d", text_color="white", width=120, height=120, command=self.finish)

        self.q10option_2.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q10option_3.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q10option_4.pack(fill=X, padx=25, pady=self.option_padding_y)
        self.q10option_1.pack(fill=X, padx=25, pady=self.option_padding_y)
        
        self.q10option_1.bind("<Enter>", lambda e: self.q10option_1.configure(fg_color="black", text_color="white"))
        self.q10option_1.bind("<Leave>", lambda e: self.q10option_1.configure(fg_color="white", text_color="black"))
        self.q10option_2.bind("<Enter>", lambda e: self.q10option_2.configure(fg_color="black", text_color="white"))
        self.q10option_2.bind("<Leave>", lambda e: self.q10option_2.configure(fg_color="white", text_color="black"))
        self.q10option_3.bind("<Enter>", lambda e: self.q10option_3.configure(fg_color="black", text_color="white"))
        self.q10option_3.bind("<Leave>", lambda e: self.q10option_3.configure(fg_color="white", text_color="black"))
        self.q10option_4.bind("<Enter>", lambda e: self.q10option_4.configure(fg_color="black", text_color="white"))
        self.q10option_4.bind("<Leave>", lambda e: self.q10option_4.configure(fg_color="white", text_color="black"))

        self.q10option_1.configure(command=lambda: self.test_answer_10("option1"))
        self.q10option_2.configure(command=lambda: self.test_answer_10("option4"))
        self.q10option_3.configure(command=lambda: self.test_answer_10("option3"))
        self.q10option_4.configure(command=lambda: self.test_answer_10("correct_option"))

    def test_answer_10(self, selected_answer10):
        self.my_correct_option = "correct_option"
        self.selected_answer10 = selected_answer10

        if self.my_correct_option == self.selected_answer10:
            print("Correct !!!")
            self.q10option_1.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q10option_2.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q10option_3.configure(fg_color="white", text_color="black", border_width=1.5, state="disabled")
            self.q10option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.score += 1
            self.score_lbl.configure(text=f"Score : {self.score}")
            print(f"Score : {self.score}")
            self.q10option_1.unbind()  
            self.q10option_2.unbind()
            self.q10option_3.unbind()
            self.q10option_4.unbind()
            self.next10.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)
        else:
            self.q10option_1.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q10option_2.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q10option_3.configure(fg_color="#ff9393", text_color="black", border_width=1.5, state="disabled")
            self.q10option_4.configure(fg_color="#9aeabc", text_color="black", border_width=1.5, state="disabled")
            self.q10option_1.unbind()
            self.q10option_2.unbind()
            self.q10option_3.unbind()
            self.q10option_4.unbind()
            self.next10.pack(side=BOTTOM, pady=7, ipadx=5, ipady=10)

    def finish(self):
        self.question_1.pack_forget()
        self.q10option_1.pack_forget()
        self.q10option_2.pack_forget()
        self.q10option_3.pack_forget()
        self.q10option_4.pack_forget()
        self.next10.pack_forget()
        self.line.pack_forget()
        
        self.meter = tw.Meter(
            self.option_fram,
            amounttotal=10,
            amountused=0,
            meterthickness=20,
            bootstyle=tw.INFO,
            metersize=300,
            subtext="SCORE",
            subtextfont=("Calibri (Body)", 24, "bold"),
            subtextstyle=tw.DARK
            )

        self.exit.pack(side=BOTTOM, pady=7, ipadx=5, ipady=0)
        self.meter.pack(ipadx=228, ipady=100, pady=60)

        global count
        count = 0
        threading.Thread(target=lambda: self.wait(5)).start()
        threading.Thread(target=self.my_second).start()
           
    def my_second(self):
        global count
        if count <= self.score:
            self.meter['amountused'] = count 
            count += 1
            self.option_fram.after(10, self.my_second) 
        else:
            count = 0

    def wait(self, duration):
        time.sleep(duration)

my_question_1 = "1. World's largest continent ???"
my_question_2 = "2. Who invented computer ???"
my_question_3 = "3. What is the name of largest ocean ???"
my_question_4 = "4. What is capital of India ???"
my_question_5 = "5. Who invented Google ???"
my_question_6 = "6. World largest country in Area ???"
my_question_7 = "7. What is full form of OOP ???"
my_question_8 = "8. Largest mammel on earth ???"
my_question_9 = "9. National sports of India ???"
my_question_10 = "10. Largest planet in solar system ???"

Quiz(root, 
    question_1=my_question_1, q1option_1 = "Antartica", q1option_2 = "Africa", q1option_3 = "Europe", q1correct_option = "Asia",
    question_2=my_question_2, q2option_1 = "Albert Einstein", q2option_2 = "Issac Newton", q2option_3 = "Tom Schimansky", q2correct_option = "Charles Babbage",
    question_3=my_question_3, q3option_1 = "Artic Ocean", q3option_2 = "Atlantic Ocean", q3option_3 = "Antartic Ocean", q3correct_option = "Pacific Ocean",
    question_4=my_question_4, q4option_1 = "Moscow", q4option_2 = "Washington DC", q4option_3 = "Tokyo", q4correct_option = "New Delhi",
    question_5=my_question_5, q5option_1 = "Billy Eat Cookies", q5option_2 = "Steve Jobs", q5option_3 = "Bill Gates", q5correct_option = "Larry Page",
    question_6=my_question_6, q6option_1 = "India", q6option_2 = "China", q6option_3 = "America", q6correct_option = "Russia",
    question_7=my_question_7, q7option_1 = "Object Of Programming", q7option_2 = "Obstacle of Programming", q7option_3 = "Object Of Power", q7correct_option = "Object Oriented Programming",
    question_8=my_question_8, q8option_1 = "Shark", q8option_2 = "Dolphin", q8option_3 = "Elephant", q8correct_option = "Blue Whale",
    question_9=my_question_9, q9option_1 = "Baseball", q9option_2 = "Football", q9option_3 = "Baksetball", q9correct_option = "Hockey",
    question_10=my_question_10, q10option_1 = "Mercury", q10option_2 = "Earth", q10option_3 = "Mars", q10correct_option = "Jupiter")

cProfile.run("root.mainloop()")