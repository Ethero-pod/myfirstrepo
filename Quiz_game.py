#API 
import requests
import random
import tkinter as tk 
from tkinter import messagebox
rspns = requests.get("https://opentdb.com/api.php?amount=5&type=multiple")
                    
data = rspns.json()# data = rspns.text

i =0

q1 = data.get("results")[i]
q2 = q1.get("question")

# options  

opt1 = data.get("results")[i]
opt2 = opt1.get("incorrect_answers")
opt2.append(opt1.get("correct_answer"))
random.shuffle(opt2)

# correct_answer
ans1 = data.get("results")[i]
ans2 = ans1.get("correct_answer")

fr = tk.Tk()
fr.geometry("700x450")



def view1():
    if opt2[0] == ans2 :    
        messagebox.showinfo(opt2[0],"your answer is correct")
    else :
        messagebox.showinfo("Result", f"{opt2[0]} is incorrect\nCorrect answer: {ans2}")
def view2():
    if opt2[1] == ans2 :
        messagebox.showinfo(opt2[1],"your answer is correct")
    else :
        messagebox.showinfo("Result", f"{opt2[1]} is incorrect\nCorrect answer: {ans2}")
def view3():
    if opt2[2] == ans2 :
        messagebox.showinfo(opt2[2],"your answer is correct")
    else :
        messagebox.showinfo("Result", f"{opt2[2]} is incorrect\nCorrect answer: {ans2}")
def view4():
    if opt2[3 == ans2] :
        messagebox.showinfo(opt2[3],"your answer is correct")
    else :
        messagebox.showinfo("Result", f"{opt2[3]} is incorrect\nCorrect answer: {ans2}")
def view5():
    Newpage1(fr)
# def ans():
#     messagebox.showinfo("result","your answer is correct")


score_label = tk.Label(fr, text="Score: 0", font=('Arial', 12))
score_label.pack(pady=10)


# question_label = tk.Label(fr, text=q2, wraplength=500, font=('Arial', 14))
# question_label.pack(pady=20)

# btn1 = tk.Button(fr,text = opt2[0] ,width = 20,height = 2,command = view1 )
# btn1.place(x=75,y=200)

# btn2 = tk.Button(fr,text = opt2[1] ,width = 20,height = 2,command = view2 )
# btn2.place(x=450,y=200)

# btn3 = tk.Button(fr,text = opt2[2] ,width = 20,height = 2,command = view3 )
# btn3.place(x=75,y=300)

# btn4 = tk.Button(fr,text = opt2[3],width = 20,height = 2,command = view4 )
# btn4.place(x=450,y=300)

# btn5 = tk.Button(fr,text = "NEXT",width = 20,height = 2,command = view5 )
# btn5.place(x=265,y=380)


question_label = tk.Label(fr, text=q2, wraplength=500, font=('Arial', 14))
question_label.pack(pady=20)

btn1 = tk.Button(fr,text = opt2[0] ,width = 20,height = 2,command = view1 )
btn1.place(x=75,y=200)

btn2 = tk.Button(fr,text = opt2[1] ,width = 20,height = 2,command = view2 )
btn2.place(x=450,y=200)

btn3 = tk.Button(fr,text = opt2[2] ,width = 20,height = 2,command = view3 )
btn3.place(x=75,y=300)

btn4 = tk.Button(fr,text = opt2[3],width = 20,height = 2,command = view4 )
btn4.place(x=450,y=300)

btn5 = tk.Button(fr,text = "NEXT",width = 20,height = 2,command = view5 )
btn5.place(x=265,y=380)

class Newpage1 :
    def __init__(self,master):

        page2 = tk.Toplevel(fr)
        page2.geometry("700x450")
        page2.title("New page")

        
        














fr.mainloop  ()

