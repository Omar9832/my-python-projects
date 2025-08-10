import tkinter as tk
import tkinter.messagebox as messagebox


class GUI:
    def __init__(self):
        self.points=0
        self.main=tk.Tk()
        self.main.geometry("800x800")
        self.mainbackroundimage=tk.PhotoImage(file="red.png")
        self.mainbackroundlabel=tk.Label(self.main, image=self.mainbackroundimage)
        self.mainbackroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.main.title("Home")
        self.mainlabel=tk.Label(self.main, text="Welcome to guess the logo, which quiz do you want to take?", font=("Arial", 20), height=1)
        self.mainlabel.place(x=600, y=200)
        self.mainframe=tk.Frame(self.main, highlightbackground="black", highlightthickness=5)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainbutton1=tk.Button(self.mainframe, text="Quiz 1", height=5, width=20, bg="green", font=("Arial", 15), command=self.gotoquiz1start)
        self.mainbutton1.grid(row=0, column=0, sticky="we")
        self.mainbutton2=tk.Button(self.mainframe, text="Quiz 2", font=("Arial", 15), height=5, width=20, bg="red", command=self.gotoquiz2start)
        self.mainbutton2.grid(row=0, column=1, sticky="we")
        self.mainbutton3=tk.Button(self.mainframe, text="Quiz 3", font=("Arial", 15), bg="blue", height=5, width=20, command=self.gotoquiz3start)
        self.mainbutton3.grid(row=1, column=0, sticky="we")
        self.mainbutton4=tk.Button(self.mainframe, text="Quiz 4", font=("Arial", 15), height=5, width=20, bg="orange", command=self.gotoquiz4start)
        self.mainbutton4.grid(row=1, column=1, sticky="we")
        self.mainframe.place(x=750, y=300)
        self.mainclose=tk.Button(self.main, text="CLOSE", height=5, width=15, bg="maroon", font=("Arial", 15), command=self.closemain)
        self.mainclose.place(x=875, y=600)
        self.main.mainloop()
    def closemain(self):
        self.main.destroy()

    def gotoquiz1start(self):
        self.main.withdraw()
        self.quiz1start=tk.Toplevel(self.main)
        self.quiz1start.geometry("1100x1100")
        self.quiz1start.configure(bg="aqua")
        self.quiz1start.title("Start Quiz 1")
        self.quiz1startlabel=tk.Label(self.quiz1start, text="Click to start Quiz 1", relief="ridge", fg="black", bg="aqua", font=("Arial", 20), height=5)
        self.quiz1startlabel.pack(padx=10, pady=10)
        bcolorstart="#141414"
        fcolorstart="#ffcc66"
        self.quiz1startbutton=tk.Button(self.quiz1start, text="Start", bg=bcolorstart, fg=fcolorstart, height=5, width=30, font=("Arial", 15), command=self.gotoquiz1question1)
        self.quiz1startbutton.pack(padx=250, pady=250)
        self.quiz1startbutton.bind("<Enter>", lambda event:self.on_enterstart(event, bcolorstart, fcolorstart))
        self.quiz1startbutton.bind("<Leave>", lambda event:self.on_leavestart(event, bcolorstart, fcolorstart))
        self.quiz1start.mainloop()
    def on_enterstart(self, event, bcolorstart, fcolorstart):
        self.quiz1startbutton["background"]=fcolorstart
        self.quiz1startbutton["foreground"]=bcolorstart
    def on_leavestart(self, event, bcolorstart, fcolorstart):
        self.quiz1startbutton["background"]=bcolorstart
        self.quiz1startbutton["foreground"]=fcolorstart
    
    
    def gotoquiz1question1(self):
        self.quiz1start.withdraw()
        self.quiz1question1=tk.Toplevel(self.main)
        self.quiz1question1.geometry("1500x1500")
        self.quiz1question1backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz1question1backroundlabel=tk.Label(self.quiz1question1, image=self.quiz1question1backroundimage)
        self.quiz1question1backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz1question1.title("Quiz 1 Question 1")
        self.quiz1question1label=tk.Label(self.quiz1question1,text="Question 1", height=5, width=15, bg="red", fg="blue", font=("Arial", 15))
        self.quiz1question1label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz1question1, text=f"Points: {self.points}", height=2, bg="purple", font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image1=tk.PhotoImage(file="Volk.png")
        self.image1label=tk.Label(self.quiz1question1, image=self.image1, bd=5, relief="sunken")
        self.image1label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz1question1button1=tk.Button(self.quiz1question1, text="Toyota", height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquiz1question2("Toyota"))
        self.quiz1question1button1.pack(padx=10, pady=10)
        self.quiz1question1button1.bind("<Enter>", lambda event:self.on_enter1(event, bcolor1, fcolor1))
        self.quiz1question1button1.bind("<Leave>", lambda event:self.on_leave1(event, bcolor1, fcolor1))
        self.quiz1question1button2=tk.Button(self.quiz1question1, text="Honda", height=2, font=("Arial", 15), bg=bcolor2, fg=fcolor2, command=lambda:self.gotoquiz1question2("Honda"), width=40)
        self.quiz1question1button2.pack(padx=10, pady=10)
        self.quiz1question1button2.bind("<Enter>", lambda event:self.on_enter2(event, bcolor2, fcolor2))
        self.quiz1question1button2.bind("<Leave>", lambda event:self.on_leave2(event, bcolor2, fcolor2))
        self.quiz1question1button3=tk.Button(self.quiz1question1, text="Mazda", height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquiz1question2("Mazda"))
        self.quiz1question1button3.pack(padx=10, pady=10)
        self.quiz1question1button3.bind("<Enter>", lambda event:self.on_enter3(event, bcolor3, fcolor3))
        self.quiz1question1button3.bind("<Leave>", lambda event:self.on_leave3(event, bcolor3, fcolor3))
        self.quiz1question1button4=tk.Button(self.quiz1question1, text="Volkswagen", height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquiz1question2("Volkswagen"))
        self.quiz1question1button4.pack(padx=10, pady=10)
        self.quiz1question1button4.bind("<Enter>", lambda event:self.on_enter4(event, bcolor4, fcolor4))
        self.quiz1question1button4.bind("<Leave>", lambda event:self.on_leave4(event, bcolor4, fcolor4))
        self.quiz1question1.mainloop()

    def on_enter1(self, event, bcolor1, fcolor1):
        self.quiz1question1button1["background"]=fcolor1
        self.quiz1question1button1["foreground"]=bcolor1
    def on_leave1(self, event, bcolor1, fcolor1):
        self.quiz1question1button1["background"]=bcolor1
        self.quiz1question1button1["foreground"]=fcolor1
    def on_enter2(self, event, bcolor2, fcolor2):
        self.quiz1question1button2["background"]=fcolor2
        self.quiz1question1button2["foreground"]=bcolor2
    def on_leave2(self, event, bcolor2, fcolor2):
        self.quiz1question1button2["background"]=bcolor2
        self.quiz1question1button2["foreground"]=fcolor2
    def on_enter3(self, event, bcolor3, fcolor3):
        self.quiz1question1button3["background"]=fcolor3
        self.quiz1question1button3["foreground"]=bcolor3
    def on_leave3(self, event, bcolor3, fcolor3):
        self.quiz1question1button3["background"]=bcolor3
        self.quiz1question1button3["foreground"]=fcolor3
    def on_enter4(self, event, bcolor4, fcolor4):
        self.quiz1question1button4["background"]=fcolor4
        self.quiz1question1button4["foreground"]=bcolor4
    def on_leave4(self, event, bcolor4, fcolor4):
        self.quiz1question1button4["background"]=bcolor4
        self.quiz1question1button4["foreground"]=fcolor4
   
    

  
    
    def gotoquiz1question2(self, button_text1):
        if button_text1=="Volkswagen":
            self.points=self.points+100
        self.quiz1question1.withdraw()
        self.quiz1question2=tk.Toplevel(self.main)
        self.quiz1question2.geometry("1100x1100")
        self.quiz1question2.title("Question 2")
        self.quiz1question2backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz1question2backroundlabel=tk.Label(self.quiz1question2, image=self.quiz1question2backroundimage)
        self.quiz1question2backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz1question2label=tk.Label(self.quiz1question2, text="Question 2", font=("Arial", 20), bg="red", fg="blue")
        self.quiz1question2label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz1question2, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image2=tk.PhotoImage(file="Toyota.png")
        self.image2label=tk.Label(self.quiz1question2, image=self.image2, bd=5, relief="sunken")
        self.image2label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"

        self.quiz1question2button1=tk.Button(self.quiz1question2, text="Acura", bg=bcolor1, fg=fcolor1, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz1question3("Acura"))
        self.quiz1question2button1.pack(padx=10, pady=10)
        self.quiz1question2button1.bind("<Enter>", lambda event: self.on_enter5(event, bcolor1, fcolor1))
        self.quiz1question2button1.bind("<Leave>", lambda event: self.on_leave5(event, bcolor1, fcolor1))
        self.quiz1question2button2=tk.Button(self.quiz1question2, text="Toyota", bg=bcolor2, fg=fcolor2, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1question3("Toyota"))
        self.quiz1question2button2.pack(padx=10, pady=10)
        self.quiz1question2button2.bind("<Enter>", lambda event: self.on_enter6(event, bcolor2, fcolor2))
        self.quiz1question2button2.bind("<Leave>", lambda event: self.on_leave6(event, bcolor2, fcolor2))
        self.quiz1question2button3=tk.Button(self.quiz1question2, text="Audi", bg=bcolor3, fg=fcolor3, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1question3("Audi"))
        self.quiz1question2button3.pack(padx=10, pady=10)
        self.quiz1question2button3.bind("<Enter>", lambda event: self.on_enter7(event, bcolor3, fcolor3))
        self.quiz1question2button3.bind("<Leave>", lambda event: self.on_leave7(event, bcolor3, fcolor3))
        self.quiz1question2button4=tk.Button(self.quiz1question2, text="Buick", bg=bcolor4, fg=fcolor4, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1question3("Buick"))
        self.quiz1question2button4.pack(padx=10, pady=10)
        self.quiz1question2button4.bind("<Enter>", lambda event: self.on_enter8(event, bcolor4, fcolor4))
        self.quiz1question2button4.bind("<Leave>", lambda event: self.on_leave8(event, bcolor4, fcolor4))
        self.quiz1question2.mainloop()

    def on_enter5(self, event, bcolor1, fcolor1):
        self.quiz1question2button1["background"]=fcolor1
        self.quiz1question2button1["foreground"]=bcolor1
    def on_leave5(self, event, bcolor1, fcolor1):
        self.quiz1question2button1["background"]=bcolor1
        self.quiz1question2button1["foreground"]=fcolor1
    def on_enter6(self, event, bcolor2, fcolor2):
        self.quiz1question2button2["background"]=fcolor2
        self.quiz1question2button2["foreground"]=bcolor2
    def on_leave6(self, event, bcolor2, fcolor2):
        self.quiz1question2button2["background"]=bcolor2
        self.quiz1question2button2["foreground"]=fcolor2
    def on_enter7(self, event, bcolor3, fcolor3):
        self.quiz1question2button3["background"]=fcolor3
        self.quiz1question2button3["foreground"]=bcolor3
    def on_leave7(self, event, bcolor3, fcolor3):
        self.quiz1question2button3["background"]=bcolor3
        self.quiz1question2button3["foreground"]=fcolor3
    def on_enter8(self, event, bcolor4, fcolor4):
        self.quiz1question2button4["background"]=fcolor4
        self.quiz1question2button4["foreground"]=bcolor4
    def on_leave8(self, event, bcolor4, fcolor4):
        self.quiz1question2button4["background"]=bcolor4
        self.quiz1question2button4["foreground"]=fcolor4
        
    def gotoquiz1question3(self, button_text2):
        if button_text2=="Toyota":
            self.points=self.points+100
        self.quiz1question2.withdraw()
        self.quiz1question3=tk.Toplevel(self.main)
        self.quiz1question3.geometry("1100x1100")
        self.quiz1question3backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz1question3backroundlabel=tk.Label(self.quiz1question3, image=self.quiz1question3backroundimage)
        self.quiz1question3backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz1question3.title("Question 3")
        self.quiz1question3label=tk.Label(self.quiz1question3, text="Question 3", bg="red", fg="blue", font=("Arial", 20), height=5)
        self.quiz1question3label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz1question3, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image3=tk.PhotoImage(file="Citroen.png")
        self.image3label=tk.Label(self.quiz1question3, image=self.image3, bd=5, relief="sunken")
        self.image3label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz1question3button1=tk.Button(self.quiz1question3, text="BMW", bg=bcolor1, fg=fcolor1, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1question4("BMW"))
        self.quiz1question3button1.pack(padx=10, pady=10)
        self.quiz1question3button1.bind("<Enter>", lambda event: self.on_enter9(event, bcolor1, fcolor1))
        self.quiz1question3button1.bind("<Leave>", lambda event: self.on_leave9(event, bcolor1, fcolor1))
        self.quiz1question3button2=tk.Button(self.quiz1question3, text="Alfa Romeo", bg=bcolor2, fg=fcolor2, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1question4("Alfa Romeo"))
        self.quiz1question3button2.pack(padx=10, pady=10)
        self.quiz1question3button2.bind("<Enter>", lambda event: self.on_enter10(event, bcolor2, fcolor2))
        self.quiz1question3button2.bind("<Leave>", lambda event: self.on_leave10(event, bcolor2, fcolor2))
        self.quiz1question3button3=tk.Button(self.quiz1question3, text="Citroën", bg=bcolor3, fg=fcolor3, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1question4("Citroën"))
        self.quiz1question3button3.pack(padx=10, pady=10)
        self.quiz1question3button3.bind("<Enter>", lambda event: self.on_enter11(event, bcolor3, fcolor3))
        self.quiz1question3button3.bind("<Leave>", lambda event: self.on_leave11(event, bcolor3, fcolor3))
        self.quiz1question3button4=tk.Button(self.quiz1question3, text="Chevrolet", bg=bcolor4, fg=fcolor4, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1question4("Chevrolet"))
        self.quiz1question3button4.pack(padx=10, pady=10)
        self.quiz1question3button4.bind("<Enter>", lambda event: self.on_enter12(event, bcolor4, fcolor4))
        self.quiz1question3button4.bind("<Leave>", lambda event: self.on_leave12(event, bcolor4, fcolor4))
        self.quiz1question3.mainloop()
    
    def on_enter9(self, event, bcolor1, fcolor1):
        self.quiz1question3button1["background"]=fcolor1
        self.quiz1question3button1["foreground"]=bcolor1
    def on_leave9(self, event, bcolor1, fcolor1):
        self.quiz1question3button1["background"]=bcolor1
        self.quiz1question3button1["foreground"]=fcolor1
    def on_enter10(self, event, bcolor2, fcolor2):
        self.quiz1question3button2["background"]=fcolor2
        self.quiz1question3button2["foreground"]=bcolor2
    def on_leave10(self, event, bcolor2, fcolor2):
        self.quiz1question3button2["background"]=bcolor2
        self.quiz1question3button2["foreground"]=fcolor2
    def on_enter11(self, event, bcolor3, fcolor3):
        self.quiz1question3button3["background"]=fcolor3
        self.quiz1question3button3["foreground"]=bcolor3
    def on_leave11(self, event, bcolor3, fcolor3):
        self.quiz1question3button3["background"]=bcolor3
        self.quiz1question3button3["foreground"]=fcolor3
    def on_enter12(self, event, bcolor4, fcolor4):
        self.quiz1question3button4["background"]=fcolor4
        self.quiz1question3button4["foreground"]=bcolor4
    def on_leave12(self, event, bcolor4, fcolor4):
        self.quiz1question3button4["background"]=bcolor4
        self.quiz1question3button4["foreground"]=fcolor4
        
        
    def gotoquiz1question4(self, button_text3):
        if button_text3=="Citroën":
            self.points=self.points+100
        self.quiz1question3.withdraw()
        self.quiz1question4=tk.Toplevel(self.main)
        self.quiz1question4.geometry("1100x1100")
        self.quiz1question4backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz1question4backroundlabel=tk.Label(self.quiz1question4, image=self.quiz1question4backroundimage)
        self.quiz1question4backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz1question4.title("Question 4")
        self.quiz1question4label=tk.Label(self.quiz1question4, text="Question 4", bg="red", fg="blue", font=("Arial", 20), height=5)
        self.quiz1question4label.pack(padx=10, pady=10)
        self.scoreframe=tk.Frame(self.quiz1question4)
        self.scoreframe.columnconfigure(0, weight=1)
        self.scoreframe.columnconfigure(1, weight=1)
        self.score=tk.Label(self.quiz1question4, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image4=tk.PhotoImage(file="Koenigsegg.png")
        self.image4label=tk.Label(self.quiz1question4, image=self.image4, bd=5, relief="sunken")
        self.image4label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz1question4button1=tk.Button(self.quiz1question4, text="Aston Martin", bg=bcolor1, fg=fcolor1, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1finish("Aston Martin"))
        self.quiz1question4button1.pack(padx=10, pady=10)
        self.quiz1question4button1.bind("<Enter>", lambda event: self.on_enter13(event, bcolor1, fcolor1))
        self.quiz1question4button1.bind("<Leave>", lambda event: self.on_leave13(event, bcolor1, fcolor1))
        self.quiz1question4button2=tk.Button(self.quiz1question4, text="Bugatti", bg=bcolor2, fg=fcolor2, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1finish("Bugatti"))
        self.quiz1question4button2.pack(padx=10, pady=10)
        self.quiz1question4button2.bind("<Enter>", lambda event: self.on_enter14(event, bcolor2, fcolor2))
        self.quiz1question4button2.bind("<Leave>", lambda event: self.on_leave14(event, bcolor2, fcolor2))
        self.quiz1question4button3=tk.Button(self.quiz1question4, text="Mclaren", bg=bcolor3,fg=fcolor3, font=("Arial", 15), height=2, width=40, command=lambda:self.gotoquiz1finish("Mclaren"))
        self.quiz1question4button3.pack(padx=10, pady=10)
        self.quiz1question4button3.bind("<Enter>", lambda event: self.on_enter15(event, bcolor3, fcolor3))
        self.quiz1question4button3.bind("<Leave>", lambda event: self.on_leave15(event, bcolor3, fcolor3))
        self.quiz1question4button4=tk.Button(self.quiz1question4, text="Koenigsegg", bg=bcolor4, fg=fcolor4, font=("Arial", 15), height=2, width=40, command=lambda: self.gotoquiz1finish("Koenigsegg"))
        self.quiz1question4button4.pack(padx=10, pady=10)
        self.quiz1question4button4.bind("<Enter>", lambda event: self.on_enter16(event, bcolor4, fcolor4))
        self.quiz1question4button4.bind("<Leave>", lambda event: self.on_leave16(event, bcolor4, fcolor4))
        self.quiz1question4.mainloop()
    def on_enter13(self, event, bcolor1, fcolor1):
        self.quiz1question4button1["background"]=fcolor1
        self.quiz1question4button1["foreground"]=bcolor1
    def on_leave13(self, event, bcolor1, fcolor1):
        self.quiz1question4button1["background"]=bcolor1
        self.quiz1question4button1["foreground"]=fcolor1
    def on_enter14(self, event, bcolor2, fcolor2):
        self.quiz1question4button2["background"]=fcolor2
        self.quiz1question4button2["foreground"]=bcolor2
    def on_leave14(self, event, bcolor2, fcolor2):
        self.quiz1question4button2["background"]=bcolor2
        self.quiz1question4button2["foreground"]=fcolor2
    def on_enter15(self, event, bcolor3, fcolor3):
        self.quiz1question4button3["background"]=fcolor3
        self.quiz1question4button3["foreground"]=bcolor3
    def on_leave15(self, event, bcolor3, fcolor3):
        self.quiz1question4button3["background"]=bcolor3
        self.quiz1question4button3["foreground"]=fcolor3
    def on_enter16(self, event, bcolor4, fcolor4):
        self.quiz1question4button4["background"]=fcolor4
        self.quiz1question4button4["foreground"]=bcolor4
    def on_leave16(self, event, bcolor4, fcolor4):
        self.quiz1question4button4["background"]=bcolor4
        self.quiz1question4button4["foreground"]=fcolor4
    
       
        
    def gotoquiz1finish(self, button_text4):
        if button_text4=="Koenigsegg":
            self.points=self.points+100
        self.quiz1question4.withdraw()
        self.quiz1finish=tk.Toplevel(self.main)
        self.quiz1finish.geometry("1100x1100")
        self.quiz1finishbackroundimage=tk.PhotoImage(file="cool.png")
        self.quiz1finishbackroundimagelabel=tk.Label(self.quiz1finish, image=self.quiz1finishbackroundimage)
        self.quiz1finishbackroundimagelabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz1finish.title("Quiz 1 finished")
        self.quiz1finishlabel1=tk.Label(self.quiz1finish, text="You have finished the quiz!", bg="red", fg="blue", font=("Arial", 20), height=5)
        self.quiz1finishlabel1.pack(padx=10, pady=10)
        self.quiz1finishframe1=tk.Frame(self.quiz1finish)
        self.quiz1finishframe1.columnconfigure(0, weight=1)
        self.quiz1finishframe1.columnconfigure(1, weight=1)
        self.quiz1finishlabel3=tk.Label(self.quiz1finishframe1, text=f"Total points: {self.points}", font=("Arial", 18), height=5)
        self.quiz1finishlabel3.grid(row=0, column=1)
        self.quiz1finishframe1.place(x=400, y=400)
        self.quiz1finishframe2=tk.Frame(self.quiz1finish)
        self.quiz1finishframe2.columnconfigure(0, weight=1)
        self.quiz1finishframe2.columnconfigure(1, weight=1)
        self.quiz1finishframe2.columnconfigure(2, weight=1)
        self.quiz1finishframe2.columnconfigure(3, weight=1)
        self.quiz1finishbutton1=tk.Button(self.quiz1finishframe2, text="Home", bg="red", font=("Arial", 15), height=5, command=self.__init__)
        self.quiz1finishbutton1.grid(row=0, column=0, sticky="we")
        self.quiz1finishbutton2=tk.Button(self.quiz1finishframe2, text="CLOSE", bg="blue", font=("Arial", 15), height=5, command=self.quiz1finish)
        self.quiz1finishbutton2.grid(row=0, column=1, sticky="we")
        self.quiz1finishbutton3=tk.Button(self.quiz1finishframe2, text="Quiz 1 Answer Key", height=5, bg="green", font=("Arial", 15), command=self.gotoquiz1answerkey)
        self.quiz1finishbutton3.grid(row=0, column=3)
        self.quiz1finishbutton4=tk.Button(self.quiz1finishframe2, text="Rate Us", height=5, font=("Arial", 15), bg="orange", command=self.gotorateus)
        self.quiz1finishbutton4.grid(row=0, column=3)
        self.quiz1finishframe2.pack(padx=10, pady=10)
        self.quiz1finish.mainloop()
    
    def closequiz1finish(self):
        self.quiz1finish.destroy()
    
    def gotorateus(self):
        self.quiz1finish.withdraw()
        self.rateus=tk.Toplevel(self.main)
        self.rateus.geometry("1000x1000")
        self.rateus.configure(bg="aqua")
        self.rateus.title("Rate Us")
        self.rateuslabel1=tk.Label(self.rateus, text="Rate Us", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.rateuslabel1.pack(padx=10, pady=10)
        self.rateusframe1=tk.Frame(self.rateus)
        self.rateusframe1.columnconfigure(0, weight=1)
        self.rateusframe1.columnconfigure(1, weight=1)
        self.rateusframe1.columnconfigure(2, weight=1)
        self.rateusframe1.columnconfigure(3, weight=1)
        self.rateusframe1.columnconfigure(4, weight=1)
        self.checkvar1=tk.BooleanVar()
        self.checkvar2=tk.BooleanVar()
        self.checkvar3=tk.BooleanVar()
        self.checkvar4=tk.BooleanVar()
        self.checkvar5=tk.BooleanVar()
        self.checkvar6=tk.BooleanVar()
        self.rateuslabel2=tk.Label(self.rateusframe1, text="How good was our application?", height=5, font=("Arial", 20), bg="black")
        self.rateuslabel2.grid(row=0, column=0)
        self.rateuscheckbutton1=tk.Checkbutton(self.rateusframe1, text="Solid", height=5, font=("Arial", 15), command=self.togglecheck1, variable=self.checkvar1)
        self.rateuscheckbutton1.grid(row=0, column=1)
        self.rateuscheckbutton2=tk.Checkbutton(self.rateusframe1, text="Decent", height=5, font=("Arial", 15), command=self.togglecheck2, variable=self.checkvar2)
        self.rateuscheckbutton2.grid(row=0, column=2)
        self.rateuscheckbutton3=tk.Checkbutton(self.rateusframe1, text="Bad", height=5, font=("Arial", 15), command=self.togglecheck3, variable=self.checkvar3)
        self.rateuscheckbutton3.grid(row=0, column=3)
        self.rateuscheckbutton4=tk.Checkbutton(self.rateusframe1, text="Really Bad", height=5, font=("Arial", 15), command=self.togglecheck4, variable=self.checkvar4)
        self.rateuscheckbutton4.grid(row=0, column=4)
        self.rateuslabel3=tk.Label(self.rateusframe1, text="Do you think there are any improvements/adjustments that can be made?If yes explain?", height=5, font=("Arial", 20), bg="black")
        self.rateuslabel3.grid(row=1, column=0)
        self.rateuscheckbutton5=tk.Checkbutton(self.rateusframe1, text="YES", height=5, font=("Arial", 15), command=lambda:[self.gotocommenttextbox, self.togglecheck5], variable=self.checkvar5)
        self.rateuscheckbutton5.grid(row=1, column=1)
        self.rateuscheckbutton6=tk.Checkbutton(self.rateusframe1, text="NO", height=5, font=("Arial", 15), command=lambda:[self.togglecheck6, self.gotocommenttextboxwithdraw], variable=self.checkvar6)
        self.rateuscheckbutton6.grid(row=1, column=2)
        self.rateusframe1.pack(padx=10, pady=10)
        self.rateusbutton=tk.Button(self.rateus, text="Submit", bg="green", height=5, font=("Arial", 15), command=lambda:[self.submit, self.printresponses])
        self.rateusbutton.pack(padx=10, pady=10)
        self.rateus.mainloop()
    def togglecheck1(self):
        self.rateuscheckbutton2.deselect()
        self.rateuscheckbutton3.deselect()
        self.rateuscheckbutton4.deselect()
    def togglecheck2(self):
        self.rateuscheckbutton1.deselect()
        self.rateuscheckbutton3.deselect()
        self.rateuscheckbutton4.deselect()
    def togglecheck3(self):
        self.rateuscheckbutton1.deselect()
        self.rateuscheckbutton2.deselect()
        self.rateuscheckbutton4.deselect()
    def togglecheck4(self):
        self.rateuscheckbutton1.deselect()
        self.rateuscheckbutton2.deselect()
        self.rateuscheckbutton3.deselect()
    def togglecheck5(self):
        self.rateuscheckbutton6.deselect()
    def togglecheck6(self):
        self.rateuscheckbutton5.deselect()
    
    def submit(self):
        if not(self.checkvar1.get() or self.checkvar2.get() or self.checkvar3.get() or self.checkvar4.get() and self.checkvar5.get() or self.checkvar6.get() and self.checkvar7.get()):
            messagebox.showerror("!!!PLEASE CHECK ALL!!!")
            return
        else:
            self.rateus.withdraw()
            self.thankyoupage=tk.Toplevel(self.main)
            self.thankyoupage.geometry("500x500")
            self.thankyoupage.title("After Ratings")
            self.thankyoupage.configure(bg="aqua")
            self.thankyoupagelabel=tk.Label(self.thankyoupage, text="Thank you for your ratings!", heigh=5, font=("Arial", 20), bg="red", fg="blue")
            self.thankyoupagelabel.pack(padx=10, pady=10)
            self.thankyoupageframe1=tk.Frame(self.thankyoupage)
            self.thankyoupageframe1.columnconfigure(0, weight=1)
            self.thankyoupageframe1.columnconfigure(1, weight=1)
            self.thankyoupagebutton1=tk.Button(self.thankyoupageframe1, text="Home", height=5, font=("Arial", 15), bg="red", command=self.__init__)
            self.thankyoupagebutton1.grid(row=0, column=0, sticky="we")
            self.thankyoupagebutton2=tk.Button(self.thankyoupageframe1, text="CLOSE", height=5, font=("Arial", 15), bg="blue", command=self.thankyoupage.destroy())
            self.thankyoupagebutton2.grid(row=0, column=1, sticky="we")
            self.thankyoupageframe1.pack(padx=10, pady=10)
            self.thankyoupage.mainloop()
            
    def gotocommenttextbox(self):
        self.checkvar7=tk.StringVar()
        self.commenttextbox=tk.Text(self.rateus, height=5, font=("Arial", 15), variable=self.checkvar7)
        self.commenttextbox.pack(padx=10, pady=10)

    def gotocommenttextboxwithdraw(self):
        self.commenttextbox.forget()
        
    def gotoquiz1answerkey(self):
        self.quiz1answerkey=tk.Toplevel(self.main)
        self.quiz1answerkey.geometry("800x800")
        self.quiz1answerkey.configure(bg="aqua")
        self.quiz1answerkey.title("Quiz 1 Answer Key")
        self.quiz1answerkeylabel1=tk.Label(self.quiz1answerkey, text="Quiz 1 Answer Key", height=5, bg="red", fg="blue", font=("Arial", 20))
        self.quiz1answerkeylabel1.pack(padx=10, pady=10)
        self.quiz1answerkeyframe=tk.Frame(self.quiz1answerkey)
        self.quiz1answerkeyframe.columnconfigure(0, weight=1)
        self.quiz1answerkeyframe.columnconfigure(1, weight=1)
        self.quiz1answerkeylabel2=tk.Label(self.quiz1answerkeyframe, text="Question 1:", height=5, font=("Arial", 20), bg="black")
        self.quiz1answerkeylabel2.grid(row=0, column=0)
        self.quiz1answerkeylabel3=tk.Label(self.quiz1answerkeyframe, text="Volkswagen", height=5, font=("Arial", 17), bg="red")
        self.quiz1answerkeylabel3.grid(row=0, column=1)
        self.quiz1answerkeylabel4=tk.Label(self.quiz1answerkeyframe, text="Question 2:", height=5, font=("Arial", 20), bg="black")
        self.quiz1answerkeylabel4.grid(row=1, column=0)
        self.quiz1answerkeylabel5=tk.Label(self.quiz1answerkeyframe, text="Toyota", height=5, font=("Arial", 17), bg="red")
        self.quiz1answerkeylabel5.grid(row=1, column=1)
        self.quiz1answerkeylabel6=tk.Label(self.quiz1answerkeyframe, text="Question 3:", height=5, font=("Arial", 20), bg="black")
        self.quiz1answerkeylabel6.grid(row=2, column=0)
        self.quiz1answerkeylabel7=tk.Label(self.quiz1answerkeyframe, text="Citroën", height=5, font=("Arial", 17), bg="red")
        self.quiz1answerkeylabel7.grid(row=2, column=1)
        self.quiz1answerkeylabel8=tk.Label(self.quiz1answerkeyframe, text="Question 4:", height=5, font=("Arial", 20), bg="black")
        self.quiz1answerkeylabel8.grid(row=3, column=0)
        self.quiz1answerkeylabel9=tk.Label(self.quiz1answerkeyframe, text="Koenigsegg", height=5, font=("Arial", 17), bg="red")
        self.quiz1answerkeylabel9.grid(row=2, column=1)
        self.quiz1answerkeyframe.pack(padx=10, pady=10)
        self.quiz1answerkeybutton=tk.Button(self.quiz1answerkeyframe, text="CLOSE", height=5, font=("Arial", 15), bg="blue", command=self.quiz1answerkey.destroy())
        self.quiz1answerkeybutton.pack(padx=10, pady=10)
        self.quiz1answerkey.mainloop()

    def gotoquiz2start(self):
        self.main.withdraw()
        self.quiz2start=tk.Toplevel(self.main)
        self.quiz2start.geometry("500x500")
        self.quiz2start.configure(bg="aqua")
        self.quiz2start.title("Start Quiz 2")
        self.quiz2startlabel=tk.Label(self.quiz2start, text="Click to start Quiz 2", bg="red", fg="blue", font=("Arial", 20), height=5)
        self.quiz2startlabel.pack(padx=10, pady=10)
        self.quiz2startbutton=tk.Button(self.quiz2start, text="Start", bg="green", height=5, font=("Arial", 15), command=self.gotoquiz2question1)
        self.quiz2startbutton.pack(padx=10, pady=10)
        self.quiz2start.mainloop()
    def gotoquiz2question1(self):
        self.quiz2start.withdraw()
        self.quiz2question1=tk.Toplevel(self.main)
        self.quiz2question1.geometry("1100x1100")
        self.quiz2question1backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz2question1backroundlabel=tk.Label(self.quiz2question1, image=self.quiz2question1backroundimage)
        self.quiz2question1backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz2question1.title("Quiz 2 question 1")
        self.quiz2question1label=tk.Label(self.quiz2question1, text="Question 1", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz2question1label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz2question1, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image5=tk.PhotoImage(file="Tacobell.png")
        self.image5label=tk.Label(self.quiz2question1, image=self.image5, bd=5, relief="sunken")
        self.image5label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz2question1button1=tk.Button(self.quiz2question1, text="Starbucks", bg=bcolor1, fg=fcolor1, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question2("Starbucks"))
        self.quiz2question1button1.pack(padx=10, pady=10)
        self.quiz2question1button1.bind("<Enter>", lambda event: self.on_enter17(event, bcolor1, fcolor1))
        self.quiz2question1button1.bind("<Leave>", lambda event: self.on_leave17(event, bcolor1, fcolor1))
        self.quiz2question1button2=tk.Button(self.quiz2question1, text="Mcdonalds", bg=bcolor2, fg=fcolor2, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question2("Mcdonalds"))
        self.quiz2question1button2.pack(padx=10, pady=10)
        self.quiz2question1button2.bind("<Enter>", lambda event: self.on_enter18(event, bcolor2, fcolor2))
        self.quiz2question1button2.bind("<Leave>", lambda event: self.on_leave18(event, bcolor2, fcolor2))
        self.quiz2question1button3=tk.Button(self.quiz2question1, text="Taco Express", bg=bcolor3, fg=fcolor3, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question2("Taco Express"))
        self.quiz2question1button3.pack(padx=10, pady=10)
        self.quiz2question1button3.bind("<Enter>", lambda event: self.on_enter19(event, bcolor3, fcolor3))
        self.quiz2question1button3.bind("<Leave>", lambda event: self.on_leave19(event, bcolor3, fcolor3))
        self.quiz2question1button4=tk.Button(self.quiz2question1, text="Taco Bell", bg=bcolor4, fg=fcolor4, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question2("Taco Bell"))
        self.quiz2question1button4.pack(padx=10, pady=10)
        self.quiz2question1button4.bind("<Enter>", lambda event: self.on_enter20(event, bcolor4, fcolor4))
        self.quiz2question1button4.bind("<Leave>", lambda event: self.on_leave20(event, bcolor4, fcolor4))
        self.quiz2question1.mainloop()

    def on_enter17(self, event, bcolor1, fcolor1):
        self.quiz2question1button1["background"]=fcolor1
        self.quiz2question1button1["foreground"]=bcolor1
    def on_leave17(self, event, bcolor1, fcolor1):
        self.quiz2question1button1["background"]=bcolor1
        self.quiz2question1button1["foreground"]=fcolor1
    def on_enter18(self, event, bcolor2, fcolor2):
        self.quiz2question1button2["background"]=fcolor2
        self.quiz2question1button2["foreground"]=bcolor2
    def on_leave18(self, event, bcolor2, fcolor2):
        self.quiz2question1button2["background"]=bcolor2
        self.quiz2question1button2["foreground"]=fcolor2
    def on_enter19(self, event, bcolor3, fcolor3):
        self.quiz2question1button3["background"]=fcolor3
        self.quiz2question1button3["foreground"]=bcolor3
    def on_leave19(self, event, bcolor3, fcolor3):
        self.quiz2question1button3["background"]=bcolor3
        self.quiz2question1button3["foreground"]=fcolor3
    def on_enter20(self, event, bcolor4, fcolor4):
        self.quiz2question1button4["background"]=fcolor4
        self.quiz2question1button4["foreground"]=bcolor4
    def on_leave20(self, event, bcolor4, fcolor4):
        self.quiz2question1button4["background"]=bcolor4
        self.quiz2question1button4["foreground"]=fcolor4

        
    def gotoquiz2question2(self, button_text5):
        if button_text5=="Taco Bell":
            self.points=self.points+100
        self.quiz2question1.withdraw()
        self.quiz2question2=tk.Toplevel(self.main)
        self.quiz2question2.geometry("1100x1100")
        self.quiz2question2backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz2question2backroundlabel=tk.Label(self.quiz2question2, image=self.quiz2question2backroundimage)
        self.quiz2question2backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz2question2.title("Quiz 2 Question 2")
        self.quiz2question2label=tk.Label(self.quiz2question2, text="Question 2", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz2question2label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz2question2, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image6=tk.PhotoImage(file="In-n-out.png")
        self.image6label=tk.Label(self.quiz2question2, image=self.image6, bd=5, relief="sunken")
        self.image6label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz2question2button1=tk.Button(self.quiz2question2, text="Pizza Hut", bg=bcolor1, fg=fcolor1, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question3("Pizza Hut"))
        self.quiz2question2button1.pack(padx=10, pady=10)
        self.quiz2question2button1.bind("<Enter>", lambda event: self.on_enter21(event, bcolor1, fcolor1))
        self.quiz2question2button1.bind("<Leave>", lambda event: self.on_leave21(event, bcolor1, fcolor1))
        self.quiz2question2button2=tk.Button(self.quiz2question2, text="In-n-out", bg=bcolor2, fg=fcolor2, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question3("In-n-out"))
        self.quiz2question2button2.pack(padx=10, pady=10)
        self.quiz2question2button2.bind("<Enter>", lambda event: self.on_enter22(event, bcolor2, fcolor2))
        self.quiz2question2button2.bind("<Leave>", lambda event: self.on_leave22(event, bcolor2, fcolor2))
        self.quiz2question2button3=tk.Button(self.quiz2question2, text="Sonic", bg=bcolor3, fg=fcolor3, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question3("Sonic"))
        self.quiz2question2button3.pack(padx=10, pady=10)
        self.quiz2question2button3.bind("<Enter>", lambda event: self.on_enter23(event, bcolor3, fcolor3))
        self.quiz2question2button3.bind("<Leave>", lambda event: self.on_leave23(event, bcolor3, fcolor3))
        self.quiz2question2button4=tk.Button(self.quiz2question2, text="Subway", bg=bcolor4, fg=fcolor4, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question3("Subway"))
        self.quiz2question2button4.pack(padx=10, pady=10)
        self.quiz2question2button4.bind("<Enter>", lambda event: self.on_enter24(event, bcolor4, fcolor4))
        self.quiz2question2button4.bind("<Leave>", lambda event: self.on_leave24(event, bcolor4, fcolor4))
        self.quiz2question2.mainloop()
    
    def on_enter21(self, event, bcolor1, fcolor1):
        self.quiz2question2button1["background"]=fcolor1
        self.quiz2question2button1["foreground"]=bcolor1
    def on_leave21(self, event, bcolor1, fcolor1):
        self.quiz2question2button1["background"]=bcolor1
        self.quiz2question2button1["foreground"]=fcolor1
    def on_enter22(self, event, bcolor2, fcolor2):
        self.quiz2question2button2["background"]=fcolor2
        self.quiz2question2button2["foreground"]=bcolor2
    def on_leave22(self, event, bcolor2, fcolor2):
        self.quiz2question2button2["background"]=bcolor2
        self.quiz2question2button2["foreground"]=fcolor2
    def on_enter23(self, event, bcolor3, fcolor3):
        self.quiz2question2button3["background"]=fcolor3
        self.quiz2question2button3["foreground"]=bcolor3
    def on_leave23(self, event, bcolor3, fcolor3):
        self.quiz2question2button3["background"]=bcolor3
        self.quiz2question2button3["foreground"]=fcolor3
    def on_enter24(self, event, bcolor4, fcolor4):
        self.quiz2question2button4["background"]=fcolor4
        self.quiz2question2button4["foreground"]=bcolor4
    def on_leave24(self, event, bcolor4, fcolor4):
        self.quiz2question2button4["background"]=bcolor4
        self.quiz2question2button4["foreground"]=fcolor4

        
    def gotoquiz2question3(self, button_text6):
        if button_text6=="In-n-out":
            self.points=self.points+100
        self.quiz2question2.withdraw()
        self.quiz2question3=tk.Toplevel(self.main)
        self.quiz2question3.geometry("1100x1100")
        self.quiz2question3backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz2question3backroundlabel=tk.Label(self.quiz2question3, image=self.quiz2question3backroundimage)
        self.quiz2question3backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz2question3.title("Quiz 2 Question 3")
        self.quiz2question3label=tk.Label(self.quiz2question3, text="Question 3", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz2question3label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz2question3, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image7=tk.PhotoImage(file="Hardee's.png")
        self.image7label=tk.Label(self.quiz2question3, image=self.image7, bd=5, relief="sunken")
        self.image7label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz2question3button1=tk.Button(self.quiz2question3, text="KFC", bg=bcolor1, fg=fcolor1, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question4("KFC"))
        self.quiz2question3button1.pack(padx=10, pady=10)
        self.quiz2question3button1.bind("<Enter>", lambda event: self.on_enter25(event, bcolor1, fcolor1))
        self.quiz2question3button1.bind("<Leave>", lambda event: self.on_leave25(event, bcolor1, fcolor1))
        self.quiz2question3button2=tk.Button(self.quiz2question3, text="Arby's", bg=bcolor2, fg=fcolor2, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question4("Arby's"))
        self.quiz2question3button2.pack(padx=10, pady=10)
        self.quiz2question3button2.bind("<Enter>", lambda event: self.on_enter26(event, bcolor2, fcolor2))
        self.quiz2question3button2.bind("<Leave>", lambda event: self.on_leave26(event, bcolor2, fcolor2))
        self.quiz2question3button3=tk.Button(self.quiz2question3, text="Hardee's", bg=bcolor3, fg=fcolor3, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz2question4("Hardee's"))
        self.quiz2question3button3.pack(padx=10, pady=10)
        self.quiz2question3button3.bind("<Enter>", lambda event: self.on_enter27(event, bcolor3, fcolor3))
        self.quiz2question3button3.bind("<Leave>", lambda event: self.on_leave27(event, bcolor3, fcolor3))
        self.quiz2question3button4=tk.Button(self.quiz2question3, text="Domino's", bg=bcolor4, fg=fcolor4, height=2, width=40, font=("Aria1", 15), command=lambda:self.gotoquiz2question4("Domino's"))
        self.quiz2question3button4.pack(padx=10, pady=10)
        self.quiz2question3button4.bind("<Enter>", lambda event: self.on_enter28(event, bcolor4, fcolor4))
        self.quiz2question3button4.bind("<Leave>", lambda event: self.on_leave28(event, bcolor4, fcolor4))
        self.quiz2question3.mainloop()
    
    def on_enter25(self, event, bcolor1, fcolor1):
        self.quiz2question3button1["background"]=fcolor1
        self.quiz2question3button1["foreground"]=bcolor1
    def on_leave25(self, event, bcolor1, fcolor1):
        self.quiz2question3button1["background"]=bcolor1
        self.quiz2question3button1["foreground"]=fcolor1
    def on_enter26(self, event, bcolor2, fcolor2):
        self.quiz2question3button2["background"]=fcolor2
        self.quiz2question3button2["foreground"]=bcolor2
    def on_leave26(self, event, bcolor2, fcolor2):
        self.quiz2question3button2["background"]=bcolor2
        self.quiz2question3button2["foreground"]=fcolor2
    def on_enter27(self, event, bcolor3, fcolor3):
        self.quiz2question3button3["background"]=fcolor3
        self.quiz2question3button3["foreground"]=bcolor3
    def on_leave27(self, event, bcolor3, fcolor3):
        self.quiz2question3button3["background"]=bcolor3
        self.quiz2question3button3["foreground"]=fcolor3
    def on_enter28(self, event, bcolor4, fcolor4):
        self.quiz2question3button4["background"]=fcolor4
        self.quiz2question3button4["foreground"]=bcolor4
    def on_leave28(self, event, bcolor4, fcolor4):
        self.quiz2question3button4["background"]=bcolor4
        self.quiz2question3button4["foreground"]=fcolor4

    
        
    def gotoquiz2question4(self, button_text7):
        if button_text7=="Hardee's":
            self.points=self.points+100
        
        self.quiz2question3.withdraw()
        self.quiz2question4=tk.Toplevel(self.main)
        self.quiz2question4.geometry("1100x1100")
        self.quiz2question4backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz2question4backroundlabel=tk.Label(self.quiz2question4, image=self.quiz2question4backroundimage)
        self.quiz2question4backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz2question4.title("Question 4")
        self.quiz2question4label=tk.Label(self.quiz2question4, text="Question 4", height=5, bg="red", fg="blue", font=("Arial", 20))
        self.quiz2question4label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz2question4, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image8=tk.PhotoImage(file="Jack in the box.png")
        self.image8label=tk.Label(self.quiz2question4, image=self.image8, bd=5, relief="sunken")
        self.image8label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz2question4button1=tk.Button(self.quiz2question4, text="Mcdonalds", height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquiz2finish("Mcdonalds"))
        self.quiz2question4button1.pack(padx=10, pady=10)
        self.quiz2question4button1.bind("<Enter>", lambda event: self.on_enter29(event, bcolor1, fcolor1))
        self.quiz2question4button1.bind("<Leave>", lambda event: self.on_leave29(event, bcolor1, fcolor1))
        self.quiz2question4button2=tk.Button(self.quiz2question4, text="Burger King", height=2, width=40, bg=bcolor2, fg=fcolor2, font=("Arial", 15), command=lambda:self.gotoquiz2finish("Burger King"))
        self.quiz2question4button2.pack(padx=10, pady=10)
        self.quiz2question4button2.bind("<Enter>", lambda event: self.on_enter30(event, bcolor2, fcolor2))
        self.quiz2question4button2.bind("<Leave>", lambda event: self.on_leave30(event, bcolor2, fcolor2))
        self.quiz2question4button3=tk.Button(self.quiz2question4, text="Wendy's", height=2,width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquiz2finish("Wendy's"))
        self.quiz2question4button3.pack(padx=10, pady=10)
        self.quiz2question4button3.bind("<Enter>", lambda event: self.on_enter31(event, bcolor3, fcolor3))
        self.quiz2question4button3.bind("<Leave>", lambda event: self.on_leave31(event, bcolor3, fcolor3))
        self.quiz2question4button4=tk.Button(self.quiz2question4, text="Jack In the Box", height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquiz2finish("Jack In the Box"))
        self.quiz2question4button4.pack(padx=10, pady=10)
        self.quiz2question4button4.bind("<Enter>", lambda event: self.on_enter32(event, bcolor4, fcolor4))
        self.quiz2question4button4.bind("<Leave>", lambda event: self.on_leave32(event, bcolor4, fcolor4))
        self.quiz2question4.mainloop()

    def on_enter29(self, event, bcolor1, fcolor1):
        self.quiz2question4button1["background"]=fcolor1
        self.quiz2question4button1["foreground"]=bcolor1
    def on_leave29(self, event, bcolor1, fcolor1):
        self.quiz2question4button1["background"]=bcolor1
        self.quiz2question4button1["foreground"]=fcolor1
    def on_enter30(self, event, bcolor2, fcolor2):
        self.quiz2question4button2["background"]=fcolor2
        self.quiz2question4button2["foreground"]=bcolor2
    def on_leave30(self, event, bcolor2, fcolor2):
        self.quiz2question4button2["background"]=bcolor2
        self.quiz2question4button2["foreground"]=fcolor2
    def on_enter31(self, event, bcolor3, fcolor3):
        self.quiz2question4button3["background"]=fcolor3
        self.quiz2question4button3["foreground"]=bcolor3
    def on_leave31(self, event, bcolor3, fcolor3):
        self.quiz2question4button3["background"]=bcolor3
        self.quiz2question4button3["foreground"]=fcolor3
    def on_enter32(self, event, bcolor4, fcolor4):
        self.quiz2question4button4["background"]=fcolor4
        self.quiz2question4button4["foreground"]=bcolor4
    def on_leave32(self, event, bcolor4, fcolor4):
        self.quiz2question4button4["background"]=bcolor4
        self.quiz2question4button4["foreground"]=fcolor4

        
    def gotoquiz2finish(self, button_text8):
        if button_text8=="Jack In the Box":
            self.points=self.points+100
        self.quiz2question4.withdraw()
        self.quiz2finish=tk.Toplevel(self.main)
        self.quiz2finish.geometry("800x800")
        self.quiz2finishbackroundimage=tk.PhotoImage(file="cool.png")
        self.quiz2finishbackroundimagelabel=tk.Label(self.quiz2finish, image=self.quiz2finishbackroundimage)
        self.quiz2finishbackroundimagelabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz2finish.title("Quiz 2 finished")
        self.quiz2finishlabel=tk.Label(self.quiz2finish, text="You have finished the quiz", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz2finishlabel.pack(padx=10, pady=10)
        self.quiz2finishframe1=tk.Frame(self.quiz2finish)
        self.quiz2finishframe1.columnconfigure(0, weight=1)
        self.quiz2finishframe1.columnconfigure(1, weight=1)
        self.quiz2finishlabel3=tk.Label(self.quiz2finishframe1, text=f"Total points: {self.points}", font=("Arial", 18), height=5)
        self.quiz2finishlabel3.grid(row=0, column=1)
        self.quiz2finishframe1.pack(padx=10, pady=10)
        self.quiz2finishframe1.place(x=400, y=400)
        self.quiz2finishframe2=tk.Frame(self.quiz2finish)
        self.quiz2finishframe2.columnconfigure(0, weight=1)
        self.quiz2finishframe2.columnconfigure(1, weight=1)
        self.quiz2finishframe2.columnconfigure(2, weight=1)
        self.quiz2finishframe2.columnconfigure(3, weight=1)
        self.quiz2finishbutton1=tk.Button(self.quiz2finishframe2, text="Home", bg="red", font=("Arial", 15), height=5, command=self.__init__)
        self.quiz2finishbutton1.grid(row=0, column=0, sticky="we")
        self.quiz2finishbutton2=tk.Button(self.quiz2finishframe2, text="CLOSE", bg="blue", font=("Arial", 15), height=5, command=self.closequiz2finish)
        self.quiz2finishbutton2.grid(row=0, column=1, sticky="we")
        self.quiz2finishbutton3=tk.Button(self.quiz2finishframe2, text="Quiz 2 Answer Key", height=5, font=("Arial", 15), bg="green", command=self.gotoquiz2answerkey)
        self.quiz2finishbutton3.grid(row=0, column=2, sticky="we")
        self.quiz2finishbutton4=tk.Button(self.quiz2finishframe2, text="Rate Us", height=5, font=("Arial", 15), bg="orange", command=self.gotorateus)
        self.quiz2finishbutton4.grid(row=0, column=3, sticky="we")
        self.quiz2finishframe2.pack(padx=10, pady=10)
        self.quiz2finish.mainloop()
    def closequiz2finish(self):
        self.quiz2finish.destroy()
    
    def gotoquiz2answerkey(self):
        self.quiz2answerkey=tk.Toplevel(self.main)
        self.quiz2answerkey.geometry("800x800")
        self.quiz2answerkey.configure(bg="aqua")
        self.quiz2answerkey.title("Quiz 2 Answer Key")
        self.quiz2answerkeylabel1=tk.Label(self.quiz2answerkey, text="Quiz 2 Answer Key", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.quiz2answerkeylabel1.pack(padx=10, pady=10)
        self.quiz2answerkeyframe=tk.Frame(self.quiz2answerkey)
        self.quiz2answerkeyframe.columnconfigure(0, weight=1)
        self.quiz2answerkeyframe.columnconfigure(1, weight=1)
        self.quiz2answerkeylabel2=tk.Label(self.quiz2answerkeyframe, text="Question 1:", height=5, font=("Arial", 20), bg="black")
        self.quiz2answerkeylabel2.grid(row=0, column=0)
        self.quiz2answerkeylabel3=tk.Label(self.quiz2answerkeyframe, text="Taco Bell", height=5, font=("Arial", 17), bg="red")
        self.quiz2answerkeylabel3.grid(row=0, column=1)
        self.quiz2answerkeylabel4=tk.Label(self.quiz2answerkeyframe, text="Question 2:", height=5, font=("Arial", 20), bg="black")
        self.quiz2answerkeylabel4.grid(row=1, column=0)
        self.quiz2answerkeylabel5=tk.Label(self.quiz2answerkeyframe, text="In-in-out", height=5, font=("Arial", 17), bg="red")
        self.quiz2answerkeylabel5.grid(row=1, column=1)
        self.quiz2answerkeylabel6=tk.Label(self.quiz2answerkeyframe, text="Question 3:", height=5, font=("Arial", 20), bg="black")
        self.quiz2answerkeylabel6.grid(row=2, column=0)
        self.quiz2answerkeylabel7=tk.Label(self.quiz2answerkeyframe, text="Hardee's", height=5, font=("Arial", 20), bg="red")
        self.quiz2answerkeylabel7.grid(row=2, column=1)
        self.quiz2answerkeylabel8=tk.Label(self.quiz2answerkeyframe, text="Question 4:", height=5, font=("Arial", 20), bg="black")
        self.quiz2answerkeylabel8.grid(row=3, column=0)
        self.quiz2answerkeylabel9=tk.Label(self.quiz2answerkeyframe, text="Jack In the Box", height=5, font=("Arial", 17), bg="red")
        self.quiz2answerkeylabel9.grid(row=3, column=1)
        self.quiz2answerkeyframe.pack(padx=10, pady=10)
        self.quiz2answerkeybutton=tk.Button(self.quiz2answerkey, text="CLOSE", height=5, font=("Arial", 15), bg="blue", command=self.quiz2answerkey.destroy())
        self.quiz2answerkeybutton.pack(padx=10, pady=10)
        self.quiz2answerkey.mainloop()

        

    def gotoquiz3start(self):
        self.main.withdraw() 
        self.quiz3start=tk.Toplevel(self.main)
        self.quiz3start.geometry("500x500")
        self.quiz3start.configure(bg="aqua")
        self.quiz3start.title("Start Quiz 3")
        self.quiz3startlabel=tk.Label(self.quiz3start, text="Click to start quiz 3", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.quiz3startlabel.pack(padx=10, pady=10)
        self.quiz3startbutton=tk.Button(self.quiz3start, text="Start", height=5, font=("Arial", 15), bg="green", command=self.gotoquiz3question1)
        self.quiz3startbutton.pack(padx=10, pady=10)
        self.quiz3start.mainloop()
    def gotoquiz3question1(self):
        self.quiz3start.withdraw()
        self.quiz3question1=tk.Toplevel(self.main)
        self.quiz3question1.geometry("1100x1100")
        self.quiz3question1backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz3question1backroundlabel=tk.Label(self.quiz3question1, image=self.quiz3question1backroundimage)
        self.quiz3question1backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz3question1.title("Quiz 3 Question 1")
        self.quiz3question1label=tk.Label(self.quiz3question1, text="Quiz 1 Question 1", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz3question1label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz3question1, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image9=tk.PhotoImage(file="LG.png")
        self.image9label=tk.Label(self.quiz3question1, image=self.image9, bd=5, relief="sunken")
        self.image9label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz3question1button1=tk.Button(self.quiz3question1, text="Apple", bg=bcolor1, fg=fcolor1, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question2("Apple"))
        self.quiz3question1button1.pack(padx=10, pady=10)
        self.quiz3question1button1.bind("<Enter>", lambda event: self.on_enter33(event, bcolor1, fcolor1))
        self.quiz3question1button1.bind("<Leave>", lambda event: self.on_leave33(event, bcolor1, fcolor1))
        self.quiz3question1button2=tk.Button(self.quiz3question1, text="LG", bg=bcolor2, fg=fcolor2, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question2("LG"))
        self.quiz3question1button2.pack(padx=10, pady=10)
        self.quiz3question1button2.bind("<Enter>", lambda event: self.on_enter34(event, bcolor2, fcolor2))
        self.quiz3question1button2.bind("<Leave>", lambda event: self.on_leave34(event, bcolor2, fcolor2))
        self.quiz3question1button3=tk.Button(self.quiz3question1, text="Samsung", bg=bcolor3, fg=fcolor3, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question2("Samsung"))
        self.quiz3question1button3.pack(padx=10, pady=10)
        self.quiz3question1button3.bind("<Enter>", lambda event: self.on_enter35(event, bcolor3, fcolor3))
        self.quiz3question1button3.bind("<Leave>", lambda event: self.on_leave35(event, bcolor3, fcolor3))
        self.quiz3question1button4=tk.Button(self.quiz3question1, text="Sony", bg=bcolor4, fg=fcolor4, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question2("Sony"))
        self.quiz3question1button4.pack(padx=10, pady=10)
        self.quiz3question1button4.bind("<Enter>", lambda event: self.on_enter36(event, bcolor4, fcolor4))
        self.quiz3question1button4.bind("<Leave>", lambda event: self.on_leave36(event, bcolor4, fcolor4))
        self.quiz3question1.mainloop()

    def on_enter33(self, event, bcolor1, fcolor1):
        self.quiz3question1button1["background"]=fcolor1
        self.quiz3question1button1["foreground"]=bcolor1
    def on_leave33(self, event, bcolor1, fcolor1):
        self.quiz3question1button1["background"]=bcolor1
        self.quiz3question1button1["foreground"]=fcolor1
    def on_enter34(self, event, bcolor2, fcolor2):
        self.quiz3question1button2["background"]=fcolor2
        self.quiz3question1button2["foreground"]=bcolor2
    def on_leave34(self, event, bcolor2, fcolor2):
        self.quiz3question1button2["background"]=bcolor2
        self.quiz3question1button2["foreground"]=fcolor2
    def on_enter35(self, event, bcolor3, fcolor3):
        self.quiz3question1button3["background"]=fcolor3
        self.quiz3question1button3["foreground"]=bcolor3
    def on_leave35(self, event, bcolor3, fcolor3):
        self.quiz3question1button3["background"]=bcolor3
        self.quiz3question1button3["foreground"]=fcolor3
    def on_enter36(self, event, bcolor4, fcolor4):
        self.quiz3question1button4["background"]=fcolor4
        self.quiz3question1button4["foreground"]=bcolor4
    def on_leave36(self, event, bcolor4, fcolor4):
        self.quiz3question1button4["background"]=bcolor4
        self.quiz3question1button4["foreground"]=fcolor4


        
    
    def gotoquiz3question2(self, button_text9):
        if button_text9=="LG":
            self.points=self.points+100
        self.quiz3question1.withdraw()
        self.quiz3question2=tk.Toplevel(self.main)
        self.quiz3question2.geometry("1100x1100")
        self.quiz3question2backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz3question2backroundlabel=tk.Label(self.quiz3question2, image=self.quiz3question2backroundimage)
        self.quiz3question2backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz3question2.title("Question 3 Question 2")
        self.quiz3question2label=tk.Label(self.quiz3question2, text="Question 2", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz3question2label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz3question2, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image10=tk.PhotoImage(file="Huawei.png")
        self.image10label=tk.Label(self.quiz3question2, image=self.image10, bd=5, relief="sunken")
        self.image10label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz3question2button1=tk.Button(self.quiz3question2, text="Windows", bg=bcolor1, fg=fcolor1, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question3("Windows"))
        self.quiz3question2button1.pack(padx=10, pady=10)
        self.quiz3question2button1.bind("<Enter>", lambda event: self.on_enter37(event, bcolor1, fcolor1))
        self.quiz3question2button1.bind("<Leave>", lambda event: self.on_leave37(event, bcolor1, fcolor1))
        self.quiz3question2button2=tk.Button(self.quiz3question2, text="Panasonic", bg=bcolor2, fg=fcolor2, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question3("Panasonic"))
        self.quiz3question2button2.pack(padx=10, pady=10)
        self.quiz3question2button2.bind("<Enter>", lambda event: self.on_enter38(event, bcolor2, fcolor2))
        self.quiz3question2button2.bind("<Leave>", lambda event: self.on_leave38(event, bcolor2, fcolor2))
        self.quiz3question2button3=tk.Button(self.quiz3question2, text="Dell", bg=bcolor3, fg=fcolor3, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question3("Dell"))
        self.quiz3question2button3.pack(padx=10, pady=10)
        self.quiz3question2button3.bind("<Enter>", lambda event: self.on_enter39(event, bcolor3, fcolor3))
        self.quiz3question2button3.bind("<Leave>", lambda event: self.on_leave39(event, bcolor3, fcolor3))
        self.quiz3question2button4=tk.Button(self.quiz3question2, text="Huawei", bg=bcolor4, fg=fcolor4, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3question3("Huawei"))
        self.quiz3question2button4.pack(padx=10, pady=10)
        self.quiz3question2button4.bind("<Enter>", lambda event: self.on_enter40(event, bcolor4, fcolor4))
        self.quiz3question2button4.bind("<Leave>", lambda event: self.on_leave40(event, bcolor4, fcolor4))
        self.quiz3question2.mainloop()

    def on_enter37(self, event, bcolor1, fcolor1):
        self.quiz3question2button1["background"]=fcolor1
        self.quiz3question2button1["foreground"]=bcolor1
    def on_leave37(self, event, bcolor1, fcolor1):
        self.quiz3question2button1["background"]=bcolor1
        self.quiz3question2button1["foreground"]=fcolor1
    def on_enter38(self, event, bcolor2, fcolor2):
        self.quiz3question2button2["background"]=fcolor2
        self.quiz3question2button2["foreground"]=bcolor2
    def on_leave38(self, event, bcolor2, fcolor2):
        self.quiz3question2button2["background"]=bcolor2
        self.quiz3question2button2["foreground"]=fcolor2
    def on_enter39(self, event, bcolor3, fcolor3):
        self.quiz3question2button3["background"]=fcolor3
        self.quiz3question2button3["foreground"]=bcolor3
    def on_leave39(self, event, bcolor3, fcolor3):
        self.quiz3question2button3["background"]=bcolor3
        self.quiz3question2button3["foreground"]=fcolor3
    def on_enter40(self, event, bcolor4, fcolor4):
        self.quiz3question2button4["background"]=fcolor4
        self.quiz3question2button4["foreground"]=bcolor4
    def on_leave40(self, event, bcolor4, fcolor4):
        self.quiz3question2button4["background"]=bcolor4
        self.quiz3question2button4["foreground"]=fcolor4

        
    def gotoquiz3question3(self, button_text10):
        if button_text10=="Huawei":
            self.points=self.points+100
        self.quiz3question2.withdraw()
        self.quiz3question3=tk.Toplevel(self.main)
        self.quiz3question3.geometry("1100x1100")
        self.quiz3question3backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz3question3backroundlabel=tk.Label(self.quiz3question3, image=self.quiz3question3backroundimage)
        self.quiz3question3backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz3question3.title("Question 3")
        self.quiz3question3label=tk.Label(self.quiz3question3, text="Question 3", height=5, bg="red", fg="blue", font=("Arial", 20))
        self.quiz3question3label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz3question3, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=850, y=100)
        self.image11=tk.PhotoImage(file="Beats.png")
        self.image11label=tk.Label(self.quiz3question3, image=self.image11, bd=5, relief="sunken")
        self.image11label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz3question3button1=tk.Button(self.quiz3question3, text="Samsung", height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquiz3question4("Samsung"))
        self.quiz3question3button1.pack(padx=10, pady=10)
        self.quiz3question3button1.bind("<Enter>", lambda event: self.on_enter41(event, bcolor1, fcolor1))
        self.quiz3question3button1.bind("<Leave>", lambda event: self.on_leave41(event, bcolor1, fcolor1))
        self.quiz3question3button2=tk.Button(self.quiz3question3, text="Hp", height=2, width=40, bg=bcolor2, fg=fcolor2, font=("Arial", 15), command=lambda:self.gotoquiz3question4("Hp"))
        self.quiz3question3button2.pack(padx=10, pady=10)
        self.quiz3question3button2.bind("<Enter>", lambda event: self.on_enter42(event, bcolor2, fcolor2))
        self.quiz3question3button2.bind("<Leave>", lambda event: self.on_leave42(event, bcolor2, fcolor2))
        self.quiz3question3button3=tk.Button(self.quiz3question3, text="Beats", height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquiz3question4("Beats"))
        self.quiz3question3button3.pack(padx=10, pady=10)
        self.quiz3question3button3.bind("<Enter>", lambda event: self.on_enter43(event, bcolor3, fcolor3))
        self.quiz3question3button3.bind("<Leave>", lambda event: self.on_leave43(event, bcolor3, fcolor3))
        self.quiz3question3button4=tk.Button(self.quiz3question3, text="Dell", height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquiz3question4("Dell"))
        self.quiz3question3button4.pack(padx=10, pady=10)
        self.quiz3question3button4.bind("<Enter>", lambda event: self.on_enter44(event, bcolor4, fcolor4))
        self.quiz3question3button4.bind("<Leave>", lambda event: self.on_leave44(event, bcolor4, fcolor4))
        self.quiz3question3.mainloop()
    

    def on_enter41(self, event, bcolor1, fcolor1):
        self.quiz3question3button1["background"]=fcolor1
        self.quiz3question3button1["foreground"]=bcolor1
    def on_leave41(self, event, bcolor1, fcolor1):
        self.quiz3question3button1["background"]=bcolor1
        self.quiz3question3button1["foreground"]=fcolor1
    def on_enter42(self, event, bcolor2, fcolor2):
        self.quiz3question3button2["background"]=fcolor2
        self.quiz3question3button2["foreground"]=bcolor2
    def on_leave42(self, event, bcolor2, fcolor2):
        self.quiz3question3button2["background"]=bcolor2
        self.quiz3question3button2["foreground"]=fcolor2
    def on_enter43(self, event, bcolor3, fcolor3):
        self.quiz3question3button3["background"]=fcolor3
        self.quiz3question3button3["foreground"]=bcolor3
    def on_leave43(self, event, bcolor3, fcolor3):
        self.quiz3question3button3["background"]=bcolor3
        self.quiz3question3button3["foreground"]=fcolor3
    def on_enter44(self, event, bcolor4, fcolor4):
        self.quiz3question3button4["background"]=fcolor4
        self.quiz3question3button4["foreground"]=bcolor4
    def on_leave44(self, event, bcolor4, fcolor4):
        self.quiz3question3button4["background"]=bcolor4
        self.quiz3question3button4["foreground"]=fcolor4
    

        
    def gotoquiz3question4(self, button_text11):
        if button_text11=="Beats":
            self.points=self.points+100
        self.quiz3question3.withdraw()
        self.quiz3question4=tk.Toplevel(self.main)
        self.quiz3question4.geometry("1100x1100")
        self.quiz3question4backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz3question4backroundlabel=tk.Label(self.quiz3question4, image=self.quiz3question4backroundimage)
        self.quiz3question4backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz3question4.title("Question 4")
        self.quiz3question4label=tk.Label(self.quiz3question4, text="Question 4", height=5, bg="red", fg="blue", font=("Arial", 15))
        self.quiz3question4label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz3question4, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image12=tk.PhotoImage(file="Havells.png")
        self.image12label=tk.Label(self.quiz3question4, image=self.image12, bd=5, relief="sunken")
        self.image12label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz3question4button1=tk.Button(self.quiz3question4, text="Nokia", height=2, width=40, bg=bcolor1, fg=fcolor1, font=("Arial", 15), command=lambda:self.gotoquiz3finish("Nokia"))
        self.quiz3question4button1.pack(padx=10, pady=10)
        self.quiz3question4button1.bind("<Enter>", lambda event: self.on_enter45(event, bcolor1, fcolor1))
        self.quiz3question4button1.bind("<Leave>", lambda event: self.on_leave45(event, bcolor1, fcolor1))
        self.quiz3question4button2=tk.Button(self.quiz3question4, text="Havells", bg=bcolor2, fg=fcolor2, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz3finish("Havells"))
        self.quiz3question4button2.pack(padx=10, pady=10)
        self.quiz3question4button2.bind("<Enter>", lambda event: self.on_enter46(event, bcolor2, fcolor2))
        self.quiz3question4button2.bind("<Leave>", lambda event: self.on_leave46(event, bcolor2, fcolor2))
        self.quiz3question4button3=tk.Button(self.quiz3question4, text="Philips", height=2, width=40, bg=bcolor3, fg=fcolor3, font=("Arial", 15), command=lambda:self.gotoquiz3finish("Philips"))
        self.quiz3question4button3.pack(padx=10, pady=10)
        self.quiz3question4button3.bind("<Enter>", lambda event: self.on_enter47(event, bcolor3, fcolor3))
        self.quiz3question4button3.bind("<Leave>", lambda event: self.on_leave47(event, bcolor3, fcolor3))
        self.quiz3question4button4=tk.Button(self.quiz3question4, text="Lenovo", height=2, width=40, bg=bcolor4, fg=fcolor4, font=("Arial", 15), command=lambda:self.gotoquiz3finish("Lenovo"))
        self.quiz3question4button4.pack(padx=10, pady=10)
        self.quiz3question4button4.bind("<Enter>", lambda event: self.on_enter48(event, bcolor4, fcolor4))
        self.quiz3question4button4.bind("<Leave>", lambda event: self.on_leave48(event, bcolor4, fcolor4))
        self.quiz3question4.mainloop()

    def on_enter45(self, event, bcolor1, fcolor1):
        self.quiz3question4button1["background"]=fcolor1
        self.quiz3question4button1["foreground"]=bcolor1
    def on_leave45(self, event, bcolor1, fcolor1):
        self.quiz3question4button1["background"]=bcolor1
        self.quiz3question4button1["foreground"]=fcolor1
    def on_enter46(self, event, bcolor2, fcolor2):
        self.quiz3question4button2["background"]=fcolor2
        self.quiz3question4button2["foreground"]=bcolor2
    def on_leave46(self, event, bcolor2, fcolor2):
        self.quiz3question4button2["background"]=bcolor2
        self.quiz3question4button2["foreground"]=fcolor2
    def on_enter47(self, event, bcolor3, fcolor3):
        self.quiz3question4button3["background"]=fcolor3
        self.quiz3question4button3["foreground"]=bcolor3
    def on_leave47(self, event, bcolor3, fcolor3):
        self.quiz3question4button3["background"]=bcolor3
        self.quiz3question4button3["foreground"]=fcolor3
    def on_enter48(self, event, bcolor4, fcolor4):
        self.quiz3question4button4["background"]=fcolor4
        self.quiz3question4button4["foreground"]=bcolor4
    def on_leave48(self, event, bcolor4, fcolor4):
        self.quiz3question4button4["background"]=bcolor4
        self.quiz3question4button4["foreground"]=fcolor4
 
        
    def gotoquiz3finish(self, button_text12):
        if button_text12=="Havells":
            self.points=self.points+100
        self.quiz3question4.withdraw()
        self.quiz3finish=tk.Toplevel(self.main)
        self.quiz3finish.geometry("800x800")
        self.quiz3finishbackroundimage=tk.PhotoImage(file="cool.png")
        self.quiz3finishbackroundimagelabel=tk.Label(self.quiz3finish, image=self.quiz3finishbackroundimage)
        self.quiz3finishbackroundimagelabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz3finish.title("Quiz 4 finished")
        self.quiz3finishlabel1=tk.Label(self.quiz3finish, text="You have finished the quiz!", height=5, bg="red", fg="blue", font=("Arial", 20))
        self.quiz3finishlabel1.pack(padx=10, pady=10)
        self.quiz3finishframe1=tk.Frame(self.quiz3finish)
        self.quiz3finishframe1.columnconfigure(0, weight=1)
        self.quiz3finishframe1.columnconfigure(1, weight=1)
        self.quiz3finishlabel3=tk.Label(self.quiz3finishframe1, text=f"Total Points: {self.points}", height=5, font=("Arial", 18))
        self.quiz3finishlabel3.grid(row=0, column=1)
        self.quiz3finishframe1.place(x=400, y=400)
        self.quiz3finishframe2=tk.Frame(self.quiz3finish)
        self.quiz3finishframe2.columnconfigure(0, weight=1)
        self.quiz3finishframe2.columnconfigure(1, weight=1)
        self.quiz3finishframe2.columnconfigure(2, weight=1)
        self.quiz3finishframe2.columnconfigure(3, weight=1)
        self.quiz3finishbutton1=tk.Button(self.quiz3finishframe2, text="Home", height=5, bg="red", font=("Arial", 15), command=self.__init__)
        self.quiz3finishbutton1.grid(row=0, column=0)
        self.quiz3finishbutton2=tk.Button(self.quiz3finishframe2, text="CLOSE", height=5, bg="blue", font=("Arial", 15), command=self.closequiz3finish)
        self.quiz3finishbutton2.grid(row=0, column=1)
        self.quiz3finishbutton3=tk.Button(self.quiz3finishframe2, text="Quiz 3 Answer Key", height=5, font=("Arial", 15), bg="green", command=self.gotoquiz3answerkey)
        self.quiz3finishbutton3.grid(row=0, column=2)
        self.quiz3finishbutton4=tk.Button(self.quiz3finishframe2, text="Rate Us", height=5, font=("Arial", 15), bg="orange", command=self.gotorateus)
        self.quiz3finishbutton4.grid(row=0, column=3)
        self.quiz3finishframe1.pack(padx=10, pady=10)
        self.quiz3finishframe2.pack(padx=10, pady=10)
        self.quiz3finish.mainloop()
    def closequiz3finish(self):
        self.quiz3finish.destroy()
    def gotoquiz3answerkey(self):
        self.quiz3answerkey=tk.Toplevel(self.main)
        self.quiz3answerkey.geometry("800x800")
        self.quiz3answerkey.configure(bg="aqua")
        self.quiz3answerkey.title("Quiz 3 Answer Key")
        self.quiz3answerkeylabel1=tk.Label(self.quiz3answerkey, text="Quiz 3 Answer Key", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.quiz3answerkeylabel1.pack(padx=10, pady=10)
        self.quiz3answerkeyframe=tk.Frame(self.quiz3answerkey)
        self.quiz3answerkeyframe.columnconfigure(0, weight=1)
        self.quiz3answerkeyframe.columnconfigure(1, weight=1)
        self.quiz3answerkeylabel2=tk.Label(self.quiz3answerkeyframe, text="Question 1:", height=5, font=("Arial", 20), bg="black")
        self.quiz3answerkeylabel2.grid(row=0, column=0)
        self.quiz3answerkeylabel3=tk.Label(self.quiz3answerkeyframe, text="LG", height=5, font=("Arial", 17), bg="red")
        self.quiz3answerkeylabel3.grid(row=0, column=1)
        self.quiz3answerkeylabel4=tk.Label(self.quiz3answerkeyframe, text="Question 2:", height=5, font=("Arial", 20), bg="black")
        self.quiz3answerkeylabel4.grid(row=1, column=0)
        self.quiz3answerkeylabel5=tk.Label(self.quiz3answerkeyframe, text="Huawei", height=5, font=("Arial", 17), bg="red")
        self.quiz3answerkeylabel5.grid(row=1, column=1)
        self.quiz3answerkeylabel6=tk.Label(self.quiz3answerkeyframe, text="Question 3:", height=5, font=("Arial", 20), bg="black") 
        self.quiz3answerkeylabel6.grid(row=2, column=0)
        self.quiz3answerkeylabel7=tk.Label(self.quiz3answerkeyframe, text="Beats", height=5, font=("Arial", 17), bg="red")
        self.quiz3answerkeylabel7.grid(row=2, column=1)
        self.quiz3answerkeylabel8=tk.Label(self.quiz3answerkeyframe, text="Question 4:", height=5, font=("Arial", 20), bg="black")
        self.quiz3answerkeylabel8.grid(row=3, column=0)
        self.quiz3answerkeylabel9=tk.Label(self.quiz3answerkeyframe, text="Havells", height=5, font=("Arial", 17), bg="red")
        self.quiz3answerkeylabel9.grid(row=3, column=1)
        self.quiz3answerkeyframe.pack(padx=10, pady=10)
        self.quiz3answerkeybutton=tk.Button(self.quiz3answerkey, text="CLOSE", height=5, font=("Arial", 15), bg="blue")
        self.quiz3answerkey.mainloop()
    def gotoquiz4start(self):
        self.main.withdraw()
        self.quiz4start=tk.Toplevel(self.main)
        self.quiz4start.geometry("500x500")
        self.quiz4start.configure(bg="aqua")
        self.quiz4start.title("Start Quiz 4")
        self.quiz4startlabel=tk.Label(self.quiz4start, text="Click to start Quiz 4", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz4startlabel.pack(padx=10, pady=10)
        self.quiz4startbutton=tk.Button(self.quiz4start, text="Start", height=5, font=("Arial", 15), bg="green", command=self.gotoquiz4question1)
        self.quiz4startbutton.pack(padx=10, pady=10)
        self.quiz4start.mainloop()
    def gotoquiz4question1(self):
        self.quiz4start.withdraw()
        self.quiz4question1=tk.Toplevel(self.main)
        self.quiz4question1.geometry("1100x1100")
        self.quiz4question1backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz4question1backroundlabel=tk.Label(self.quiz4question1, image=self.quiz4question1backroundimage)
        self.quiz4question1backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz4question1.title("Quiz 4 Question 1")
        self.quiz4question1label=tk.Label(self.quiz4question1, text="Quiz 4 Question 1", bg="red", fg="blue", height=5, font=("Arial", 20))
        self.quiz4question1label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz4question1, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image13=tk.PhotoImage(file="Fila.png")
        self.image13label=tk.Label(self.quiz4question1, image=self.image13, bd=5, relief="sunken")
        self.image13label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz4question1button1=tk.Button(self.quiz4question1, text="Nike", bg=bcolor1, fg=fcolor1, height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz4question2("Nike"))
        self.quiz4question1button1.pack(padx=10, pady=10)
        self.quiz4question1button1.bind("<Enter>", lambda event: self.on_enter49(event, bcolor1, fcolor1))
        self.quiz4question1button1.bind("<Leave>", lambda event: self.on_leave49(event, bcolor1, fcolor1))
        self.quiz4question1button2=tk.Button(self.quiz4question1, text="Fila", height=2, bg=bcolor2, fg=fcolor2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz4question2("Fila"))
        self.quiz4question1button2.pack(padx=10, pady=10)
        self.quiz4question1button2.bind("<Enter>", lambda event: self.on_enter50(event, bcolor2, fcolor2))
        self.quiz4question1button2.bind("<Leave>", lambda event: self.on_leave50(event, bcolor2, fcolor2))
        self.quiz4question1button3=tk.Button(self.quiz4question1, text="Levi's", height=2, bg=bcolor3, fg=fcolor3, width=40, font=("Arial", 15), command=lambda:self.gotoquiz4question2("Levi's"))
        self.quiz4question1button3.pack(padx=10, pady=10)
        self.quiz4question1button3.bind("<Enter>", lambda event: self.on_enter51(event, bcolor3, fcolor3))
        self.quiz4question1button3.bind("<Leave>", lambda event: self.on_leave51(event, bcolor3, fcolor3))
        self.quiz4question1button4=tk.Button(self.quiz4question1, text="Adidas", height=2, bg=bcolor4, fg=fcolor4, width=40, font=("Arial", 15), command=lambda:self.gotoquiz4question2("Adidas"))
        self.quiz4question1button4.pack(padx=10, pady=10)
        self.quiz4question1button4.bind("<Enter>", lambda event: self.on_enter52(event, bcolor4, fcolor4))
        self.quiz4question1button4.bind("<Leave>", lambda event: self.on_leave52(event, bcolor4, fcolor4))
        self.quiz4question1.mainloop()

    def on_enter49(self, event, bcolor1, fcolor1):
        self.quiz4question1button1["background"]=fcolor1
        self.quiz4question1button1["foreground"]=bcolor1
    def on_leave49(self, event, bcolor1, fcolor1):
        self.quiz4question1button1["background"]=bcolor1
        self.quiz4question1button1["foreground"]=fcolor1
    def on_enter50(self, event, bcolor2, fcolor2):
        self.quiz4question1button2["background"]=fcolor2
        self.quiz4question1button2["foreground"]=bcolor2
    def on_leave50(self, event, bcolor2, fcolor2):
        self.quiz4question1button2["background"]=bcolor2
        self.quiz4question1button2["foreground"]=fcolor2
    def on_enter51(self, event, bcolor3, fcolor3):
        self.quiz4question1button3["background"]=fcolor3
        self.quiz4question1button3["foreground"]=bcolor3
    def on_leave51(self, event, bcolor3, fcolor3):
        self.quiz4question1button3["background"]=bcolor3
        self.quiz4question1button3["foreground"]=fcolor3
    def on_enter52(self, event, bcolor4, fcolor4):
        self.quiz4question1button4["background"]=fcolor4
        self.quiz4question1button4["foreground"]=bcolor4
    def on_leave52(self, event, bcolor4, fcolor4):
        self.quiz4question1button4["background"]=bcolor4
        self.quiz4question1button4["foreground"]=fcolor4

        

    def gotoquiz4question2(self, button_text13): 
        if button_text13=="Fila":
            self.points=self.points+100
        self.quiz4question1.withdraw()
        self.quiz4question2=tk.Toplevel(self.main)
        self.quiz4question2.geometry("1100x1100")
        self.quiz4question2backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz4question2backroundlabel=tk.Label(self.quiz4question2, image=self.quiz4question2backroundimage)
        self.quiz4question2backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz4question2.title("Question 4")
        self.quiz4question2label=tk.Label(self.quiz4question2, text="Question 2", bg="red", fg="blue", height=5, font=("Arial", 15))
        self.quiz4question2label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz4question2, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image14=tk.PhotoImage(file="AmericanEagle.png")
        self.image14label=tk.Label(self.quiz4question2, image=self.image14, bd=5, relief="sunken")
        self.image14label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz4question2button1=tk.Button(self.quiz4question2, text="American Eagle", bg="red", height=2, width=40, font=("Arial", 15), command=lambda:self.gotoquiz4question3("American Eagle"))
        self.quiz4question2button1.pack(padx=10, pady=10)
        self.quiz4question2button1.bind("<Enter>", lambda event: self.on_enter53(event, bcolor1, fcolor1))
        self.quiz4question2button1.bind("<Leave>", lambda event: self.on_leave53(event, bcolor1, fcolor1))
        self.quiz4question2button2=tk.Button(self.quiz4question2, text="Gucci", height=2, width=40, bg="blue", font=("Arial", 15), command=lambda:self.gotoquiz4question3("Gucci"))
        self.quiz4question2button2.pack(padx=10, pady=10)
        self.quiz4question2button2.bind("<Enter>", lambda event: self.on_enter54(event, bcolor2, fcolor2))
        self.quiz4question2button2.bind("<Leave>", lambda event: self.on_leave54(event, bcolor2, fcolor2))
        self.quiz4question2button3=tk.Button(self.quiz4question2, text="Lacoste", height=2, width=40, bg="green", font=("Arial", 15), command=lambda:self.gotoquiz4question3("Lacoste"))
        self.quiz4question2button3.pack(padx=10, pady=10)
        self.quiz4question2button3.bind("<Enter>", lambda event: self.on_enter55(event, bcolor3, fcolor3))
        self.quiz4question2button3.bind("<Leave>", lambda event: self.on_leave55(event, bcolor3, fcolor3))
        self.quiz4question2button4=tk.Button(self.quiz4question2, text="Tomy Hilfiger", height=2, width=40, bg="orange", font=("Arial", 15), command=lambda:self.gotoquiz4question3("Tomy Hilfiger"))
        self.quiz4question2button4.pack(padx=10, pady=10)
        self.quiz4question2button4.bind("<Enter>", lambda event: self.on_enter56(event, bcolor4, fcolor4))
        self.quiz4question2button4.bind("<Leave>", lambda event: self.on_leave56(event, bcolor4, fcolor4))
        self.quiz4question2.mainloop()
    
    def on_enter53(self, event, bcolor1, fcolor1):
        self.quiz4question2button1["background"]=fcolor1
        self.quiz4question2button1["foreground"]=bcolor1
    def on_leave53(self, event, bcolor1, fcolor1):
        self.quiz4question2button1["background"]=bcolor1
        self.quiz4question2button1["foreground"]=fcolor1
    def on_enter54(self, event, bcolor2, fcolor2):
        self.quiz4question2button2["background"]=fcolor2
        self.quiz4question2button2["foreground"]=bcolor2
    def on_leave54(self, event, bcolor2, fcolor2):
        self.quiz4question2button2["background"]=bcolor2
        self.quiz4question2button2["foreground"]=fcolor2
    def on_enter55(self, event, bcolor3, fcolor3):
        self.quiz4question2button3["background"]=fcolor3
        self.quiz4question2button3["foreground"]=bcolor3
    def on_leave55(self, event, bcolor3, fcolor3):
        self.quiz4question2button3["background"]=bcolor3
        self.quiz4question2button3["foreground"]=fcolor3
    def on_enter56(self, event, bcolor4, fcolor4):
        self.quiz4question2button4["background"]=fcolor4
        self.quiz4question2button4["foreground"]=bcolor4
    def on_leave56(self, event, bcolor4, fcolor4):
        self.quiz4question2button4["background"]=bcolor4
        self.quiz4question2button4["foreground"]=fcolor4

    def gotoquiz4question3(self, button_text14):
        if button_text14=="American Eagle":
            self.points=self.points+100
        self.quiz4question2.withdraw()
        self.quiz4question3=tk.Toplevel(self.main)
        self.quiz4question3.geometry("1100x1100")
        self.quiz4question3backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz4question3backroundlabel=tk.Label(self.quiz4question3, image=self.quiz4question3backroundimage)
        self.quiz4question3backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz4question3.title("Question 3")
        self.quiz4question3label=tk.Label(self.quiz4question3, text="Question 4", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.quiz4question3label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz4question3, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image15=tk.PhotoImage(file="Gucci.png")
        self.image15label=tk.Label(self.quiz4question3, image=self.image15, bd=5, relief="sunken")
        self.image15label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz4question3button1=tk.Button(self.quiz4question3, text="Gucci", height=2, width=40, font=("Arial", 15), bg=bcolor1, fg=fcolor1, command=lambda:self.gotoquiz4question4("Gucci"))
        self.quiz4question3button1.pack(padx=10, pady=10)
        self.quiz4question3button1.bind("<Enter>", lambda event: self.on_enter57(event, bcolor1, fcolor1))
        self.quiz4question3button1.bind("<Leave>", lambda event: self.on_leave57(event, bcolor1, fcolor1))
        self.quiz4question3button2=tk.Button(self.quiz4question3, text="Vans", height=2, width=40, font=("Arial", 15), bg=bcolor2, fg=fcolor2, command=lambda:self.gotoquiz4question4("Vans"))
        self.quiz4question3button2.pack(padx=10, pady=10)
        self.quiz4question3button2.bind("<Enter>", lambda event: self.on_enter58(event, bcolor2, fcolor2))
        self.quiz4question3button2.bind("<Leave>", lambda event: self.on_leave58(event, bcolor2, fcolor2))
        self.quiz4question3button3=tk.Button(self.quiz4question3, text="Puma", height=2, width=40, font=("Arial", 15), bg=bcolor3, fg=fcolor3, command=lambda:self.gotoquiz4question4("Puma"))
        self.quiz4question3button3.pack(padx=10, pady=10)
        self.quiz4question3button3.bind("<Enter>", lambda event: self.on_enter59(event, bcolor3, fcolor3))
        self.quiz4question3button3.bind("<Leave>", lambda event: self.on_leave59(event, bcolor3, fcolor3))
        self.quiz4question3button4=tk.Button(self.quiz4question3, text="Gap", height=2, width=40, font=("Arial", 15), bg=bcolor4, fg=fcolor4, command=lambda:self.gotoquiz4question4("Gap"))
        self.quiz4question3button4.pack(padx=10, pady=10)
        self.quiz4question3button4.bind("<Enter>", lambda event: self.on_enter60(event, bcolor4, fcolor4))
        self.quiz4question3button4.bind("<Leave>", lambda event: self.on_leave60(event, bcolor4, fcolor4))
        self.quiz4question3.mainloop()
    
    def on_enter57(self, event, bcolor1, fcolor1):
        self.quiz4question3button1["background"]=fcolor1
        self.quiz4question3button1["foreground"]=bcolor1
    def on_leave57(self, event, bcolor1, fcolor1):
        self.quiz4question3button1["background"]=bcolor1
        self.quiz4question3button1["foreground"]=fcolor1
    def on_enter58(self, event, bcolor2, fcolor2):
        self.quiz4question3button2["background"]=fcolor2
        self.quiz4question3button2["foreground"]=bcolor2
    def on_leave58(self, event, bcolor2, fcolor2):
        self.quiz4question3button2["background"]=bcolor2
        self.quiz4question3button2["foreground"]=fcolor2
    def on_enter59(self, event, bcolor3, fcolor3):
        self.quiz4question3button3["background"]=fcolor3
        self.quiz4question3button3["foreground"]=bcolor3
    def on_leave59(self, event, bcolor3, fcolor3):
        self.quiz4question3button3["background"]=bcolor3
        self.quiz4question3button3["foreground"]=fcolor3
    def on_enter60(self, event, bcolor4, fcolor4):
        self.quiz4question3button4["background"]=fcolor4
        self.quiz4question3button4["foreground"]=bcolor4
    def on_leave60(self, event, bcolor4, fcolor4):
        self.quiz4question3button4["background"]=bcolor4
        self.quiz4question3button4["foreground"]=fcolor4

    
    def gotoquiz4question4(self, button_text15):
        if button_text15=="Gucci":
            self.points=self.points+100
        
        self.quiz4question3.withdraw()
        self.quiz4question4=tk.Toplevel(self.main)
        self.quiz4question4.geometry("1100x1100")
        self.quiz4question4backroundimage=tk.PhotoImage(file="nice.png")
        self.quiz4question4backroundlabel=tk.Label(self.quiz4question4, image=self.quiz4question4backroundimage)
        self.quiz4question4backroundlabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz4question4.title("Question 4")
        self.quiz4question4label=tk.Label(self.quiz4question4, text="Question 4", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.quiz4question4label.pack(padx=10, pady=10)
        self.score=tk.Label(self.quiz4question4, text=f"Points: {self.points}", height=2, font=("Arial", 17))
        self.score.place(x=1100, y=20)
        self.image16=tk.PhotoImage(file="UnderArmour.png")
        self.image16label=tk.Label(self.quiz4question4, image=self.image16,bd=5, relief="sunken")
        self.image16label.pack(padx=10, pady=10)
        bcolor1="#141414"
        fcolor1="#ffcc66"
        bcolor2="#141414"
        fcolor2="#66CDAA"
        bcolor3="#141414"
        fcolor3="#DC143C"
        bcolor4="#141414"
        fcolor4="#9400D3"
        self.quiz4question4button1=tk.Button(self.quiz4question4, text="Prada", height=2, width=40, font=("Arial", 15), bg=bcolor1, fg=fcolor1, command=lambda:self.gotoquiz4finish("Prada"))
        self.quiz4question4button1.pack(padx=10, pady=10)
        self.quiz4question4button1.bind("<Enter>", lambda event: self.on_enter61(event, bcolor1, fcolor1))
        self.quiz4question4button1.bind("<Leave>", lambda event: self.on_leave61(event, bcolor1, fcolor1))
        self.quiz4question4button2=tk.Button(self.quiz4question4, text="Under Armour", height=2, width=40, font=("Arial", 15), bg=bcolor2, fg=fcolor2, command=lambda:self.gotoquiz4finish("Under Armour"))
        self.quiz4question4button2.pack(padx=10, pady=10)
        self.quiz4question4button2.bind("<Enter>", lambda event: self.on_enter62(event, bcolor2, fcolor2))
        self.quiz4question4button2.bind("<Leave>", lambda event: self.on_leave62(event, bcolor2, fcolor2))
        self.quiz4question4button3=tk.Button(self.quiz4question4, text="Reebok", height=2, width=40, font=("Arial", 15), bg=bcolor3, fg=fcolor3, command=lambda:self.gotoquiz4finish("Reebok"))
        self.quiz4question4button3.pack(padx=10, pady=10)
        self.quiz4question4button3.bind("<Enter>", lambda event: self.on_enter63(event, bcolor3, fcolor3))
        self.quiz4question4button3.bind("<Leave>", lambda event: self.on_leave63(event, bcolor3, fcolor3))
        self.quiz4question4button4=tk.Button(self.quiz4question4, text="Versace", height=2, width=40, font=("Arial", 15), bg=bcolor4, fg=fcolor4, command=lambda:self.gotoquiz4finish("Versace"))
        self.quiz4question4button4.pack(padx=10, pady=10)
        self.quiz4question4button4.bind("<Enter>", lambda event: self.on_enter64(event, bcolor4, fcolor4))
        self.quiz4question4button4.bind("<Leave>", lambda event: self.on_leave64(event, bcolor4, fcolor4))
        self.quiz4question4.mainloop()

    def on_enter61(self, event, bcolor1, fcolor1):
        self.quiz4question4button1["background"]=fcolor1
        self.quiz4question4button1["foreground"]=bcolor1
    def on_leave61(self, event, bcolor1, fcolor1):
        self.quiz4question4button1["background"]=bcolor1
        self.quiz4question4button1["foreground"]=fcolor1
    def on_enter62(self, event, bcolor2, fcolor2):
        self.quiz4question4button2["background"]=fcolor2
        self.quiz4question4button2["foreground"]=bcolor2
    def on_leave62(self, event, bcolor2, fcolor2):
        self.quiz4question4button2["background"]=bcolor2
        self.quiz4question4button2["foreground"]=fcolor2
    def on_enter63(self, event, bcolor3, fcolor3):
        self.quiz4question4button3["background"]=fcolor3
        self.quiz4question4button3["foreground"]=bcolor3
    def on_leave63(self, event, bcolor3, fcolor3):
        self.quiz4question4button3["background"]=bcolor3
        self.quiz4question4button3["foreground"]=fcolor3
    def on_enter64(self, event, bcolor4, fcolor4):
        self.quiz4question4button4["background"]=fcolor4
        self.quiz4question4button4["foreground"]=bcolor4
    def on_leave64(self, event, bcolor4, fcolor4):
        self.quiz4question4button4["background"]=bcolor4
        self.quiz4question4button4["foreground"]=fcolor4

    
    def gotoquiz4finish(self, button_text16):
        if button_text16=="Under Amour":
            self.points=self.points+100
        self.quiz4question4.withdraw()
        self.quiz4finish=tk.Toplevel(self.main)
        self.quiz4finish.geometry("800x800")
        self.quiz4finishbackroundimage=tk.PhotoImage(file="cool.png")
        self.quiz4finishbackroundimagelabel=tk.Label(self.quiz4finish, image=self.quiz4finishbackroundimage)
        self.quiz4finishbackroundimagelabel.place(x=0, y=0, relheight=1, relwidth=1)
        self.quiz4finish.title("Quiz 4 finished")
        self.quiz4finishlabel=tk.Label(self.quiz4finish, text="You have finished the quiz!", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.quiz4finishlabel.pack(padx=10, pady=10)
        self.quiz4finishframe1=tk.Frame(self.quiz4finish)
        self.quiz4finishframe1.columnconfigure(0, weight=1)
        self.quiz4finishframe1.columnconfigure(1, weight=1)
        self.quiz4finishlabel2=tk.Label(self.quiz4finishframe1, text="Score(out of 400)", height=5, font=("Arial", 20), bg="green", fg="red")
        self.quiz4finishlabel2.grid(row=0, column=0)
        self.quiz4finishlabel3=tk.Label(self.quiz4finishframe1, text=f"Total Points: {self.points}", height=5, font=("Arial", 18))
        self.quiz4finishlabel3.grid(row=0, column=1)
        self.quiz4finishframe1.place(x=400, y=400)
        self.quiz4finishframe2=tk.Frame(self.quiz4finish)
        self.quiz4finishframe2.columnconfigure(0, weight=1)
        self.quiz4finishframe2.columnconfigure(1, weight=1)
        self.quiz4finishframe2.columnconfigure(2, weight=1)
        self.quiz4finishframe2.columnconfigure(3, weight=1)
        self.quiz4finishbutton1=tk.Button(self.quiz4finishframe2, text="Home", height=5, font=("Arial", 15), bg="red", command=self.__init__)
        self.quiz4finishbutton1.grid(row=0, column=0, sticky="we")
        self.quiz4finishbutton2=tk.Button(self.quiz4finishframe2, text="CLOSE", height=5, font=("Arial", 15), bg="blue", command=self.closequiz4finish)
        self.quiz4finishbutton2.grid(row=0, column=1, sticky="we")
        self.quiz4finishbutton3=tk.Button(self.quiz4finishframe2, text="Quiz 4 Answer Key", height=5, font=("Arial", 15), bg="green", command=self.gotoquiz4answerkey)
        self.quiz4finishbutton3.grid(row=0, column=2, sticky="we")
        self.quiz4finishbutton4=tk.Button(self.quiz4finishframe2, text="Rate Us", height=5, font=("Arial", 15), bg="orange", command=self.gotorateus)
        self.quiz4finishbutton4.grid(row=0, column=3)
        self.quiz4finishframe1.pack(padx=10, pady=10)
        self.quiz4finishframe2.pack(padx=10, pady=10)
        self.quiz4finish.mainloop()
    def closequiz4finish(self):
        self.quiz4finish.destroy()
    def gotoquiz4answerkey(self):
        self.quiz4answerkey=tk.Toplevel(self.main)
        self.quiz4answerkey.geometry("800x800")
        self.quiz4answerkey.configure(bg="aqua")
        self.quiz4answerkey.title("Quiz 4 Answer Key")
        self.quiz4answerkeylabel1=tk.Label(self.quiz4answerkey, text="Quiz 4 Answer Key", height=5, font=("Arial", 20), bg="red", fg="blue")
        self.quiz4answerkeylabel1.pack(padx=10, pady=10)
        self.quiz4answerkeyframe=tk.Frame(self.quiz4answerkey)
        self.quiz4answerkeyframe.columnconfigure(0, weight=1)
        self.quiz4answerkeyframe.columnconfigure(1, weight=1)
        self.quiz4answerkeylabel2=tk.Label(self.quiz4answerkeyframe, text="Question 1:", height=5, font=("Arial", 20), bg="black")
        self.quiz4answerkeylabel2.grid(row=0, column=0)
        self.quiz4answerkeylabel3=tk.Label(self.quiz4answerkeyframe, text="Fila", height=5, font=("Arial", 17), bg="red")
        self.quiz4answerkeylabel3.grid(row=0, column=1)
        self.quiz4answerkeylabel4=tk.Label(self.quiz4answerkeyframe, text="Question 2:", height=5, font=("Arial", 20), bg="black")
        self.quiz4answerkeylabel4.grid(row=1, column=0)
        self.quiz4answerkeylabel5=tk.Label(self.quiz4answerkeyframe, text="American Eagle", height=5, font=("Arial", 17), bg="red")
        self.quiz4answerkeylabel5.grid(row=1, column=1)
        self.quiz4answerkeylabel6=tk.Label(self.quiz4answerkeyframe, text="Question 3:", height=5, font=("Arial", 20), bg="black")
        self.quiz4answerkeylabel6.grid(row=2, column=0)
        self.quiz4answerkeylabel7=tk.Label(self.quiz4answerkeyframe, text="Gucci", height=5, font=("Arial", 17), bg="red")
        self.quiz4answerkeylabel7.grid(row=2, column=1)
        self.quiz4answerkeylabel8=tk.Label(self.quiz4answerkeyframe, text="Question 4:", height=5, font=("Arial", 20), bg="black")
        self.quiz4answerkeylabel8.grid(row=3, column=0)
        self.quiz4answerkeylabel9=tk.Label(self.quiz4answerkeyframe, text="Under Armour", height=5, font=("Arial", 17), bg="red")
        self.quiz4answerkeylabel9.grid(row=3, column=1)
        self.quiz4answerkeyframe.pack(padx=10, pady=10)
        self.quiz4answerkeybutton=tk.Button(self.quiz4answerkeyframe, text="CLOSE", height=5, font=("Arial", 15), bg="blue")
        self.quiz4answerkeybutton.pack(padx=10, pady=10)
        self.quiz4answerkey.mainloop()
    def printresponses(self):
        if self.checkvar1.get():
            print("How good was our application: Solid")
        elif self.checkvar2.get():
            print("How good was our application: Decent")
        elif self.checkvar3.get():
            print("How good was our application: Really Bad")
        else:
            print("How good was our application: Bad")
        if self.checkvar6.get():
            print("Do you think there are any improvements/adjustments that can be made: Yes")
            print("Explain:", self.commenttextbox.get())
        else:
            print("Do you think there are any improvements/adjustments that can be made: No")
GUI()



        

        



        


    

    
        



        


